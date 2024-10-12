from datetime import date
from py_parse_pg_bin.parse import parse
from py_parse_pg_bin.contracts import FieldInfo, FieldType, TableInfo


def test_parse():
    with open('tests/data/data1.bin', 'rb') as f:
        data = f.read()

    table_info = TableInfo(
        name='data',
        fields_info=[
            FieldInfo(name='col1', type=FieldType.INT),
            FieldInfo(name='col2', type=FieldType.FLOAT),
            FieldInfo(name='col3', type=FieldType.TEXT),
            FieldInfo(name='col4', type=FieldType.DATE),
            FieldInfo(name='col5', type=FieldType.BOOL),
            FieldInfo(name='col6', type=FieldType.INT, is_array=True),
            FieldInfo(name='col7', type=FieldType.FLOAT, is_array=True),
            FieldInfo(name='col8', type=FieldType.TEXT, is_array=True),
            FieldInfo(name='col9', type=FieldType.DATE, is_array=True),
            FieldInfo(name='col10', type=FieldType.BOOL, is_array=True),
        ]
    )

    data_table_rows = parse(data, table_info)

    assert type(data_table_rows) == tuple
    assert len(data_table_rows) == 3
    assert data_table_rows[0].col1 == 1
    assert data_table_rows[0].col2 == 1.1
    assert data_table_rows[0].col3 == 'one'
    assert data_table_rows[0].col4 == date(2021, 1, 1)
    assert data_table_rows[0].col5 is True
    assert data_table_rows[0].col6 == [1, 2, 3]
    assert data_table_rows[0].col7 == [1.1, 2.2, 3.3]
    assert data_table_rows[0].col8 == ['one', 'two', 'three']
    assert data_table_rows[0].col9 == [
        date(2021, 1, 1), date(2021, 1, 2), date(2021, 1, 3)]
    assert data_table_rows[0].col10 == [True, False, True]

    assert data_table_rows[1].col1 == 2
    assert data_table_rows[1].col2 == 2.2
    assert data_table_rows[1].col3 == 'two'
    assert data_table_rows[1].col4 == date(2021, 2, 1)
    assert data_table_rows[1].col5 is False
    assert data_table_rows[1].col6 == [4, 5, 6]
    assert data_table_rows[1].col7 == [4.4, 5.5, 6.6]
    assert data_table_rows[1].col8 == ['four', 'five', 'six']
    assert data_table_rows[1].col9 == [
        date(2021, 2, 1), date(2021, 2, 2), date(2021, 2, 3)]
    assert data_table_rows[1].col10 == [False, True, False]

    assert data_table_rows[2].col1 == 3
    assert data_table_rows[2].col2 == 3.3
    assert data_table_rows[2].col3 == 'three'
    assert data_table_rows[2].col4 == date(2021, 3, 1)
    assert data_table_rows[2].col5 is True
    assert data_table_rows[2].col6 == [7, 8, 9]
    assert data_table_rows[2].col7 == [7.7, 8.8, 9.9]
    assert data_table_rows[2].col8 == ['seven', 'eight', 'nine']
    assert data_table_rows[2].col9 == [
        date(2021, 3, 1), date(2021, 3, 2), date(2021, 3, 3)]
    assert data_table_rows[2].col10 == [True, False, True]


if __name__ == '__main__':
    test_parse()
