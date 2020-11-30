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

    PercMatrix cube(10, 0.6);
    cube.colorize();


    std::cout << "Time elapsed: " << t.elapsed() << " seconds" << std::endl;



}
