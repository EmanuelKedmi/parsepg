import struct
from datetime import date, timedelta
from itertools import cycle
from typing import Any, Literal, TypeVar, overload


from py_parse_pg_bin.contracts import TableInfo, annotation_mapping


T = TypeVar('T')


def parse_element(data: bytes, field_type: type[T]) -> T:
    if field_type == int:
        return int.from_bytes(data, 'big')  # type: ignore
    elif field_type == float:
        return struct.unpack('!d', data)[0]
    elif field_type == str:
        return data.decode()  # type: ignore
    elif field_type == date:
        days_since_epoch = int.from_bytes(data, 'big')
        postgres_epoch = date(2000, 1, 1)
        return postgres_epoch + timedelta(days=days_since_epoch)  # type: ignore # noqa
    elif field_type == bool:
        return bool.from_bytes(data, 'big')  # type: ignore
    raise Exception(f'Unknown field type: {field_type}')


def parse_array(array_data: bytes, field_type: type[T]):
    num_dimensions = int.from_bytes(array_data[:4], 'big')
    flags = int.from_bytes(array_data[4:8], 'big')  # pyright: ignore[reportUnusedVariable] # noqa
    element_type_oid = int.from_bytes(array_data[8:12], 'big')  # pyright: ignore[reportUnusedVariable] # noqa
    array_data = array_data[12:]
    dimensions: list[tuple[int, int]] = []
    for _ in range(num_dimensions):
        num_elements = int.from_bytes(array_data[:4], 'big')
        lower_bound = int.from_bytes(array_data[4:8], 'big')
        dimensions.append((num_elements, lower_bound))
        array_data = array_data[8:]
    elements: list[T] = []
    for num_elements, _ in dimensions:
        for _ in range(num_elements):
            element_size = int.from_bytes(array_data[:4], 'big')
            element_data = array_data[4:4+element_size]
            elements.append(parse_element(element_data, field_type))
            array_data = array_data[4+element_size:]
    return elements


@overload
def parse_field(
    data: bytes, field_type: type[T], is_array: Literal[True]) -> list[T]: ...


@overload
def parse_field(
    data: bytes, field_type: type[T], is_array: Literal[False]) -> T: ...


@overload
def parse_field(
    data: bytes, field_type: type[T], is_array: bool) -> T | list[T]: ...


def parse_field(data: bytes, field_type: type[T], is_array: bool) -> T | list[T]:
    if is_array:
        return parse_array(data, field_type)
    return parse_element(data, field_type)


def parse_pgbin(data: bytes, table_info: TableInfo) -> tuple[tuple[Any, ...], ...]:
    signature = data[:11]
    if signature != b'PGCOPY\n\377\r\n\0':
        raise Exception('Invalid signature')

    flags = int.from_bytes(data[11:15], 'big')
    has_oids = bool(flags & 0b0000_0000_0000_0000_1000_0000_0000_0000)
    _ = has_oids

    headers_size = int.from_bytes(data[15:19], 'big')
    headers = data[19:19+headers_size]
    _ = headers

    data = data[19+headers_size:]

    field_infos = cycle(table_info.fields_info)

    tuples: list[tuple[Any, ...]] = []
    while len(data) > 2:
        fields_count = int.from_bytes(data[:2], "big")
        data = data[2:]
        fields: list[Any] = []
        while fields_count > 0:
            field_info = next(field_infos)
            field_size = int.from_bytes(data[:4], 'big')
            field_data = data[4:4+field_size]
            field_type = annotation_mapping[field_info.type]
            is_array = field_info.is_array
            fields.append(parse_field(field_data, field_type, is_array))

            data = data[4+field_size:]
            fields_count -= 1
        tuples.append(tuple(fields))
    return tuple(tuples)
