#Atividade Abud
#Data 1/04/26 
import random
GUESS = 0
LEVEL = 0
TRIES = 0
while 1 > LEVEL > 3:
    LEVEL = int(input("Escolha o nível: \n1- Fácil (1 a 10)\n2- Médio (1 a 50)\n 3- Difícil (1 a 100)"))
    if 1 > LEVEL > 3:
        print("Level inválido")
if LEVEL == 1:
    NRAN = random.randint(1, 10)
    while GUESS != NRAN:
        GUESS = int(input("Tente adivinhar o número: "))
        if GUESS == NRAN:
            print("Você acertou!")
        if GUESS > NRAN:
            print("Chute alto")
        else:
            print("Chute baixo")
        TRIES += 1
    print(f"Em {TRIES} tentativas")
if LEVEL == 2:
    NRAN = random.randint(1, 50)
    while GUESS != NRAN:
        GUESS = int(input("Tente adivinhar o número: "))
        if GUESS == NRAN:
            print("Você acertou!")
        if GUESS > NRAN:
            print("Chute alto")
        else:
            print("Chute baixo")
        TRIES += 1
    print(f"Em {TRIES} tentativas")
if LEVEL == 3:
    NRAN = random.randint(1, 100)
    while GUESS != NRAN:
        GUESS = int(input("Tente adivinhar o número: "))
        if GUESS == NRAN:
            print("Você acertou!")
        if GUESS > NRAN:
            print("Chute alto")
        else:
            print("Chute baixo")
        TRIES += 1
    print(f"Em {TRIES} tentativas")