 # Gaussian Elimination

Sloves **Ax = b**

Input can be provided as a CSV with coefficients and solutions listed in the augmented matrix form [A b] or via the command line


To run example provided:

    python gaussian_elimination.py -equation_coefficients tests/test_data/coefficients.csv -n_unknowns 4


To run unit test:

    pytest tests/