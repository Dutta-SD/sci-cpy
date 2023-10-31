n = int(input("**** Lagrange's Method of Interpolation**** \n\n\nEnter the number of observations: "))
x = [0] * n
f = [0] * n
result = 0.0

for i in range(n):
	x[i], f[i] = map(float, input(f"Enter x{i+1} & f{i+1} : ").split())

X = float(input("Enter x for finding f(x): "))

for i in range(n):
	temp = 1.0
	for j in range(n):
		if j != i:
			temp *= (X - x[j]) / (x[i] - x[j])
	result += temp * f[i]

print(f"f({X}) = {result}")