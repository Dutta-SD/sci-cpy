from sympy import *


#Simpson's 1/3 Rule of approximation for defininite integrals
#str_expr - string input expression (e.g. "x**2 + 3*x - 1/2")
#a - lower bound of definite integral
#b - upper bound of definite integral
def simpsonsRule(str_expr, a, b):
    x = symbols("x")
    fcn = sympify(str_expr)
    delta_x = (b - a) / 6
    fcn_a = fcn.subs(x, a)
    fcn_b = fcn.subs(x, b)
    fcn_ab = fcn.subs(x, (a + b) / 2) * 4
    return str(delta_x * (fcn_a + fcn_ab + fcn_b))


str_expr = input("Enter an expression: ")
a = float(input("Enter a lower bound: "))
b = float(input("Enter a upper bound: "))
print("Approximate Integral: " + simpsonsRule(str_expr, a, b))