# Faça um programa que capture o nome do usuário, altura em metros, idade e imprima esses dados na tela. #

nome = input(" Por favor, insira seu nome: ")
altura = float(input(" Por favor, insira sua altura: "))
idade = int(input(" Por favor, insira sua idade: "))
nota1 = int(input("Digite sua primeira nota: "))
nota2 = int(input("Digite sua segunda nota: "))
somaNotas = nota1 + nota2

mensagem = f"Olá, meu nome é {nome} , tenho {altura} de altura, tenho {idade} anos e a soma das minhas notas foi de: {somaNotas}. "

print(mensagem)

