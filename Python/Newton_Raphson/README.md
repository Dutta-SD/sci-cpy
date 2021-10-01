# Newton Raphson Algorithm

This program demonstrates Newton Raphson Algorithm(NPA).
It is advised to follow all rules of the algorithm while entering the input.
Program will cause an error in case any of the algorithm rules are not obeyed.

This program has a dependency on **SymPy** library. Sympy is basically used here to convert math function in string form
into a solvable function and to differentiate that function.

***newraph.py*** file is also a independently runnable file in addition to being a module. You can run this file to test NewRaphAlgorithm function.

## Newton Raphson Algorithm Rules

1- The Newton-Raphson method (also known as Newton's method) is a way to quickly find a good approximation for the root of a real-valued function.

2- Newton Raphson Method can solve only one variable function.

3- Newton's method may not work if there are points of inflection, local maxima or minima around nearpoint taken or the root. In a situation like this, it will help to get an even closer starting point, where these critical points will not interfere.

4- Near point taken should be closer to the root you need than to any other root (if the function has multiple roots).

#### Source - [Brilliant.org](https://brilliant.org/wiki/newton-raphson-method/#:~:text=The%20Newton%2DRaphson%20method%20(also,straight%20line%20tangent%20to%20it.)

## Python *'NewRaphAlgorithm'* function rules:

1- There should always be a '\*' sign between any number and variable or brackets.
       For Example: 'x^2-4x-7' is not allowed. Write it as 'x^2-4\*x-7'.
                    Also, '4(x+2)' is not allowed. Write it as '4\*(x+2)'

2- Multiple alphabets together are considered as one variable.
       For Example: '2\*kite' is considered same as '2\*x'.

3- NewRaphAlgorithm function accepts only a string as the math function, a float as root nearpoint 
and an integer as no. of decimal places of approximation (Any float provided will be converted to a whole number).

4- Violation of any rule will cause a New_Raph_Error followed by description of the error.

## How to use this Program as a Module in other Programs:

Just write this on top of the code

    from newraph import NewRaphAlgorithm
As demonstrated in ***tests.py*** file.

       
### **NOTE:-**

ITS NOT THAT I AM 100% SURE THAT THIS PROGRAM IS COMPLETELY BUG FREE, BUT I HAVE FIXED A PRETTY GOOD CHUNK OF THEM. BUT IF STILL A BUG IS FOUND THAT MEANS 
I DIDN'T ENCOUNTER THAT BUG IN MY TESTING. I TESTED THIS PROGRAM WITH OVER A 100 POLYNOMIALS.


***Created by Chaitanya Lakhchaura (aka ZenithFlux on github- https://github.com/ZenithFlux/)***  