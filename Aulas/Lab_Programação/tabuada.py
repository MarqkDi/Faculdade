#Atividade Abud
#Data 1/04/26
RES = 0
NUM = int(input("Digite um número pra descobrir a tabuada: "))
for i in range(1, 11):
    RES = NUM * i
    print(f"{NUM} x {i} = {RES}")
