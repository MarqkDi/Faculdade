print("-----Primeira Parte-----")
PROVA1P = float(input("Digite a nota da primeira prova: "))
TRABALHO1P = float(input("Digite a nota do primeiro trabalho: "))
PESO1P = int(input("Digite o peso da primeira parte: "))
PRIM_NOTA = PROVA1P + TRABALHO1P

print("-----Segunda Parte----")
PROVA2P = float(input("Digite a nota da primeira prova: "))
TRABALHO1_2P = float(input("Digite a nota do primeiro trabalho: "))
TRABALHO2_2P = float(input("Digite a nota do segundo trabalho: "))
PESO2P = int(input("Digite o peso da primeira parte: "))
SEG_NOTA = PROVA2P + TRABALHO1_2P + TRABALHO2_2P

MEDIA_POND = ((PRIM_NOTA * PESO1P) + (SEG_NOTA * PESO2P)) / (PESO1P + PESO2P)

print(f"Sua média ponderada é {MEDIA_POND}")