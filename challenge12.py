'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, crie uma lista de frutas e vegetais. 
Use um for loop aninhado(Nested for loop) para imprimir todas as 
combinações possíveis de frutas e vegetais, com fruta primeiro e
o vegetal em segundo.
'''
fruits = ['maça', 'pera', 'morango', 'mamao']
vegetables = ['batata', 'cenoura', 'chuchu', 'abobrinha']

for fruit in fruits:
    for vegetable in vegetables:
        print(fruit, vegetable)
