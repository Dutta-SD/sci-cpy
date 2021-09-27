from sympy import sympify, diff, Add, Mul

def NewRaphAlgorithm(equation, nearpoint, decimal= 3):
    equation = sympify(equation)
    diff_eq = diff(equation)
    var = list(equation.free_symbols)[0]
    prev_np = None
    while prev_np != nearpoint:
        eq = equation.subs(var, nearpoint)
        diff_eq = diff_eq.subs(var, nearpoint)
        prev_np = nearpoint
        nearpoint = Add(nearpoint, Mul(-1, (eq/diff_eq)))
        nearpoint = round(nearpoint, decimal)
    return nearpoint

if __name__ == '__main__':
    equation = input('Enter the equation: ')
    nearpoint = input('Enter value of a number near to a root: ')
    decimal = input('Enter the no. of decimal places for the appoximation of the root: ')
    print(NewRaphAlgorithm(equation, nearpoint, decimal))
    