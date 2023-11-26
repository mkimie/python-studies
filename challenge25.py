'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Crie uma função que aceite dois números como entrada e retorne a soma desses números
'''

def sum(num1, num2):
    result = num1 + num2
    return result

num1 = int(input("Enter the number n1: "))
num2 = int(input("Enter the number n2: "))
result = str(sum(num1, num2))
print(f"The sum of the {num1} and {num2} is {result}")
