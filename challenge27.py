'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: As funções recursivas são funções que se chamam dentro do seu próprio bloco de código.
Elas são úteis para resolver problemas que podem ser divididos em problemas menores e de natureza 
semelhante.

Um exemplo clássico de onde a recursão é usada pe o cálculo do fatorial de um número. O fatorial de um
número n é o produto de todos os números inteiros positivos de n até 1.
'''

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return  num * factorial(num-1)

num = int(input("Enter the number: "))

print(f"The factorial of {num} is {factorial(num)}")