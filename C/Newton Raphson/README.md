
Newton Raphson Method

->Newton Raphson Method is a numerical method to approximate the root of a polynomial.

->Newton Raphson Method is an open method of root finding which means that it needs a single initial guess to reach the solution instead of narrowing down two initial guesses.

Suppose you need to find the root of a continuous, differentiable function f(x), and you know the root you are looking for is near the point x = x0. Then Newton's method tells us that a better approximation for the root is

             x1=x0-f(x0)/f'(x0)

This process may be repeated as many times as necessary to get the desired accuracy. In general, for any x-value x(n), the next value is given by

             x(n+1)=x(n)-f(xn)/f'(xn)    

Steps

1.Initial guess.

2.Using the formula mentioned above calculate the next value of x0.

3.Check if x is the root of the function or is in the range of affoardable error. In other words check if f(x0)=0 or |f(x0)| < affordable error. Repeat step 2 if not. If the formula mentioned above gives the same result, x0 is the root of the polynomial.

Example:

Equation to be solved is 

    f(x)=x*x-25.
    
f(x) gives the value of f(x) at a given value of x.

    f'(x)=2*x.
    
f'(x) gives the value of first order derivative of f(x) with respect to the variable x at a given value of x.

Now, by following the above metioned steps we get the root of the equation as x0=5.
