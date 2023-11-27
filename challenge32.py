'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, crie uma função lambda que eleve um número ao quadrado.
Em seguida use essa função para calcular o quadrado de todos os números em uma lista usando loop for.
'''
numbers = range(1,11)
square = lambda num: num ** 2
results = []

for num in numbers:
    results.append(square(num))

print(f"The squares of numbers{numbers} are {results}")