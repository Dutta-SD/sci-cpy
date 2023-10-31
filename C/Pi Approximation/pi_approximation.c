// FILEPATH: c:\Users\Soumya Prabha Maiti\Desktop\sci-cpy\Python\Pi_Approximation\file.c
#include <stdio.h>

int main()
{
    // Initialize denominator
    int k = 1;

    // Initialize sum
    double s = 0;

    for (int i = 0; i < 1000000; i++)
    {
        // even index elements are positive
        if (i % 2 == 0)
        {
            s += (4.0 / k);
        }
        else
        {
            // odd index elements are negative
            s -= (4.0 / k);
        }

        // denominator is odd
        k += 2;
    }

    printf("%lf", s);

    return 0;
}
