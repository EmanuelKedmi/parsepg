#include <stdexcept>

#include "ppgbin.h"

PgBin::PgBin(uint8_t *bytes, size_t size)
{
    constexpr uint16_t MIN_SIZE = 13;
    constexpr uint32_t OIDS_FLAG = 0b0000;

    if (size < MIN_SIZE)
        return;

    std::memcpy(signature, bytes, sizeof(signature));

    flags = bytes[11];
    headersLength = (uint32_t) * (bytes + 11);

    uint8_t *tuplesData = bytes + 11 + headersLength;
    size_t estimatedTuplesLenght = estimateTuplesLength(tuplesData, tuplesData - bytes - 1);
    if (estimatedTuplesLenght == 0)
        return;

    tuples.reserve((size_t)ceilf(estimatedTuplesLenght * 0.8f));
    size_t tuplesSize = size - (tuplesData - bytes); // TODO: verify via debug
    while (tuplesData < (bytes + size - 1))
    {
        const auto &tuple = tuples.emplace_back(tuplesData, tuplesSize);
        tuplesData += tuple.get_size();
        tuplesSize -= tuple.get_size();
    }
}

bool PgBin::check_flag(Flags flags)
{
    return this->flags & flags;
}

size_t PgBin::estimateTuplesLength(uint8_t *tuplesData, size_t size)
{
    // super naive implementation, total size divided by first element size

    // 2 is field count (16bit) of first tuple
    if (size < 2)
        return 0;

    // start at 2 bytes for tuple's field count
    uint16_t fieldsCount = *(uint16_t *)tuplesData;
    uint8_t *fieldsData = tuplesData + 2;
    while (fieldsCount-- > 0)
    {
        uint32_t fieldSize = *(uint32_t *)(fieldsData);
        fieldsData += 4 + fieldSize;
    }

    return size / (fieldsData - tuplesData);
}

PgTuple::PgTuple(uint8_t *bytes, size_t size)
{
    if (size < 2)
    {
        throw std::runtime_error("Expected data but got none");
    }

    size_t fieldCount = *(uint16_t *)bytes;
    uint8_t *fieldsData = bytes + 2;
    while (fieldCount-- > 0)
    {
        int32_t fieldSize = *(int32_t *)fieldsData;
        fields.emplace_back(fieldsData + 4, fieldSize);
        fieldsData += 4 + fieldSize;
    }
}

PgField::PgField(uint8_t *bytes, int32_t size)
{
}

int add(int a, int b)
{
    return a + b;
}