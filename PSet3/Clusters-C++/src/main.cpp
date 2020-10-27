#include <cstddef>
#include <iostream>
#include <cstdlib>
#include <ctime>

#include "include/generator.h"
#include "include/timer.h"

#define LOG(x) std::cout << x << std::endl;


int main()
{
    /* LOG(percolate(100, 200, 0.6)) */
    /* const int size = 15; */
    /* const double prob = 0.55;               // The probability of a cell to be on (1) */
    /* srand(time(NULL)); */
    /* ptrMatrix grid = generate_grid(size, prob); */

    /* // Print grid before colorize */
    /* for (int i = 0; i < size; i++) */
    /* { */
    /*     for (int j = 0; j < size; j++) */
    /*     { */
    /*         std::cout << *grid[i][j] << ", "; */
    /*     } */
    /*     std::cout << std::endl; */
    /* } */

    /* std::cout << std::endl << std::endl; */

    /* /1* ptrMatrix c_grid = colorize(grid); *1/ */
    /* colorize(grid); */

    /* // Print colored grid */
    /* for (int i = 0; i < size; i++) */
    /* { */
    /*     for (int j = 0; j < size; j++) */
    /*     { */
    /*         std::cout << *grid[i][j] << ",\t"; */
    /*     } */
    /*     std::cout << std::endl; */
    /* } */

    /* LOG(is_percolated(grid)) */

    LOG("Percolating includes repeating the process 500 times")

    Timer t;

    PercMatrix perc_matrix(10, 0);
    LOG("Percolating for 10")
    for (double prob=0; prob < 1.0; prob += 0.05)
    {
        LOG(perc_matrix.percolate(500, prob))
    }

    LOG("Percolating for 100")
    for (double prob=0; prob < 1.0; prob += 0.05)
    {
        LOG(percolate(500, 100, prob))
    }

    LOG("Percolating for 200")
    for (double prob=0; prob < 1.0; prob += 0.05)
    {
        LOG(percolate(500, 200, prob))
    }

    std::cout << "Time elapsed: " << t.elapsed() << " seconds" << std::endl;



}
