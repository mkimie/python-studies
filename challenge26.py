'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Crie uma função que calcule a potência de um número.
A função deve aceitar dois argumentos: a base e o exponente.
No entanto, se o expoente não for fornecido ao chamar a função, ele
deve assumir o valor padrão 2
'''

def potentiation(base, exponent=2):
    result = base ** exponent
    return result

base = int(input("Enter the base: "))
exponent = input("Enter the exponent: ")

if exponent:
    result = str(potentiation(base, int(exponent)))
    print(f"The power of {base} raised to {exponent} is {result}")
else:
    result = str(potentiation(base))
    print(f"The power of {base} raised to {exponent} is {result}")