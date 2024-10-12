DROP TABLE IF EXISTS numerics;
CREATE TABLE numerics (
    col0 smallint,
    col1 int,
    col2 bigint,
    col3 decimal,
    col4 numeric,
    col5 DOUBLE PRECISION,
    col6 smallserial,
    col7 serial,
    col8 bigserial,
    col0_a smallint[],
    col1_a int[],
    col2_a bigint[],
    col3_a decimal[],
    col4_a numeric[],
    col5_a DOUBLE PRECISION[],
    col6_a smallserial[],
    col7_a serial[],
    col8_a bigserial[],
    col0_nn smallint NOT NULL,
    col1_nn int NOT NULL,
    col2_nn bigint NOT NULL,
    col3_nn decimal NOT NULL,
    col4_nn numeric NOT NULL,
    col5_nn DOUBLE PRECISION NOT NULL,
    col6_nn smallserial NOT NULL,
    col7_nn serial NOT NULL,
    col8_nn bigserial NOT NULL
);
INSERT INTO numerics (
    col0, col1, col2, col3, col4, col5, col6, col7, col8,
    col0_a, col1_a, col2_a, col3_a, col4_a, col5_a, col6_a, col7_a, col8_a,
    col0_nn, col1_nn, col2_nn, col3_nn, col4_nn, col5_nn, col6_nn, col7_nn, col8_nn
) VALUES
    -- Test normal types with valid values
    (1, 100, 1000, 10.5, 20.5, 30.5, 1, 1, 1, 
    NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 
    1, 100, 1000, 10.5, 20.5, 30.5, 1, 1, 1),

    -- Test normal types with boundary values
    (32767, 2147483647, 9223372036854775807, 9999999999.9999, 9999999999.9999, 1.7976931348623157E+308, 32767, 2147483647, 9223372036854775807, 
    NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 
    32767, 2147483647, 9223372036854775807, 9999999999.9999, 9999999999.9999, 1.7976931348623157E+308, 32767, 2147483647, 9223372036854775807),

    -- Test arrays with valid values
    (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 
    '{1,2,3}', '{100,200,300}', '{1000,2000,3000}', '{10.5,20.5,30.5}', '{20.5,30.5,40.5}', '{30.5,40.5,50.5}', '{1,2,3}', '{1,2,3}', '{1,2,3}', 
    0, 0, 0, 0, 0, 0, 0, 0, 0),

    -- Test multi-dimensional arrays
    (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 
    '{{1,2},{3,4}}', '{{100,200},{300,400}}', '{{1000,2000},{3000,4000}}', '{{10.5,20.5},{30.5,40.5}}', '{{20.5,30.5},{40.5,50.5}}', '{{30.5,40.5},{50.5,60.5}}', '{{1,2},{3,4}}', '{{1,2},{3,4}}', '{{1,2},{3,4}}', 
    0, 0, 0, 0, 0, 0, 0, 0, 0),

    -- Test nullable types with NULL values
    (NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 
    NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 
    0, 0, 0, 0, 0, 0, 0, 0, 0),

    -- Test mix of NULL and non-NULL values
    (1, NULL, 1000, NULL, 20.5, NULL, 1, NULL, 1, 
    '{1,2,3}', NULL, '{1000,2000,3000}', NULL, '{20.5,30.5,40.5}', NULL, '{1,2,3}', NULL, '{1,2,3}', 
    1, 0, 1000, 0, 20.5, 0, 1, 0, 1);