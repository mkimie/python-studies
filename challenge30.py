'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, crie uma função lambda que aceite dois números e retorne a multiplicação desses números.
'''

multiplication = lambda num1, num2: num1 * num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The The multiplication between the {num1} and {num2} is {multiplication(num1, num2)}")