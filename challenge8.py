'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, comece com a lista 'frutas' do desafio anterior.
Primeiro, seu desafio é alterar o segundo elemento(índice 1) de 'banana' para 'morango'.
Depois disso, adicione a fruta 'abacaxi' ao final da lista.
Por fim, imprima a lista modificada na tela.
'''

fruits = ['maça', 'banana', 'manga', 'uva']
fruits[1] = 'morango'
fruits.append('abacaxi')

print(f"Last fruit: {fruits}")