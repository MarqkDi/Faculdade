#Atividade Abud
#Data 1/04/26
VAL = int(input("Digite um valor pra verificar se é primo: "))
PRIM = True
if VAL < 2:
    PRIM = False

else:
    for i in range(2, VAL):
        if VAL % i == 0:
            PRIM = False
            break
if PRIM:
    print("Número primo!")
else:
    print("O número não é primo!")