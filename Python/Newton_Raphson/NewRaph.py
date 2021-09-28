from sympy import sympify, diff

class New_Raph_Error(Exception):
    pass

def NewRaphAlgorithm(equation, nearpoint, decimal= 3):
    try:
        decimal=int(decimal)
    except (TypeError, ValueError):
        raise New_Raph_Error('Only whole numbers are accepted as decimal places')
    
    try:
        nearpoint=float(nearpoint)
    except (TypeError, ValueError):
        raise New_Raph_Error('Only rational numbers are accepted as root nearpoint')
    
    try:
        equation = str(equation)
        equation = sympify(equation)
    except:
        raise New_Raph_Error("Please use '*' between any number and variable or brackets.")
    
    try:
        diff_equation = diff(equation)
    except ValueError:
        raise New_Raph_Error('Newton Raphson Method can solve only one variable polynomials')
    
    try:
        var = list(equation.free_symbols)[0]
    except IndexError:
        raise New_Raph_Error('A number has been entered instead of a equation')
    
    
    if float(diff_equation.subs(var, nearpoint)) == 0:
        raise New_Raph_Error('Root assumption provided is either on maxima or minima of the function')
    
    prev_np = None
    
    x=0
    while x<50 and prev_np != nearpoint and nearpoint != float('nan'):
        eq = float(equation.subs(var, nearpoint))
        diff_eq = float(diff_equation.subs(var, nearpoint))
        prev_np = nearpoint
        try:
            nearpoint = nearpoint - (eq/diff_eq)
        except ZeroDivisionError:
            return prev_np
        nearpoint = round(nearpoint, decimal)
        x+=1
    
    if nearpoint == float('nan'):
        raise New_Raph_Error('''There is a local minima or maxima or a point of inflection between 
root assumption provided and nearest root value''')
    elif x==50:
        raise New_Raph_Error("Entered polynomial doesn't have any real root")
    else:
        return nearpoint
    

if __name__ == '__main__':
    print('''This program demonstrates Newton Raphson Algorithm.
It is advised to follow all rules of the algorithm while entering the input.
Program will cause an error in case any of the algorithm rules are not obeyed.
          
There should always be a '*' sign between any number and variable.
E.g.- 'x^2-4x-7' is not allowed. Write it as 'x^2-4*x-7'.

Multiple alphabets together are considered as one variable.
E.g.- '2kite' is considered same as '2x'.\n''')
    
    equation = input('Enter a one variable polynomial: ')
    nearpoint = input('Enter value of a number close to a root: ')
    decimal = input('Enter the no. of decimal places for the appoximation of the root: ')
    print(NewRaphAlgorithm(equation, nearpoint, decimal))  