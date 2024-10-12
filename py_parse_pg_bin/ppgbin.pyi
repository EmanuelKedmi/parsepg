import typing

from py_parse_pg_bin.contracts import TableInfo

T = typing.TypeVar('T')


def parse_element(data: bytes, field_type: type[T]) -> T: ...


def parse_array(array_data: bytes, field_type: type[T]) -> list[T]: ...


@typing.overload
def parse_field(
    data: bytes, field_type: type[T], is_array: typing.Literal[True]) -> list[T]: ...


@typing.overload
def parse_field(
    data: bytes, field_type: type[T], is_array: typing.Literal[False]) -> T: ...


@typing.overload
def parse_field(
    data: bytes, field_type: type[T], is_array: bool) -> T | list[T]: ...


def parse_field(
    data: bytes, field_type: type[T], is_array: bool) -> T | list[T]: ...


def parse_pgbin(
    data: bytes, table_info: TableInfo) -> tuple[tuple[typing.Any, ...], ...]: ...
