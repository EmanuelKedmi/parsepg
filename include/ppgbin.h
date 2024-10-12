#pragma once

#include <cinttypes>
#include <cstring>
#include <vector>
#include <variant>

#ifdef _WIN32
#ifdef PPGBIN_EXPORTS
#define PPGBIN_API __declspec(dllexport)
#else
#define PPGBIN_API __declspec(dllimport)
#endif // PPGBIN_EXPORTS
#else
#define PPGBIN_API
#endif // _WIN32

#ifdef __cplusplus

class PgBin;
class PgTuple;
class PgField;

class PPGBIN_API PgBin
{
public:
    enum Flags
    {
        FLAG_OIDS = 0b000000001000000,
    };

    PgBin(uint8_t *bytes, size_t size);

    bool check_flag(Flags flags);

private:
    size_t estimateTuplesLength(uint8_t *tuplesData, size_t size);

public:
private:
    uint8_t *bytes;
    size_t size;

    uint8_t signature[11];
    uint32_t flags;
    uint32_t headersLength;
    uint8_t *headersData = nullptr;

    std::vector<PgTuple> tuples;
};

using PgTypes = std::variant<int64_t, std::string, bool, uint8_t *, float, double, uint32_t>;
class PPGBIN_API PgTuple
{
public:
    PgTuple(uint8_t *bytes, size_t size);

    size_t get_size() const { return size; }

private:
    size_t size;
    std::vector<PgField> fields;
};

class PPGBIN_API PgField
{
public:
    PgField(uint8_t *bytes, int32_t size);

private:
    int64_t parse_int(uint8_t *bytes, size_t size);
    float parse_float(uint8_t *bytes, size_t size);
    double parse_double(uint8_t *bytes, size_t size);

private:
    PgTypes value;
};

extern "C"
{
#endif

    PPGBIN_API int add(int a, int b);

#ifdef __cplusplus
}
#endif