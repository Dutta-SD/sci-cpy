from sympy import *


def simpsonsRule(str_expr, a, b):
    """Simpson's 1/3 Rule of approximation for defininite integrals
    Takes three parameters: string expression, a - lower bound, b - upper bound
    Returns: approximation for definite integral of inputted expression"""
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