DROP TABLE IF EXISTS strings;

CREATE TABLE strings (
    col0 charvar(255),
    col1 char(255),
    col2 bpchar,
    col3 text,
    col0_a charvar(255)[],
    col1_a char(255)[],
    col2_a bpchar[],
    col3_a text[],
    col0_nn charvar(255) NOT NULL,
    col1_nn char(255) NOT NULL,
    col2_nn bpchar NOT NULL,
    col3_nn text NOT NULL
);

INSERT INTO strings (
    col0, col1, col2, col3, 
    col0_a, col1_a, col2_a, col3_a, 
    col0_nn, col1_nn, col2_nn, col3_nn
) VALUES
    -- Test normal types with valid values
    ('valid varchar', 'valid char', 'valid bpchar', 'valid text', 
    NULL, NULL, NULL, NULL, 
    'valid varchar', 'valid char', 'valid bpchar', 'valid text'),

    -- Test normal types with boundary values
    ('a' || repeat('a', 254), 'b' || repeat('b', 254), 'c', 'd' || repeat('d', 1000), 
    NULL, NULL, NULL, NULL, 
    'a' || repeat('a', 254), 'b' || repeat('b', 254), 'c', 'd' || repeat('d', 1000)),

    -- Test arrays with valid values
    (NULL, NULL, NULL, NULL, 
    '{"valid varchar1", "valid varchar2"}', '{"valid char1", "valid char2"}', '{"valid bpchar1", "valid bpchar2"}', '{"valid text1", "valid text2"}', 
    'valid varchar', 'valid char', 'valid bpchar', 'valid text'),

    -- Test multi-dimensional arrays
    (NULL, NULL, NULL, NULL, 
    '{{"valid varchar1", "valid varchar2"}, {"valid varchar3", "valid varchar4"}}', '{{"valid char1", "valid char2"}, {"valid char3", "valid char4"}}', '{{"valid bpchar1", "valid bpchar2"}, {"valid bpchar3", "valid bpchar4"}}', '{{"valid text1", "valid text2"}, {"valid text3", "valid text4"}}', 
    'valid varchar', 'valid char', 'valid bpchar', 'valid text'),

    -- Test nullable types with NULL values
    (NULL, NULL, NULL, NULL, 
    NULL, NULL, NULL, NULL, 
    'valid varchar', 'valid char', 'valid bpchar', 'valid text'),

    -- Test mix of NULL and non-NULL values
    ('valid varchar', NULL, 'valid bpchar', NULL, 
    '{"valid varchar1", NULL}', '{"valid char1", NULL}', '{"valid bpchar1", NULL}', '{"valid text1", NULL}', 
    'valid varchar', 'valid char', 'valid bpchar', 'valid text');