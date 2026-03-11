IDADE = int(input("Digite sua idade: "))
PESO = float(input("Insira seu peso (kg): "))
ALTURA = float(input("Insira sua altura (m): "))
GENERO = str(input("Insira seu gênero (H/M): ".upper()))

ALTURACM = ALTURA * 100
ALTURAPOL = ALTURACM / 2.54
IMC = PESO / (ALTURA * ALTURA)
TMBH = 66.5 + (13.75 * PESO) + (5.003 * ALTURACM) - (6.75 * IDADE)
TMBM = 655.1 + (9.563 * PESO) + (1.850 * ALTURACM) - (4.676 * IDADE)
IDEALBRH = ALTURACM - 100
IDEALBRM = ALTURACM - 105
IDEALDEVH = 50 + 2.3 * (ALTURAPOL - 60)
IDEALDEVM = 45.5 + 2.3 * (ALTURAPOL - 60)
IDEALROBH = 52 + 1.9 * (ALTURAPOL - 60)
IDEALROBM = 49 + 1.7 * (ALTURAPOL - 60)

print(f"Seu IMC é: {IMC:.2f}".replace('.', ','))
if IMC < 18.5:
    print("Você está abaixo do peso! Procure um nutricionista.")
elif 18.5 <= IMC < 24.9:
    print("Você está no peso ideal! Continue assim.")
else:
    print("Você está acima do peso! Procure um nutricionista.")

if GENERO == "M":
    print (f"Sua Taxa Metabólica Basal é: {TMBM:.2f}")
    print (f"Seu Peso Ideal segundo a fórmula de Broca é: {IDEALBRM:.2f}")
    print (f"Seu Peso Ideal segundo a fórmula de Devine é: {IDEALDEVM:.2f}")
    print (f"Seu Peso Ideal segundo a fórmula de Robinson é: {IDEALROBM:.2f}")
else:
    print (f"Sua Taxa Metabólica Basal é: {TMBH:.2f}")
    print (f"Seu Peso Ideal segundo a fórmula de Broca é: {IDEALBRH:.2f}")
    print (f"Seu Peso Ideal segundo a fórmula de Devine é: {IDEALDEVH:.2f}")
    print (f"Seu Peso Ideal segundo a fórmula de Robinson é: {IDEALROBH:.2f}")
