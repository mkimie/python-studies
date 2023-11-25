'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, crie uma lista com 5 nomes de países e as capitais desses países.
Peça ao uusário para digitar o nome de um país. Se o país estiver na lista, imprima 'A capital de [país] é [capital]'.
Se o país não estiver na lista imprima 'Desculpe, não temos informações sobre a capital desse país'.
'''

countries = {
        "Argentina": "Buenos Aires", 
        "Brasil": "Brasília", 
        "Japão": "Tóquio", 
        "Grécia": "Atenas", 
        "França": "Paris"
        }

country = input("Enter the name of the country:")


if country in countries:
    print(f"The capital of {country} is {countries[country]}")
else:
    print("Sorry, we don't have information about the capital of this country")


   


   