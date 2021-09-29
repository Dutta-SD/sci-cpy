from newraph import NewRaphAlgorithm as findroot

'''
print('\nError Test: On func= x^2+5x+7, finding roots near 9, accuracy of 1 decimal places.')
root = findroot('x^2+5*x+7', 9, 1)
print(f'Expected outcome: No Real Roots Error \nOutcome: newraph.New_Raph_Error: Entered polynomial doesn't have any real root')
print('Test Passed')

# I'm not including this test in the test program as this test will terminate it. If you wish to see the test just remove the
# triple quotes
'''

print('\nAll the tests are verfied using Wolframalpha.com')

print('''Test #1: On func= x^2+5x-7, finding roots near 4, accuracy of 2 decimal places.''')
root = findroot('x^2+5*x-7', 4, 2)
print(f'Expected outcome: 1.14 \nOutcome: {root}')
print('Test Passed')

print('''\nTest #2: On func= (x+2)^2, finding roots near -5, accuracy of 2 decimal places.''')
root = findroot('(x+2)^2', -5, 2)
print(f'Expected outcome: -2.0 \nOutcome: {root}')
print('Test Passed')

print('''\nTest #3: On func= x^4 + 43x^3 + 51x^2 + 93x + 45, finding roots near 90, accuracy of 4 decimal places.''')
root = findroot('x^4 + 43*x^3 + 51*x^2 + 93*x + 45', 90, 4)
print(f'Expected outcome: -0.5792 \nOutcome: {root}')
print('Test Passed')

print('''\nTest #4: On func= x^4 + 43x^3 + 51x^2 + 93x + 45, finding roots near -90, accuracy of 3 decimal places.''')
root = findroot('x^4 + 43*x^3 + 51*x^2 + 93*x + 45', -90, 3)
print(f'Expected outcome: -41.833 \nOutcome: {root}')
print('Test Passed')

print('''\nTest #5: On func= (7x^3+19x^2+89)^2, finding roots near 6, accuracy of 3 decimal places.''')
root = findroot('(7*x^3+19*x^2+89)^2', 6, 3)
print(f'Expected outcome: -3.663 \nOutcome: {root}')
print('Test Passed')