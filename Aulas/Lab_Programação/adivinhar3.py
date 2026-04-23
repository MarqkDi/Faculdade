import random

acerto = 0
ran1 = random.randint(0, 9)
ran2 = random.randint(0, 9)
ran3 = random.randint(0, 9)

while acerto != 3:
    acerto = 0
    dif = 0
    
    num1 = int(input("Digite o número da primeira casa: "))
    num2 = int(input("Digite o número da segunda casa: "))
    num3 = int(input("Digite o número da terceira casa: "))

    if num1 == ran1:
        acerto += 1
    if num2 == ran2:
        acerto += 1
    if num3 == ran3:
        acerto += 1

    if num1 != ran1 and (num1 == ran2 or num1 == ran3):
        dif += 1
    if num2 != ran2 and (num2 == ran3 or num2 == ran1):
        dif += 1
    if num3 != ran3 and (num3 == ran1 or num3 == ran2):
        dif += 1

    if acerto == 3:
        print("Você acertou! Os números sorteados eram: ", ran1, ran2, ran3)
    elif dif > 0 or acerto > 0:
        print(f"Você tem {dif} números em casas trocadas e {acerto} em casas corretas!")
    else:
        print("Você errou todos, tente novamente!")