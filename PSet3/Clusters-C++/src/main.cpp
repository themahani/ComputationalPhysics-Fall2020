#include <iostream>
#include "include/generator.h"

int main()
{
    const int size = 5;
    Matrix grid = generate_grid(size);
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            std::cout << grid[i][j] << " ";
        }
        std::cout << std::endl;
    }

    /* for (int i = 0; i < 50; i++) */
    /* { */
    /*     std::cout << gen_rand(0.5) << std::endl; */
    /* } */
    std::cin.get();
}
