'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, quero que você crie um loop que imprima os números de 1 a 10,
mas pare de imprimir assim que chegar a 5 usando o comando 'break'. 
Em seguida, crie um segundo loop que imprima os números de 1 a 10, mas pule a impressão do número 5 usando o comando 'continue'.
'''


print('Loop com break: ')
for numero in range(1,11):
    print(numero)
    if numero == 5:
        break

print('\nLoop com continue: ')
for numero in range(1,11):
    if numero == 5 :
         continue
    print(numero)
   


   