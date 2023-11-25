'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, crie uma lista com os nomes de três cidades.
Peça ao usuário para digitar o nome de uma cidade. Se a cidade estiver na lista,
imprima 'A cidade está na lista de cidades'. Se a cidade não estiver na tupla, 
imprima 'A cidade não está na lista de cidades."

Obs.: Você não pode utilizar list[]
'''

cities = ('São Paulo', 'Rio de Janeiro', 'Salvador')
city = input("Enter the name of the city:")

if city in cities:
    print("The city is on the list of cities")
else:
    print("The city is not in the list of cities")




   


   