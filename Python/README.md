 # I-Newton Raphson Rule

- This program demonstrates Newton Raphson Algorithm(NRA).
It is advised to follow all rules of the algorithm while entering the input.
Program will cause an error in case any of the algorithm rules are not obeyed.

- This program has a dependency on **SymPy** library. Sympy is basically used here to convert math function in string form
into a solvable function and to differentiate that function.

- ***newraph.py*** file is also a independently runnable file in addition to being a module. You can run this file to test NewRaphAlgorithm function.



## Newton Raphson Algorithm Rules

- The Newton-Raphson method (also known as Newton's method) is a way to quickly find a good approximation for the root of a real-valued function.

- Newton Raphson Method can solve only one variable function.

- Newton's method may not work if there are points of inflection, local maxima or minima around nearpoint taken or the root. In a situation like this, it will help to get an even closer starting point, where these critical points will not interfere.

4- Near point taken should be closer to the root you need than to any other root (if the function has multiple roots).
## Source
- [wolfram](https://mathworld.wolfram.com/SimpsonsRule.html)<br>
- [math24.net](https://math24.net/simpsons-rule.html)

 # II-Runge Kutta  Algorithm

- Runge–Kutta method is an effective and widely used method for solving the initial-value problems of differential equations. Runge–Kutta method can be used to construct high order accurate numerical method by functions' self without needing the high order derivatives of functions.
 


- ***RK4.py*** file is also a independently runnable file. You can run this file to test  Runge Kutta function.


## Runge Kutta  Algorithm Rules
#

- A method of numerically integrating ordinary differential equations by using a trial step at the midpoint of an interval to cancel out lower-order error terms.

- The method is a fourth-order method, meaning that the local truncation error is on the order of O(h5), while the total accumulated error is order O(h4)


## Source
- [wolfram](https://mathworld.wolfram.com/Runge-KuttaMethod.html)<br>
- [geekforgeeks](https://www.geeksforgeeks.org/runge-kutta-4th-order-method-solve-differential-equation/)
- [web.mit.edu](https://web.mit.edu/10.001/Web/Course_Notes/Differential_Equations_Notes/node5.html)


 # III-Simpson’s Rule Algorithm

- Simpson's Rule is a numerical method that approximates the value of a definite integral by using quadratic functions.Simpson's Rule is based on the fact that given three points, we can find the equation of a quadratic through those points 
 

- This program has a dependency on **SymPy** library. Sympy is basically used here to convert math function in string form
into a solvable function and to differentiate that function.

- ***simpsonsRule.py*** file is also a independently runnable file in addition to being a module. You can run this file to test simpsonsRule function.


## Simpson’s  Algorithm Rules
#

- The Simpson’s method approximation for definite integral of inputted expression

- Simpson's 1/3 Rule of approximation for defininite integrals
Takes three parameters: string expression, a - lower bound, b - upper bound


## Source
- [wolfram](https://mathworld.wolfram.com/SimpsonsRule.html)<br>
- [math24.net](https://math24.net/simpsons-rule.html)