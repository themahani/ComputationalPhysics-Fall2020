#pragma  once

#include <memory>
#include <vector>
#include <iostream>
#include <stdlib.h>

// The matrix type we will use
typedef std::vector< std::vector< std::shared_ptr<int> > > ptrMatrix;
typedef std::vector< std::shared_ptr<int> > ptrRow;

// This one is just to initialize the ptrMatrix
typedef std::vector< std::vector<int> > Matrix;
typedef std::vector<int> Row;

static bool gen_rand(double prob)
{
    const double max = 4096.0;

    // using rand
    return ((rand() % 4096) / max < prob);
}


static ptrMatrix generate_grid(int size, double prob)
{
    /* Matrix matrix;                          // the grid to be generated */

    /* for(int i = 0; i < size; i++) */
    /* { */
    /*     Row row(size); */

    /*     for(int j = 0; j < size; j++) */
    /*     { */
    /*         row[j] = gen_rand(prob); */
    /*     } */

    /*     matrix.push_back(row); */
    /* } */

    ptrMatrix ptr_matrix;

    for (int i = 0; i < size; i++)
    {
        ptrRow ptr_row(size);
        for (int j = 0; j < size; j++)
        {
            ptr_row[j] = std::make_shared<int>();
            *ptr_row[j] = gen_rand(prob);
            /* ptr_row[j] = matrix[i][j] */
        }
        ptr_matrix.push_back(ptr_row);
    }
    return ptr_matrix;
}

static void find_cluster(ptrMatrix &matrix, size_t i, size_t j, std::vector<int> &front)
{
    const bool is_on = (*matrix[i][j] != 0);

    // if at the left, no need to look left
    if (j == 0 && is_on)
    {
        if (*matrix[i - 1][j] != 0)
        {
            // Same cluster so same color
            matrix[i][j] = matrix[i - 1][j];
        }
        else
        {
            // New cluster
            front.push_back(front[front.size() - 1] + 1);
            matrix[i][j] = std::make_shared<int>(front[front.size() - 1]);
        }
    }
    else if (is_on)
    {
        // Now look both up and left
        const bool left_on = (*matrix[i][j - 1] != 0);
        const bool up_on = (*matrix[i - 1][j] != 0);
        // If cluster around...
        if (up_on || left_on)
        {
            /* std::shared_ptr<int> i_left = std::make_shared<int>(*matrix[i][j - 1]); */
            /* std::shared_ptr<int> i_up = std::make_shared<int>(*matrix[i - 1][j]); */
            std::shared_ptr<int> i_left = matrix[i][j - 1];
            std::shared_ptr<int> i_up = matrix[i - 1][j];

            /* int* i_up = matrix[i - 1][j]; */

            if (up_on && left_on)
            {
                // The min is the cluster to get
                matrix[i][j] = (*i_left < *i_up ? i_left : i_up);

                // marge the two clusters
                *i_left = std::min(*i_left, *i_up);
                *i_up = std::min(*i_left, *i_up);
            }
            else
            {
                // one of them is zero
                matrix[i][j] = (*i_left != 0 ? i_left : i_up);
            }
        }
        else        //If No prev clusters around...
        {
            // New cluster
            front.push_back(front[front.size() - 1] + 1);
            matrix[i][j] = std::make_shared<int>(front[front.size() - 1]);
        }
    }
}


static ptrMatrix colorize(ptrMatrix matrix)
{
    const size_t L = matrix.size();     // Matrix size
    // Make the color codes
    std::vector<int> frontier;
    frontier.reserve(L);
    for (size_t i = 0; i < L; i++)
    {
        frontier.push_back(i + 1);
    }
    // Make the cluster initializer row
    ptrRow init;

    for (size_t i = 0; i < L; i++)
    {
        init.push_back(std::make_shared<int>(frontier[i]));
    }
    matrix.insert(matrix.begin(), init);

    for (size_t i = 1; i < L+1; i++)             // Loop over the rows, ignore init in index 0
    {
        for (size_t j = 0; j < L; j++)         // Loop over items in the row
        {
            find_cluster(matrix, i, j, frontier);
        }
    }

    return matrix;
}

static bool is_percolated(const ptrMatrix& matrix)
{
    const size_t L = matrix[0].size();

    for (size_t i = 0; i < L; i++)
        if (*matrix[matrix.size() - 1][i] > 0 && *matrix[matrix.size() - 1][i] < L)
            return 1;

    return 0;
}
