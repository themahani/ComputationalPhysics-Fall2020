#pragma  once

#include <cmath>
#include <cstddef>
#include <memory>
#include <vector>
#include <iostream>
#include <stdlib.h>
#include <ctime>
#include <unordered_map>

// The matrix type we will use
typedef std::vector< std::vector< std::shared_ptr<int> > > ptrMatrix;
typedef std::vector< std::shared_ptr<int> > ptrRow;


static bool gen_rand(double prob)
{
    const double max = 4096.0;

    // using rand
    return ((rand() % 4096) / max < prob);
}

class PercMatrix
{
    public:
        std::vector<ptrMatrix> ptr_cube;
        double percSize;
        int percColor;
        double prob;



    public:
    PercMatrix(int size, double prob)
        : percSize(0), percColor(0), prob(prob)
    {
        srand(time(0));
        for (int i = 0; i < size; i++)
        {
            ptrMatrix ptr_matrix(size);
            for (int j = 0; j < size; j++)
            {
                ptrRow ptr_row(size);
                for (int k = 0; k < size; k++)
                {
                    ptr_row[k] = std::make_shared<int>(gen_rand(prob));
                }
                ptr_matrix.push_back(ptr_row);
            }
            ptr_cube.push_back(ptr_matrix);
        }
    }


    void printMatrix() const
    {
        const size_t L = ptr_cube.size();

        for (size_t i=0; i < L; i++)
        {
            for (size_t j=0; j < L; j++)
            {
                for (size_t k=0; k < L; k++)
                {
                    std::cout << *ptr_cube[i][j][k] << ",\t";
                }
                std::cout << std::endl;
            }
            std::cout << std::endl;
        }
    }


    void reset_matrix(double probab)
    {
        prob = probab;
        percSize = 0;
        srand(time(0));
        size_t L = ptr_cube.size();
        for (size_t i=0; i< L; i++)
        {
            for (size_t j=0; j< L; j++)
            {
                for (size_t k = 0; k < L; k++)
                {
                    ptr_cube[i][j][k] = std::make_shared<int>(gen_rand(prob));
                }
            }
        }
    }


    void find_cluster(size_t i, size_t j, size_t k, std::vector<int> &front)
    {
        const bool is_on = (*ptr_cube[i][j][k] != 0);

        // if at the left, no need to look left
        if (j == 0 && is_on)
        {
            if (*ptr_cube[i - 1][j][k] != 0)
            {
                // Same cluster so same color
                ptr_cube[i][j][k] = ptr_cube[i - 1][j][k];
            }
            else
            {
                // New cluster
                front.push_back(front[front.size() - 1] + 1);
                ptr_cube[i][j][k] = std::make_shared<int>(front[front.size() - 1]);
            }
        }
        else if (is_on)
        {
            // Now look both up and left
            const bool left_on = (*ptr_cube[i][j - 1][k] != 0);
            const bool up_on = (*ptr_cube[i - 1][j][k] != 0);
            const bool back_on = (*ptr_cube[i][j][k - 1] != 0);
            // If cluster around...
            if (up_on || left_on || back_on)
            {
                /* std::shared_ptr<int> i_left = std::make_shared<int>(*ptr_matrix[i][j - 1]); */
                /* std::shared_ptr<int> i_up = std::make_shared<int>(*ptr_matrix[i - 1][j]); */
                std::shared_ptr<int> i_left = ptr_cube[i][j - 1][k];
                std::shared_ptr<int> i_up = ptr_cube[i - 1][j][k];
                std::shared_ptr<int> i_back = ptr_cube[i][j][k - 1];

                /* int* i_up = ptr_matrix[i - 1][j]; */

                if (up_on && left_on && back_on)
                {
                    // The min is the cluster to get
                    if (*i_back < *i_left && *i_back< *i_up)
                        ptr_cube[i][j][k] = i_back;
                    else if (*i_left < *i_back && *i_left < *i_up)
                        ptr_cube[i][j][k] = i_left;
                    else
                        ptr_cube[i][j][k] = i_up;


                    // marge the three clusters
                    *i_left = std::min(*i_back, std::min(*i_left, *i_up));
                    *i_back = std::min(*i_back, std::min(*i_left, *i_up));
                    *i_up = std::min(*i_back, std::min(*i_left, *i_up));
                }
                else
                {
                    // one of them is zero
                    ptr_cube[i][j][k] = (*i_left != 0 ? i_left : i_up);
                }
            }
            else        //If No prev clusters around...
            {
                // New cluster
                front.push_back(front[front.size() - 1] + 1);
                ptr_cube[i][j][k] = std::make_shared<int>(front[front.size() - 1]);
            }
        }
    }


    void colorize()
    {
        const size_t L = ptr_cube.size();     // ptr_matrix size
        // Make the color codes
        std::vector<int> frontier;
        frontier.reserve(L * L);
        for (size_t i = 0; i < L * L; i++)
        {
            frontier.push_back(i + 1);
        }
        // Make the cluster initializer surface
        ptrMatrix init;

        for (size_t i = 0; i < L; i++)
        {
            ptrRow ptr_row(L);
            for (size_t i = 0; i < L; i++)
            {
                ptr_row.push_back(std::make_shared<int>(frontier[i]));
            }
            init.push_back(ptr_row);
        }
        ptr_cube.insert(ptr_cube.begin(), init);

        for (size_t i = 1; i < L+1; i++)             // Loop over the surfaces, ignore init in index 0
        {
            for (size_t j = 0; j < L; j++)         // Loop over rows
            {
                for (size_t k = 0; k < L; k++)      // Loop over cells
                {
                    find_cluster(i, j, k, frontier);
                }
            }
        }
        ptr_cube.erase(ptr_cube.begin());       // Delete init after finished coloring the cube

    }


    bool is_percolated()
    {
        const size_t L = ptr_cube.size();

        for (size_t i = 0; i < L; i++)
        {
            for (size_t j = 0; j < L; j++)
            {
                if (*ptr_cube[ptr_cube.size() - 1][i][j] > 0 && *ptr_cube[ptr_cube.size() - 1][i][j] < L*L + 1)
                {
                    percColor = *ptr_cube[ptr_cube.size() - 1][i][j];
                    return 1;
                }
            }
        }
        return 0;
    }


    void percolate(const size_t times, const double prob)
    {
        // Initialize counter
        double sum = 0.0;
        size_t counter = 0;
        double perc_prob = 0.0;
        // Loop for <times> times and record the frequency of percolation
        for (size_t i=0; i< times; i++)
        {
            reset_matrix(prob);         // Recreate the random 1/0 state
            colorize();                 // Colorize
            if (is_percolated())
            {
                counter++;
                // Loop to get the percSize
                for (size_t i=0; i < ptr_cube.size(); i++)
                {
                    for (size_t j=0; j < ptr_cube.size(); j++)
                    {
                        for (size_t k = 0; k < ptr_cube.size(); k++)
                        {
                            if (*ptr_cube[i][j][k] == percColor)
                                percSize++;
                        }
                    }
                }
                sum += percSize / (ptr_cube.size() * ptr_cube.size());
            }
        }
        std::cout << "It percolates " << counter << " times." << std::endl;
        std::cout << "The mean perc prob for cell prob " << prob << " is: " << sum / times << std::endl;
    }


    bool not_percCluster(int color)
    {
        std::vector<int> percColors;
        const size_t L = ptr_cube.size();
        for (size_t i = 0; i < L; i++)
        {
            for (size_t j = 0; j < L; j++)
            {
                if (*ptr_cube[L - 1][i][j] > 0 && *ptr_cube[L - 1][i][j] <= L)
                {
                    percColors.push_back(*ptr_cube[L -1][i][j]);
                }
            }
        }
        for (size_t i = 0; i < percColors.size(); i++)
        {
            if (color == percColors[i])
                return 0;                   // It's a percolating cluster
        }
        return 1;                           // Not percolating cluster
    }


    double findNextGyro()
    {
        const size_t L = ptr_cube.size();
        // Color [key], size [value]
        std::unordered_map<int, int> clusterSizes;

        int maxSize = 0;
        int maxColor = 0;
        // Loop over the entire matrix.
        for (size_t i = 0; i < L; i++)
        {
            for (size_t j = 0; j < L; j++)
            {
                for (size_t k = 0; k < L; k++)
                {
                    // Ignore the Infinite cluster
                    if (not_percCluster(*ptr_cube[i][j][k]) &&
                            *ptr_cube[i][j][k] != 0)
                    {
                        // Update cluster sizes
                        if (clusterSizes.find(*ptr_cube[i][j][k]) != clusterSizes.end())
                        {
                            clusterSizes[*ptr_cube[i][j][k]] += 1;
                        }
                        else
                        {
                            clusterSizes[*ptr_cube[i][j][k]] = 1;
                        }
                        // update max cluster color code
                        if (clusterSizes[*ptr_cube[i][j][k]] > maxSize)
                        {
                            maxColor = *ptr_cube[i][j][k];
                            maxSize = clusterSizes[*ptr_cube[i][j][k]];
                        }
                    }
                }
            }
        }
        /* std::cout << "Max size is " << maxSize << " for color " << maxColor << std::endl; */
        if (maxColor == 0)
           return 0;

        // get coords of maxColor cluster
        std::vector< std::vector<int> > maxCoords;

        // Loop over matrix to find coords
        for (size_t i = 0; i < L; i++)
        {
            for (size_t j = 0; j < L; j++)
            {
                for (size_t k = 0; k < L; j++)
                {
                    if (*ptr_cube[i][j][k] == maxColor)
                    {
                        std::vector<int> xyz;
                        xyz.push_back(i);
                        xyz.push_back(j);
                        xyz.push_back(k);
                        maxCoords.push_back(xyz);
                    }
                }
            }
        }

        // Find center for cluster
        double mean_i = 0;
        double mean_j = 0;
        double mean_k = 0;
        for (int i = 0; i < maxCoords.size(); i++)
        {
            mean_i += maxCoords[i][0];
            mean_j += maxCoords[i][1];
            mean_k += maxCoords[i][2];
        }
        mean_i /= (double)maxCoords.size();
        mean_j /= (double)maxCoords.size();
        mean_k /= (double)maxCoords.size();
        /* std::cout << mean_i << ", " << mean_j << std::endl; */

        // Find the gyro radius
        double gyro = 0;
        for (int i = 0; i < maxCoords.size(); i++)
        {
            // sum the distance squared
            gyro += std::pow(maxCoords[i][0] - mean_i, 2) + std::pow(maxCoords[i][1] - mean_j, 2) + std::pow(maxCoords[i][2] - mean_k, 2);
        }
        gyro /= (double)maxCoords.size();           // divide by size
        gyro = std::pow(gyro, 0.5);

        /* std::cout << "Gyro is: " << gyro << std::endl; */
        return gyro;
    }

};
