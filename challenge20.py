'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, crie uma lista de números de 1 a 10. Use um 'for loop' para
iterar sobre a lista. Se o número atual da iteração for par, imprima 'O número[número] é par'.
Se o número for ímpar, imprima 'O númerp[número] é ímpar'."
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print(f"The number{number} is even")
    else:
        print(f"The number{number} is odd")




   


   