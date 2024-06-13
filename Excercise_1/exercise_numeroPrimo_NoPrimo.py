# Escriba una función que dio un número diga si el número es primo o no es primo.
def num_primo(n):
    for d in range(2, n):
        if n % d == 0:
            print('No es primo')
            return False
    print('Es primo')
    return True

num_primo(12)