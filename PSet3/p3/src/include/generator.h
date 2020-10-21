#include <vector>
#include <random>
#include <iostream>
#include <stdlib.h>
#include <time.h>

typedef std::vector< std::vector<int> > Matrix;
typedef std::vector<int> Row;

static bool gen_rand(double prob)
{
    const double max = 4096.0;

    // using random
    /* std::default_random_engine generator; */
    /* std::uniform_real_distribution<double> dist(0.0, max); */
    /* double my_rand = (dist(generator) / 4096.0); */

    /* std::cout << my_rand << std::endl; */

    srand(time(NULL));
    double my_rand = ((int)rand() % 4096) / max;
    if (my_rand < prob)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}


static Matrix generate_grid(int size)
{
    /* const std::size_t L = 100;               // Size of the matrix */
    Matrix matrix;                          // the grid to be generated
    double prob = 0.59;                      // The probability of a cell to be on (1)

    for(int i = 0; i < size; i++)
    {
        Row row(size);

        for(int j = 0; j < size; j++)
        {
            row[j] = gen_rand(prob);
        }

        matrix.push_back(row);
    }
    return matrix;
}


static Matrix colorize(const Matrix matrix)
{
    return matrix;
}
