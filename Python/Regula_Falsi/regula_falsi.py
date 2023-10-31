# EPSILON is a very small quantity representing the maximun allowed error
EPSILON = 0.000001

# Equation to be solved is f(x)=0
# Modify the equation to be solved by changing f(x)
# f(x) returns the value of f(x) at a given value of x


def f(x):
    return (x*x-25)  # This is the function f(x), make modifications here

# Returns the root of the equation f(x)=0, if it can be calculated. Otherwise exits the program.


def RegulaFalsi(x1, x2):
    if (f(x1)*f(x2) > 0):
        print("Invalid choice of interval!")
        exit(0)
    elif (f(x1)*f(x2) == 0):
        if (f(x1) == 0):
            return x1
        if (f(x2) == 0):
            return x2
    while True:
        x0 = (x1*f(x2)-x2*f(x1))/(f(x2)-f(x1))
        if (f(x0) <= EPSILON and f(x0) >= (-EPSILON)):
            return x0
        if (f(x1)*f(x0) < 0):
            x2 = x0
        if (f(x2)*f(x0) < 0):
            x1 = x0


# Driver code to test the above functions
if __name__ == "__main__":
    x1, x2 = map(float, input(
        "Enter the left and right boundaries in order of the closed interval as mentioned above: ").split())
    print("A root of the equation is : ", RegulaFalsi(x1, x2))
