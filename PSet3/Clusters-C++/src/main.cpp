#include <cstddef>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>

#include "include/generator.h"
#include "include/timer.h"

#define LOG(x) std::cout << x << std::endl;

void gyroRep(const size_t times, const int L)
{
    LOG("Size is: " << L)
        std::vector<double> meanGyros;
    for (double prob = 0; prob < 1.0; prob += 0.025)
    {
        LOG(prob)
            double meanGyro = 0;
        for (size_t rep = 0; rep < times; rep++)
        {
            PercMatrix matrix(L, prob);
            matrix.colorize();
            meanGyro += matrix.findNextGyro();
        }
        meanGyros.push_back(meanGyro / (double)times);
    }
    LOG("")
    for (int i = 0; i < 40; i++)
    {
        std::cout << meanGyros[i] << ",\t" << std::endl;
    }
    LOG("")
}

int main()
{


    Timer t;

    /* =========================================================
     * ==============   Problem 3 and 4     ====================
     * ========================================================= */

    /* LOG("Percolating includes repeating the process 100 times") */

    /* PercMatrix perc_matrix10(10, 0); */
    /* LOG("Percolating for 10") */
    /* for (double prob=0; prob < 1.0; prob += 0.05) */
    /* { */
    /*     /1* LOG(perc_matrix.percolate(500, prob)) *1/ */
    /*     perc_matrix10.percolate(100, prob); */
    /* } */

    /* PercMatrix perc_matrix100(100, 0); */
    /* LOG("Percolating for 100") */
    /* for (double prob=0; prob < 1.0; prob += 0.05) */
    /* { */
    /*     /1* LOG(perc_matrix.percolate(500, prob)) *1/ */
    /*     perc_matrix100.percolate(100, prob); */
    /* } */

    /* PercMatrix perc_matrix200(200, 0); */
    /* LOG("Percolating for 200") */
    /* for (double prob=0; prob < 1.0; prob += 0.05) */
    /* { */
    /*     /1* LOG(perc_matrix.percolate(500, prob)) *1/ */
    /*     perc_matrix200.percolate(100, prob); */
    /* } */

    /* ======================================================
     * ==================== Problem 5 =======================
     * ====================================================== */


    gyroRep(6000, 10);
    gyroRep(2000, 20);
    gyroRep(1000, 40);
    gyroRep(500, 80);
    gyroRep(100, 160);




    /* for (int L = 10; L < 161; L *= 2) */
    /* { */
    /*     LOG("Size is: " << L) */
    /*     std::vector<double> meanGyros; */
    /*     for (double prob = 0; prob < 1.0; prob += 0.025) */
    /*     { */
    /*         LOG(prob) */
    /*         double meanGyro = 0; */
    /*         for (int rep = 0; rep < 100; rep++) */
    /*         { */
    /*             PercMatrix matrix(L, prob); */
    /*             matrix.colorize(); */
    /*             meanGyro += matrix.findNextGyro(); */
    /*         } */
    /*         meanGyros.push_back(meanGyro / 100.0); */
    /*     } */
    /*     LOG("") */

    /*     for (int i = 0; i < 40; i++) */
    /*     { */
    /*         std::cout << meanGyros[i] << ",\t" << std::endl; */
    /*     } */
    /* } */


    std::cout << "Time elapsed: " << t.elapsed() << " seconds" << std::endl;

    // Test
    /* double prob = 0; */
    /* do */
    /* { */
    /*     std::cin >> prob; */
    /*     PercMatrix matrix(15, prob); */
    /*     matrix.printMatrix(); */
    /*     LOG("") */
    /*     matrix.colorize(); */
    /*     matrix.printMatrix(); */
    /*     LOG("") */
    /*     matrix.is_percolated(); */

    /*     LOG(matrix.percColor) */
    /*         LOG(matrix.findNextGyro()); */
    /* } */
    /* while(prob != 0); */


}
