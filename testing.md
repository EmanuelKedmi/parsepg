# Testing

The library has a comprehensive suite of tests that cover the functionality of the code.  
These tests ensure that the code behaves as expected and meets the requirements.

## Numeric Types
### Test Cases
* Normal Types
    * Insert rows with valid values for each column type.
    * Insert rows with boundary values (e.g., maximum and minimum values for smallint, int, bigint).
* Arrays
    * Insert rows with valid arrays for each column type.
    * Insert rows with multi-dimensional arrays for each column type.
* Nullable Types
    * Insert rows with NULL values for nullable columns.
    * Insert rows with a mix of NULL and non-NULL values.

## Text Types
### Test Cases
* Normal Types
    * Insert rows with valid string values for each column type.
    * Insert rows with boundary values (e.g., maximum length for varchar(255) and char(255)).
* Arrays
    * Insert rows with valid arrays for each column type.
    * Insert rows with multi-dimensional arrays for each column type.
* Nullable Types
    * Insert rows with NULL values for nullable columns.
    * Insert rows with a mix of NULL and non-NULL values.

* Normal Types
    * Insert rows with valid date and time values for each column type.
    * Insert rows with boundary values (e.g., minimum and maximum dates).
* Arrays
    * Insert rows with valid arrays for each column type.
    * Insert rows with multi-dimensional arrays for each column type.
* Nullable Types
    * Insert rows with NULL values for nullable columns.
    * Insert rows with a mix of NULL and non-NULL values.
* Timezone Handling
    * Insert rows with different timezones to ensure proper serialization.