'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, crie uma função lambda que aceite um número e retorne "Par" se o número for
par e "Ímpar" se o número for ímpar.
'''

even_or_odd = lambda num: "Even" if num % 2 == 0 else "Odd"

num = int(input("Enter the number: "))
print(f"The number {num} is {even_or_odd(num)}")