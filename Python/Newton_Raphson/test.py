from sympy import sympify, diff, Add, Mul

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
        raise New_Raph_Error("Please use '*' between any number and variable.")
    
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
    

equation = '5*x^2-9*x+5'
nearpoint = -999
decimal = 4
print(NewRaphAlgorithm(equation, nearpoint, decimal))
