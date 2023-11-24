'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, crie uma lista que inclui "maça" três vezes e outras frutas de sua escolha.
Use um loop for para contar quantas vezes "maça" aparece na lista e imprima o resultado.
'''

fruits = ["maça", "banana", "maça", "laranja", "maça", "pera"]
number_macas = 0

for fruit in fruits:
    if fruit == "maça":
        number_macas += 1
print(f"Número de maças na lista: {number_macas}")


   


   