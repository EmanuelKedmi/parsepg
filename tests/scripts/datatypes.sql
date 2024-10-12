-- Drop the table if it already exists
DROP TABLE IF EXISTS datatypes;

-- Create the table with the specified columns and data types
CREATE TABLE datatypes (
    col0 json,
    col1 jsonb,
    col2 bool,
    col3 bytea,
    col0_a json[],
    col1_a jsonb[],
    col2_a bool[],
    col3_a bytea[],
    col0_nn json not null,
    col1_nn jsonb not null,
    col2_nn bool not null,
    col3_nn bytea not null
);

-- Insert multiple rows with different test cases
INSERT INTO datatypes (
    col0, col1, col2, col3, col0_a, col1_a, col2_a, col3_a, col0_nn, col1_nn, col2_nn, col3_nn
) VALUES
    -- Row 1: Valid JSON and JSONB data
    ('{"key": "value"}', '{"key": "value"}', null, null, null, null, null, null, '{"key": "value"}', '{"key": "value"}', null, null),
    -- Row 2: Valid Boolean data
    (null, null, true, null, null, null, null, null, null, null, true, null),
    -- Row 3: Valid Binary data
    (null, null, null, decode('48656c6c6f20576f726c64', 'hex'), null, null, null, null, null, null, null, decode('48656c6c6f20576f726c64', 'hex')),
    -- Row 4: Valid JSON array data
    (null, null, null, null, ARRAY['{"key1": "value1"}', '{"key2": "value2"}'], null, null, null, '{"key": "value"}', null, null, null),
    -- Row 5: Valid JSONB array data
    (null, null, null, null, null, ARRAY['{"key1": "value1"}', '{"key2": "value2"}'], null, null, null, '{"key": "value"}', null, null),
    -- Row 6: Valid Boolean array data
    (null, null, null, null, null, null, ARRAY[true, false], null, null, null, true, null),
    -- Row 7: Valid Binary array data
    (null, null, null, null, null, null, null, ARRAY[decode('48656c6c6f', 'hex'), decode('576f726c64', 'hex')], null, null, null, decode('48656c6c6f20576f726c64', 'hex')),
    -- Row 8: Null values for nullable columns
    (null, null, null, null, null, null, null, null, null, null, null, null),
    -- Row 9: Special characters in JSON and JSONB data
    ('{"key": "value with special characters: !@#$%^&*()"}', '{"key": "value with special characters: !@#$%^&*()"}', null, null, null, null, null, null, '{"key": "value with special characters: !@#$%^&*()"}', '{"key": "value with special characters: !@#$%^&*()"}', null, null);