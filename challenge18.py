'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, imagine que você tem uma loja de carros.
Crie uma lista com carros que vocÊ tem em estoque: BMW X6, BMW i5, BMW i8.
Peça ao usuário para que ele insira o nome do carro que deseja comprar.
Se o carro estiver em estoque, imprima "Este carro está disponível".
Se o carro não estiver em estoque, imprima "Desculpe, este carro não está disponível".
'''

cars = ["BMW X6", "BMW i5", "BMW i8"]
car = input("Enter the desired car: ")

if car in cars:
    print("This car is available.")
else:
    print("Sorry. This car is not available.")


   


   