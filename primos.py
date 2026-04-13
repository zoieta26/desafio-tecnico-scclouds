def p_linear(n):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("n deve ser um inteiro maior que 1")
    primos = []
    for num in range (2, n + 1):
        for i in range(2, int(num**0.5) + 1 ):
            if num % i == 0:
                break
        else:
            primos.append(num)
    return primos

def p_recursivo(n, atual=2):
    if not isinstance(n, int) or n <= 1:
        raise ValueError("n deve ser um inteiro maior que 1")
    if atual > n:
        return []
    def eh_primo(num, divisor = 2):
        if num  < 2:
            return False
        if divisor > int(num**0.5):
            return True
        if num % divisor == 0:
            return False
        return eh_primo(num, divisor + 1)
    
    resto_da_lista = p_recursivo(n, atual + 1)
    if eh_primo(atual):
        return [atual] + resto_da_lista
    return resto_da_lista
