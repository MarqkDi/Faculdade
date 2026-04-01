#Atividade Abud
#Data 1/04/26
NOTA1 = float(input("Digite a primeira nota do aluno: "))
NOTA2 = float(input("Digite a segunda nota do aluno: "))
NOTA3 = float(input("Digite a terceira nota do aluno: "))
if 0 > NOTA1 > 10 or 0 > NOTA2 > 10 or 0 > NOTA3 > 10:
    print("Número inválido")
else:
    MEDIA = (NOTA1 + NOTA2 + NOTA3) / 3
    if MEDIA >= 7:
        print(f"Média: {MEDIA:.2f} \nSituação: Aprovado")
    elif 5 <= MEDIA < 7:
        print(f"Média: {MEDIA:.2f} \nSituação: Recuperação")
    else:
        print(f"Média: {MEDIA:.2f} \nSituação: Reprovado")