def fatorial(numero): 
    if numero < 0:
        return "Fatorial de números negativos não exite!"
    elif numero == 0:
        return 1
    else:
        f = 1
        for i in range(1, numero + 1):
            f *= i
        return fatorial