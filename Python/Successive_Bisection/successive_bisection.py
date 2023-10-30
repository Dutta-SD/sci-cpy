# EPSILON is a very small quantity representing the maximun allowed error
EPSILON = 0.000001

# Equation to be solved is f(x)=0
# Modify the equation to be solved by changing f(x)
# f(x) returns the value of f(x) at a given value of x


def f(x):
    return (x*x-25)  # This is the function f(x), make modifications here

# Returns the root of the equation f(x)=0, if it can be calculated. Otherwise exits the program.


def SuccessiveBisection(x1, x2):
    if (f(x1)*f(x2) > 0):
        print("Invalid choice of interval!")
        exit(0)
    elif (f(x1)*f(x2) == 0):
        if (f(x1) == 0):
            return x1
        if (f(x2) == 0):
            return x2

    while ((x2-x1) > EPSILON or (x2-x1) < (-EPSILON)):
        x0 = (x1+x2)/2
        if (f(x0) == 0):
            return x0
        if (f(x1)*f(x0) < 0):
            x2 = x0
        if (f(x2)*f(x0) < 0):
            x1 = x0

    return (x1+x2)/2


# Driver code to test the above functions
if __name__ == "__main__":
    x1, x2 = map(float, input(
        "Enter the left and right boundaries in order of the closed interval as mentioned above: ").split())

    print("\n\t***SOLUTION OF EQUATIONS BY SUCCESSIVE BISECTION METHOD***")
    print("\n\nINSTRUCTIONS:\nEquation to be solved is denoted by f(x)=0\nThe equation to be solved can be modified by changing the following function in the source code : f(x) \n\nInput : The left and right boundaries of a closed interval such that the values of f(x) at the boundary points are opposite in sign\nOutput : A solution for the equation if possible. If a solution can not be calculated, the program exits.")
    print("A root of the equation is : ", SuccessiveBisection(x1, x2))
