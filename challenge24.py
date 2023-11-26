'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Crie uma função que aceita um número como entrada e retorna o quadrado desse número.
'''

def numberASquared(num):
    result = num**2
    return result

number = int(input("Enter the number: "))
square = numberASquared(number)
print(f"The square of the {number} is {square}")
