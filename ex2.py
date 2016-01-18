def fibonacci(n):
	x = 0
	y = 1
	z = 1
	for i in range(1, n + 1):
		x = y
		y = z
		z = x + y
	return x

i = 1
result = 0
fib = 1
while fib < 4000000:
	fib = fibonacci(i)
	result += fib if fib % 2 == 0 else 0
	i += 1

print result
