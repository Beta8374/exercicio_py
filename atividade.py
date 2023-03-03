# print("vamos somar 2 valores")

# valor1 = int(input("Digite o primeiro valor "))
# valor2 = int(input("Agora digite o segundo valor "))

# soma = valor1 + valor2

# print("a soma entre {} e {} é {}".format(valor1, valor2, soma))

# from array import *
# print("Este programa tira a média aritmética")

# listNumb = input("Digite 3 números")
#   while listNumb:
#     listNumb = input("Digite 3 números")

print("Esse programa é um conversor de unidade")
metro = float(input("Digite um valor em metros: "))
kilom = metro/1000
hectom = metro/100
decam = metro/10
decin = metro * 10
cent = metro *100
mill = metro * 1000

print ('''{} metro, igual à 
{} kilometro 
{} hectometros 
{} decametros 
{} decimetros 
{} centimetros 
{} milimetros.'''.format(metro, kilom, hectom, decam, decin, cent, mill))