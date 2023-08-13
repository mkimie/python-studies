'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Neste desafio, quero que você crie um script que solicite ao usuário dois números.
Em seguida,seu script deve exibir a soma, a subtração, a multiplicação, a divisão(resultado decimal) e
a exponenciação(primeiro número elevado ao segundo) desses dois números.
'''

num1 = float(input("Enter the first number "))
num2 = float(input("Enter the second number "))

sum = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
exponentiation = num1**num2

print(f"Sum: {sum}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
print(f"Exponentiation: {exponentiation}")