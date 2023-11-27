'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, crie uma função lambda que aceite um número e retorne o cubo desse número
'''

# def cube(num):
#     return num ** 3

cube = lambda num: num ** 3

num = int(input("Enter the number: "))
print(f"The cube of {num} is {cube(num)}")