PAR = 0
RES = 0
for i in range(1,11):
    NUM = int(input("Digite  um número: "))
    RES = NUM % 2
    if RES == 0:
        print("É um valor par!")
        PAR = NUM + PAR
    else:
        print("É um valor impar!")
    RES = 0

print(f"A soma dos valores pares digitados é: {PAR}")