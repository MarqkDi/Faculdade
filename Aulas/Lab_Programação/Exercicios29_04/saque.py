valor = int(input("Digite o valor do saque: "))
notas = [50, 20, 10, 1]

for nota in notas:
    quantidade = valor // nota
    valor = valor % nota
    print(f"Notas de R${nota}: {quantidade}")