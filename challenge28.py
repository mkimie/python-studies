'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, crie duas funções. A primeira deve aceitar um número
e retornar o dobro desse número. A segunda função deve aceitar um número e retornar
o quadrado desse número. Em seguida, chame a primeira função dentro da segunda para retornar
o quadrado do dobro de um número.
'''

def double(num):
    return  num * 2

def square(num):
    return double(num) ** 2

num = int(input("Enter the number: "))
result = square(num)

print(f"The square of double the {double(num)} is {result}")