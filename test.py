def do_something(n):
    lambda_ = (lambda f: (lambda x: f(lambda *a: x(x)(*a)))(lambda x: f(lambda *a: x(x)(*a))))
    
    F = lambda f: lambda n: 1 if n < 2 else n * f(n - 1)
    fact = lambda_(F)
    
    print(fact(n))
    
do_something(6)
