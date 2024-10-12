#include <string>
#include <iostream>
#include <fstream>

#include "ppgbin.h"

int main()
{
    std::ifstream file("C:\\Users\\Emanu\\OneDrive\\Documents\\py-parse-pg-bin\\data.bin", std::ios::binary);
    // read all content to uint8_t buffer
    file.seekg(0, std::ios::end);
    size_t size = file.tellg();
    file.seekg(0, std::ios::beg);
    uint8_t *buffer = new uint8_t[size];
    file.read((char *)buffer, size);
    file.close();

    PgBin bin(buffer, size);

    return 0;
}