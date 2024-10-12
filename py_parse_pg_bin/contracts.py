import enum
import datetime


class FieldType(str, enum.Enum):
    INT = 'int'
    TEXT = 'text'
    BOOL = 'bool'
    BYTEA = 'bytea'
    FLOAT = 'float'
    DATE = 'date'
    TIME = 'time'
    TIMESTAMP = 'timestamp'
    TIMESTAMPTZ = 'timestamptz'
    JSON = 'json'
    JSONB = 'jsonb'


annotation_mapping: dict[FieldType, type] = {
    FieldType.INT: int,
    FieldType.TEXT: str,
    FieldType.BOOL: bool,
    FieldType.BYTEA: bytes,
    FieldType.FLOAT: float,
    FieldType.DATE: datetime.date,
    FieldType.TIME: datetime.time,
    FieldType.TIMESTAMP: datetime.datetime,
    FieldType.TIMESTAMPTZ: datetime.datetime,
    FieldType.JSON: object,
    FieldType.JSONB: object,
}


class FieldInfo:
    def __init__(self, name: str, type: FieldType, is_array: bool = False, is_nullable: bool = True) -> None:
        self.name = name
        self.type = type
        self.is_array = is_array
        self.is_nullable = is_nullable

    def __hash__(self) -> int:
        return hash((self.name, self.type, self.is_array, self.is_nullable))


class TableInfo:
    def __init__(self, name: str, fields_info: list[FieldInfo]) -> None:
        self.name = name
        self.fields_info = fields_info

    def __hash__(self) -> int:
        return hash((self.name, tuple(self.fields_info)))
