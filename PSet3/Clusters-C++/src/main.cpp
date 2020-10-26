#include <iostream>
#include <cstdlib>
#include <ctime>

#include "include/generator.h"

#define LOG(x) std::cout << x << std::endl;

int main()
{
    const int size = 15;
    const double prob = 0.45;               // The probability of a cell to be on (1)
    srand(time(NULL));
    ptrMatrix grid = generate_grid(size, prob);

    // Print grid before colorize
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            std::cout << *grid[i][j] << ", ";
        }
        std::cout << std::endl;
    }

    std::cout << std::endl << std::endl;

    /* ptrMatrix c_grid = colorize(grid); */
    colorize(grid);

    // Print colored grid
    for (int i = 1; i < size + 1; i++)
    {
        for (int j = 0; j < size; j++)
        {
            std::cout << *grid[i][j] << ",\t";
        }
        std::cout << std::endl;
    }

    LOG(is_percolated(grid))


    /* for (int i = 0; i < 50; i++) */
    /* { */
    /*     std::cout << gen_rand(0.5) << std::endl; */
    /* } */
    // std::cin.get();
}
