'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, crie dois conjuntos, cada um contendo 5 nomes de seus amigos.
Alguns nomes devem estra presentes em ambos os conjuntos. Use um método para encontrar quais nomes
aparecem em ambos os conjuntos e imprima o resultado
'''

friends = {"Micael", "Paty", "Leia", "Vivi", "Pedro"}
best_friends = {"Japa", "Isa", "Leia", "Vivi", "Helena"}

match = friends.intersection(best_friends)
print(match)


   