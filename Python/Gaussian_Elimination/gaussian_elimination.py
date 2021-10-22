import argparse
import sys
import numpy as np
import csv

parser = argparse.ArgumentParser(
        description='sum the integers at the command line')
parser.add_argument(
    "-equation_coefficients",
    "--coeffs",
    required=False, 
    help='a csv file with coefficients of linear system to solve')
parser.add_argument(
    "-n_unknowns",
    "--n",
    required=False, 
    help='number of uknowns')


def gaussian_elimination(args):
    # promt user for input if none provided
    if not args.n:
        n = input("Number of unknowns: ")
        n = int(n)
    else:
        n = int(args.n)
    AugM = np.zeros((n,n+1))
    Soln = np.zeros(n)

    if not args.coeffs:
        print("Inputs needed for system in form Ax = B")
        for k in range(n):
            for j in range(n):
                AugM[k][j] = int(input(f"Enter coefficient for equation {k+1}, unknown {j+1}: "))
            AugM[k][n] = int(input(f"Enter solution for equation{k+1}: "))
        
    else:
        csv_file = args.coeffs
        with open(csv_file, newline='') as f:
            reader = csv.reader(f)
            for rdx, row in enumerate(reader):
                for idx, num in enumerate(row):
                    AugM[rdx][idx] = str(num)    

    
    # Gaussian Elimination
    for k in range(n-1):
        if AugM[k][k] == 0:
            # need to choose a non-zero pivot row
            for i in range(k+1, n):
                if AugM[i][k] != 0:
                    # permute row s i and k
                    temp = AugM[i].copy()
                    AugM[i] = AugM[k]
                    AugM[k] = temp
                    break
        
        # Continue to get zero entries below diagonal
        for i in range(k+1, n):
            factor = AugM[i][k]/AugM[k][k]
            AugM[i] = AugM[i] - factor*AugM[k]

    # Check for existence of a solution
    for k in range(n):
        if AugM[k][k] == 0:
            print("No unique solution!")
            return

    # Back substitution
    Soln[n-1] = AugM[n-1][n]/AugM[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum = np.matmul(AugM[i][i+1:n],Soln[i+1:])
        Soln[i] = (AugM[i][n] - sum)/AugM[i][i]


    print("Solution is : ", Soln)
    return Soln

if __name__== "__main__":
    
    args = parser.parse_args(sys.argv[1:])
    gaussian_elimination(args)