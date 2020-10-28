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
        ptrMatrix ptr_matrix;
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
            ptrRow ptr_row(size);
            for (int j = 0; j < size; j++)
            {
                ptr_row[j] = std::make_shared<int>();
                *ptr_row[j] = gen_rand(prob);
                /* ptr_row[j] = matrix[i][j] */
            }
            ptr_matrix.push_back(ptr_row);
        }
    }


    void printMatrix() const
    {
        const size_t L = ptr_matrix.size();

        for (size_t i=0; i < L; i++)
        {
            for (size_t j=0; j < L; j++)
            {
                std::cout << *ptr_matrix[i][j] << ",\t";
            }
            std::cout << std::endl;
        }
    }


    void reset_matrix(double probab)
    {
        prob = probab;
        percSize = 0;
        for (int i=0; i< ptr_matrix.size(); i++)
        {
            for (int j=0; j< ptr_matrix.size(); j++)
            {
                ptr_matrix[i][j] = std::make_shared<int>(gen_rand(prob));
            }
        }
    }


    void find_cluster(size_t i, size_t j, std::vector<int> &front)
    {
        const bool is_on = (*ptr_matrix[i][j] != 0);

        // if at the left, no need to look left
        if (j == 0 && is_on)
        {
            if (*ptr_matrix[i - 1][j] != 0)
            {
                // Same cluster so same color
                ptr_matrix[i][j] = ptr_matrix[i - 1][j];
            }
            else
            {
                // New cluster
                front.push_back(front[front.size() - 1] + 1);
                ptr_matrix[i][j] = std::make_shared<int>(front[front.size() - 1]);
            }
        }
        else if (is_on)
        {
            // Now look both up and left
            const bool left_on = (*ptr_matrix[i][j - 1] != 0);
            const bool up_on = (*ptr_matrix[i - 1][j] != 0);
            // If cluster around...
            if (up_on || left_on)
            {
                /* std::shared_ptr<int> i_left = std::make_shared<int>(*ptr_matrix[i][j - 1]); */
                /* std::shared_ptr<int> i_up = std::make_shared<int>(*ptr_matrix[i - 1][j]); */
                std::shared_ptr<int> i_left = ptr_matrix[i][j - 1];
                std::shared_ptr<int> i_up = ptr_matrix[i - 1][j];

                /* int* i_up = ptr_matrix[i - 1][j]; */

                if (up_on && left_on)
                {
                    // The min is the cluster to get
                    ptr_matrix[i][j] = (*i_left < *i_up ? i_left : i_up);

                    // marge the two clusters
                    *i_left = std::min(*i_left, *i_up);
                    *i_up = std::min(*i_left, *i_up);
                }
                else
                {
                    // one of them is zero
                    ptr_matrix[i][j] = (*i_left != 0 ? i_left : i_up);
                }
            }
            else        //If No prev clusters around...
            {
                // New cluster
                front.push_back(front[front.size() - 1] + 1);
                ptr_matrix[i][j] = std::make_shared<int>(front[front.size() - 1]);
            }
        }
    }


    void colorize()
    {
        const size_t L = ptr_matrix.size();     // ptr_matrix size
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
        ptr_matrix.insert(ptr_matrix.begin(), init);

        for (size_t i = 1; i < L+1; i++)             // Loop over the rows, ignore init in index 0
        {
            for (size_t j = 0; j < L; j++)         // Loop over items in the row
            {
                find_cluster(i, j, frontier);
            }
        }
        ptr_matrix.erase(ptr_matrix.begin());

    }


    bool is_percolated()
    {
        const size_t L = ptr_matrix.size();

        for (size_t i = 0; i < L; i++)
            if (*ptr_matrix[ptr_matrix.size() - 1][i] > 0 && *ptr_matrix[ptr_matrix.size() - 1][i] < L)
            {
                percColor = *ptr_matrix[ptr_matrix.size() - 1][i];
                return 1;
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
                for (size_t i=0; i < ptr_matrix.size(); i++)
                {
                    for (size_t j=0; j < ptr_matrix.size(); j++)
                    {
                        if (*ptr_matrix[i][j] == percColor)
                            percSize++;
                    }
                }
                sum += percSize / (ptr_matrix.size() * ptr_matrix.size());
            }
        }
        std::cout << "It percolates " << counter << " times." << std::endl;
        std::cout << "The mean perc prob for cell prob " << prob << " is: " << sum / times << std::endl;
    }


    bool not_percCluster(int color)
    {
        std::vector<int> percColors;
        const size_t L = ptr_matrix.size();
        for (size_t i = 0; i < L; i++)
        {
            if (*ptr_matrix[L - 1][i] > 0 && *ptr_matrix[L - 1][i] <= L)
            {
                percColors.push_back(*ptr_matrix[L -1][i]);
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
        const size_t L = ptr_matrix.size();
        // Color [key], size [value]
        std::unordered_map<int, int> clusterSizes;

        int maxSize = 0;
        int maxColor = 0;
        // Loop over the entire matrix.
        for (size_t i = 0; i < L; i++)
        {
            for (size_t j = 0; j < L; j++)
            {
                // Ignore the Infinite cluster
                if (not_percCluster(*ptr_matrix[i][j]) &&
                        *ptr_matrix[i][j] != 0)
                {
                    // Update cluster sizes
                    if (clusterSizes.find(*ptr_matrix[i][j]) != clusterSizes.end())
                    {
                        clusterSizes[*ptr_matrix[i][j]] += 1;
                    }
                    else
                    {
                        clusterSizes[*ptr_matrix[i][j]] = 1;
                    }
                    // update max cluster color code
                    if (clusterSizes[*ptr_matrix[i][j]] > maxSize)
                    {
                        maxColor = *ptr_matrix[i][j];
                        maxSize = clusterSizes[*ptr_matrix[i][j]];
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
                if (*ptr_matrix[i][j] == maxColor)
                {
                    std::vector<int> xy;
                    xy.push_back(i);
                    xy.push_back(j);
                    maxCoords.push_back(xy);
                }
            }
        }

        // Find center for cluster
        double mean_i = 0;
        double mean_j = 0;
        for (int i = 0; i < maxCoords.size(); i++)
        {
            mean_i += maxCoords[i][0];
            mean_j += maxCoords[i][1];
        }
        mean_i /= (double)maxCoords.size();
        mean_j /= (double)maxCoords.size();
        /* std::cout << mean_i << ", " << mean_j << std::endl; */

        // Find the gyro radius
        double gyro = 0;
        for (int i = 0; i < maxCoords.size(); i++)
        {
            // sum the distance squared
            gyro += std::pow(maxCoords[i][0] - mean_i, 2) + std::pow(maxCoords[i][1] - mean_j, 2);
        }
        gyro /= (double)maxCoords.size();           // divide by size
        gyro = std::pow(gyro, 0.5);

        /* std::cout << "Gyro is: " << gyro << std::endl; */
        return gyro;
    }

};

static ptrMatrix generate_grid(int size, double prob)
{

    ptrMatrix ptr_matrix;

    for (int i = 0; i < size; i++)
    {
        ptrRow ptr_row(size);
        for (int j = 0; j < size; j++)
        {
            ptr_row[j] = std::make_shared<int>();
            *ptr_row[j] = gen_rand(prob);
            /* ptr_row[j] = ptr_matrix[i][j] */
        }
        ptr_matrix.push_back(ptr_row);
    }
    return ptr_matrix;
}


static void find_cluster(ptrMatrix &ptr_matrix, size_t i, size_t j, std::vector<int> &front)
{
    const bool is_on = (*ptr_matrix[i][j] != 0);

    // if at the left, no need to look left
    if (j == 0 && is_on)
    {
        if (*ptr_matrix[i - 1][j] != 0)
        {
            // Same cluster so same color
            ptr_matrix[i][j] = ptr_matrix[i - 1][j];
        }
        else
        {
            // New cluster
            front.push_back(front[front.size() - 1] + 1);
            ptr_matrix[i][j] = std::make_shared<int>(front[front.size() - 1]);
        }
    }
    else if (is_on)
    {
        // Now look both up and left
        const bool left_on = (*ptr_matrix[i][j - 1] != 0);
        const bool up_on = (*ptr_matrix[i - 1][j] != 0);
        // If cluster around...
        if (up_on || left_on)
        {
            /* std::shared_ptr<int> i_left = std::make_shared<int>(*ptr_matrix[i][j - 1]); */
            /* std::shared_ptr<int> i_up = std::make_shared<int>(*ptr_matrix[i - 1][j]); */
            std::shared_ptr<int> i_left = ptr_matrix[i][j - 1];
            std::shared_ptr<int> i_up = ptr_matrix[i - 1][j];

            /* int* i_up = ptr_matrix[i - 1][j]; */

            if (up_on && left_on)
            {
                // The min is the cluster to get
                ptr_matrix[i][j] = (*i_left < *i_up ? i_left : i_up);

                // marge the two clusters
                *i_left = std::min(*i_left, *i_up);
                *i_up = std::min(*i_left, *i_up);
            }
            else
            {
                // one of them is zero
                ptr_matrix[i][j] = (*i_left != 0 ? i_left : i_up);
            }
        }
        else        //If No prev clusters around...
        {
            // New cluster
            front.push_back(front[front.size() - 1] + 1);
            ptr_matrix[i][j] = std::make_shared<int>(front[front.size() - 1]);
        }
    }
}


static ptrMatrix colorize(ptrMatrix &ptr_matrix)
{
    const size_t L = ptr_matrix.size();     // ptr_matrix size
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
    ptr_matrix.insert(ptr_matrix.begin(), init);

    for (size_t i = 1; i < L+1; i++)             // Loop over the rows, ignore init in index 0
    {
        for (size_t j = 0; j < L; j++)         // Loop over items in the row
        {
            find_cluster(ptr_matrix, i, j, frontier);
        }
    }
    ptr_matrix.erase(ptr_matrix.begin());

    return ptr_matrix;
}


static bool is_percolated(const ptrMatrix& ptr_matrix)
{
    const size_t L = ptr_matrix[0].size();

    for (size_t i = 0; i < L; i++)
        if (*ptr_matrix[ptr_matrix.size() - 1][i] > 0 && *ptr_matrix[ptr_matrix.size() - 1][i] < L)
            return 1;

    return 0;
}


static size_t percolate(const size_t times, const size_t size, const double prob)
{
    // Initialize counter
    size_t counter = 0;
    // Loop for <times> times and record the frequency of percolation
    for (size_t i=0; i< times; i++)
    {
        ptrMatrix grid = generate_grid(size, prob);
        colorize(grid);
        if (is_percolated(grid))
            counter++;
    }

    return counter;
}
