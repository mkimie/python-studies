'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, comece com a lista 'frutas' do desafio anterior.
Primeiro, remova a 'manga' da lista usando o método remove(). 
Depois, disso, remova o último item da lista usando o comando del.
Por fim, imprima a lista modificada na tela.
'''

fruits = ['maça', 'morango', 'manga', 'uva', 'abacaxi']
fruits.remove('manga')
del fruits[-1]

print(f"Fruits: {fruits}")