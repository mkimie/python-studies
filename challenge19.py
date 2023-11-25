'''
Curso: Programação Python do Zero ao Avançado + 32 Projetos Reais
Instrutor: André Iacono

Desafio: Para este desafio, crie um loop que peça ao usuário para digitar o nome de uma fruta.
Se a fruta digitada não for 'abacate', o loop deve continuar pedindo ao usuário para digitar o nome de uma fruta.
Se a fruta for 'abacate', o loop deve terminar e o programa deve imprimir "Parabéns, você acertou a fruta!"
'''


fruit = ''
while fruit != 'abacate':
    fruit = input("Enter a fruit: ")
    if fruit.lower() == 'abacate':
        break
print("Congratulations, you got the fruit right!")




   


   