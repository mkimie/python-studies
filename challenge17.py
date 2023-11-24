'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, quero que você peça ao usuário que digite sua idade.
Se a idade for menor que 13, imprima "Você é uma criança".
Se a idade estiver entre 13 e 19, imprima "Você é um adolescente".
Se a idade fot 20 ou mais, imprima "Você é um adulto".
'''

age = int(input("How old are you? "))

if age < 13:
    print("You are a child.")
elif age >= 13 and age <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")


   


   