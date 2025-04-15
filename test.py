lambda_ = (lambda f: (lambda x: f(lambda *a: x(x)(*a)))(lambda x: f(lambda *a: x(x)(*a))))

F = lambda f: lambda n: 1 if n < 2 else n * f(n - 1)
out = lambda_(F)

print(out(6))
