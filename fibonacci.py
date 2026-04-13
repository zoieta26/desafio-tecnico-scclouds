def fib_recursivo(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n dever ser um inteiro não negativo")
    if n <= 1:
        return n
    return fib_recursivo(n-1) + fib_recursivo(n - 2)

def fib_linear(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n dever ser um numero inteiro não negativo")
    if n <= 1:
        return n 
    a, b = 0, 1
    for _ in range(2, n + 1):
        a,b = b, a + b
    return b
