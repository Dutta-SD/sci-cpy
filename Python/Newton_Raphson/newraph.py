# This file is also a independently runnable file in addition to being a module.
# You can run this file to test NewRaphAlgorithm function.

'''
This program demonstrates Newton Raphson Algorithm(NPA).
It is advised to follow all rules of the algorithm while entering the input.
(Either read rules provided in README.md or search online)
Program will cause an error in case any of the algorithm rules are not obeyed.

Simply import NewRaphAlgorithm function in any program to use this algorithm to find roots of a math function.

This program has a dependency on SymPy library. Sympy is basically used here to convert math function in string form
into a solvable function and to differentiate that function.

NewRaphAlgorithm function accepts only a string as the math function, a float as root nearpoint 
and an integer as no. of decimal places of approximation (Any float provided will be converted to a whole number).

Some non-algorithmic rules particular to ths module are:
         
    1- There should always be a '*' sign between any number and variable or brackets.
       For Example: 'x^2-4x-7' is not allowed. Write it as 'x^2-4*x-7'.
                    Also, '4(x+2)' is not allowed. Write it as '4*(x+2)'

    2- Multiple alphabets together are considered as one variable.
       For Example: '2*kite' is considered same as '2*x'.
       
NOTE- ITS NOT THAT I AM 100% SURE THAT THIS PROGRAM IS COMPLETELY BUG FREE, BUT I HAVE FIXED A PRETTY GOOD CHUNK OF THEM. 
BUT IF STILL A BUG IS FOUND THAT MEANS I DIDN'T ENCOUNTER THAT BUG IN MY TESTING. I TESTED THIS PROGRAM WITH OVER A 100 POLYNOMIALS.'''

# Importing SymPy library functions
from sympy import sympify, diff

# Creating a custom error for this program. This helps the user to pinpoint the exact problem
class New_Raph_Error(Exception):          
    pass

# Defining a function for Newton Raphson Algorithm (NRA).
# This accepts a string as the math function, a float as root nearpoint, an integer as no. of decimal places of approximation.
def NewRaphAlgorithm(equation, nearpoint, decimal= 3):
    
    try:    #Checking invaild input
        decimal = abs(int(decimal))                                                   
    except (TypeError, ValueError):
        raise New_Raph_Error('Only whole numbers are accepted as decimal places')
    
    try:    #Checking invaild input
        nearpoint = float(nearpoint)
    except (TypeError, ValueError):
        raise New_Raph_Error('Only rational numbers are accepted as root nearpoint')
    
    try:    #Checking invaild input
        equation = str(equation)
        equation = sympify(equation)
    except:
        raise New_Raph_Error("Please use '*' between any number and variable or brackets.")
    
    try:    #Checking invaild input
        diff_equation = diff(equation)  #Differentiation of given equation
    except ValueError:
        raise New_Raph_Error('Newton Raphson Method can solve only one variable polynomials')
    
    try:    #Checking invaild input
        var = list(equation.free_symbols)[0]
    except IndexError:
        raise New_Raph_Error('A number has been entered instead of a equation')
    
            #Checking invaild input
    if float(diff_equation.subs(var, nearpoint)) == 0:
        raise New_Raph_Error('Root assumption provided is either on maxima or minima of the function')
    
    prev_np = None    #Declaring previous nearpoint for comparison with nearpoint in NRA
    
    
    
    # Looping through actual Algorithm
    x=0
    while x<1000 and prev_np != nearpoint and nearpoint != float('nan'):
        eq = float(equation.subs(var, nearpoint))            #Solving given function by substituting nearpoint
        diff_eq = float(diff_equation.subs(var, nearpoint))  #Solving differentiated function similarly
        prev_np = nearpoint
        try:
            nearpoint = nearpoint - (eq/diff_eq)    #Formula for NRA
        except ZeroDivisionError:
            return prev_np
        nearpoint = round(nearpoint, decimal)   #Rounding answer to the number of decimal places given
        x+=1
    
    
    
# Post Algorithm result validity checking
    if nearpoint == float('nan'):
        raise New_Raph_Error('''There is a local minima or maxima or a point of inflection around 
root assumption provided and nearest root value''')
    elif x==1000:
        raise New_Raph_Error('''Entered polynomial doesn't have any real root''')
    else:
        return nearpoint
    
    
#-------------------------------------------------NRA Module Ends Here--------------------------------------------------------
    





# The code following is a sample execution program for NRA.
# Anything folllowing will only execute if this file is run directly without importing.
if __name__ == '__main__':
    print('''This program demonstrates Newton Raphson Algorithm.
It is advised to follow all rules of the algorithm while entering the input.
Program will cause an error in case any of the algorithm rules are not obeyed.
          
There should always be a '*' sign between any number and variable.
E.g.- 'x^2-4x-7' is not allowed. Write it as 'x^2-4*x-7'.

Multiple alphabets together are considered as one variable.
E.g.- '2*kite' is considered same as '2*x'.\n''')
    
    equation = input('Enter a one variable polynomial: ')
    nearpoint = input('Enter value of a number close to a root: ')
    decimal = input('Enter the no. of decimal places for the appoximation of the root: ')
    print(f'\nOne of the roots of given function is: {NewRaphAlgorithm(equation, nearpoint, decimal)}')
    
# Created by Chaitanya Lakhchaura (aka ZenithFlux on github- https://github.com/ZenithFlux/)  