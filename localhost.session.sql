-- postgres
-- create table named data with columns called col1-col10,
-- with types int, float, text, date, and boolean, the the reset of same type but arrays.
-- mix in nullability and default values.
CREATE TABLE IF NOT EXISTS data (
    col1 int,
    col2 float,
    col3 text,
    col4 date,
    col5 boolean,
    col6 int [],
    col7 float [],
    col8 text [],
    col9 date [],
    col10 boolean []
);
INSERT INTO data (
        col1,
        col2,
        col3,
        col4,
        col5,
        col6,
        col7,
        col8,
        col9,
        col10
    )
values (
        1,
        1.1,
        'one',
        '2021-01-01',
        true,
        '{1,2,3}',
        '{1.1,2.2,3.3}',
        '{"one","two","three"}',
        '{"2021-01-01","2021-01-02","2021-01-03"}',
        '{true,false,true}'
    ),
    (
        2,
        2.2,
        'two',
        '2021-02-01',
        false,
        '{4,5,6}',
        '{4.4,5.5,6.6}',
        '{"four","five","six"}',
        '{"2021-02-01","2021-02-02","2021-02-03"}',
        '{false,true,false}'
    ),
    (
        3,
        3.3,
        'three',
        '2021-03-01',
        true,
        '{7,8,9}',
        '{7.7,8.8,9.9}',
        '{"seven","eight","nine"}',
        '{"2021-03-01","2021-03-02","2021-03-03"}',
        '{true,false,true}'
    );
COPY (
    SELECT *
    FROM data
) TO '/tmp/data1.bin' (FORMAT BINARY);