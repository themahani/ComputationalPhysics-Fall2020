#include <cstddef>
#include <iostream>
#include <cstdlib>
#include <ctime>

#include "include/generator.h"
#include "include/timer.h"

#define LOG(x) std::cout << x << std::endl;


int main()
{

    LOG("Percolating includes repeating the process 100 times")

    Timer t;

    PercMatrix perc_matrix10(10, 0);
    LOG("Percolating for 10")
    for (double prob=0; prob < 1.0; prob += 0.05)
    {
        /* LOG(perc_matrix.percolate(500, prob)) */
        perc_matrix10.percolate(100, prob);
    }

    PercMatrix perc_matrix100(100, 0);
    LOG("Percolating for 100")
    for (double prob=0; prob < 1.0; prob += 0.05)
    {
        /* LOG(perc_matrix.percolate(500, prob)) */
        perc_matrix100.percolate(100, prob);
    }

    PercMatrix perc_matrix200(200, 0);
    LOG("Percolating for 200")
    for (double prob=0; prob < 1.0; prob += 0.05)
    {
        /* LOG(perc_matrix.percolate(500, prob)) */
        perc_matrix200.percolate(100, prob);
    }

    /* PercMatrix matrix(15, 0.5); */
    /* matrix.colorize(); */

    /* while(!matrix.is_percolated()) */
    /* { */
    /*     matrix.reset_matrix(0.5); */
    /*     matrix.colorize(); */
    /* } */
    /* matrix.printMatrix(); */

    std::cout << "Time elapsed: " << t.elapsed() << " seconds" << std::endl;



}
