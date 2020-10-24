#include <iostream>
#include "include/generator.h"
#include <cstdlib>
#include <ctime>

#define LOG(x) std::cout << x << std::endl;

int main()
{
    const int size = 15;
    const double prob = 0.59;               // The probability of a cell to be on (1)
    srand(time(NULL));
    ptrMatrix grid = generate_grid(size, prob);
    /* colorize(grid); */

    // Print grid
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            std::cout << *grid[i][j] << ", ";
        }
        std::cout << std::endl;
    }


    /* for (int i = 0; i < 50; i++) */
    /* { */
    /*     std::cout << gen_rand(0.5) << std::endl; */
    /* } */
    std::cin.get();
}
