from dataclasses import make_dataclass
from typing import Any
try:
    from py_parse_pg_bin import ppgbin
except ImportError:
    from py_parse_pg_bin import pyppgbin as ppgbin
from py_parse_pg_bin import contracts as c


_cls_cache: dict[c.TableInfo, type] = {}


def parse(data: bytes, table_info: c.TableInfo) -> tuple[Any, ...]:
    if table_info not in _cls_cache:
        _cls_cache[table_info] = make_dataclass(
            table_info.name,
            [
                (field_info.name, c.annotation_mapping[field_info.type])
                for field_info
                in table_info.fields_info
            ],
            slots=True,
        )
    cls = _cls_cache[table_info]

    return tuple(
        cls(*t)
        for t
        in ppgbin.parse_pgbin(data, table_info)
    )
