#include <iostream>
#include "include/generator.h"
#include <cstdlib>

#define LOG(x) std::cout << x << std::endl;

int main()
{
    const int size = 15;
    ptrMatrix grid = generate_grid(size);
    colorize(grid);
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            std::cout << *grid[i][j] << " ";
        }
        std::cout << std::endl;
    }


    /* for (int i = 0; i < 50; i++) */
    /* { */
    /*     std::cout << gen_rand(0.5) << std::endl; */
    /* } */
    std::cin.get();
}
