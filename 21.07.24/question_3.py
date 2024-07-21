fibonacci = lambda n: n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)


fib_series = [fibonacci(i) for i in range(15)]

print(fib_series)
