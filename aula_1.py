# print para escrever
print("hello World")

nada=''

nome=input("insira um nome ")
#input serve para receber o valor

while nome == nada:
#while serve para repetir enquanto há uma condição
    print("escreva um nome válido")
    nome=input("insira um nome ") 


idade=input("insira sua idade: ")

while idade == nada or idade == 0:
    print("escreva uma idade válida")
    idade=input("insira sua idade: ")

media=float(input("insira sua média: "))

while media == nada or media == 0:
    print("escreva uma média válida")
    media=float(input("insira sua média: "))

faltas=float(input("insira a quantidade de faltas: "))

while faltas == nada:
    print("insira um valor válido ou 0 caso não tenha faltas")
    faltas=input("insira a quantidade de faltas: ")

print("o nome escrito foi: {}".format(nome))
print(type(nome))
print("a idade escrita foi: {}".format(idade))
print(type(idade))
print("a média escrita foi: {}".format(media))
print(type(media))
print("a quantidade de faltas escrita foi: {}".format(faltas))
print(type(faltas))

if media >=7 and faltas <=5:
    print("de acordo com as informações, você foi aprovado")
else:
    print("de acordo com as informações, você foi reprovado")