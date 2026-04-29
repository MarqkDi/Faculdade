continuar = "s"
total = 0
soma_idades = 0
homens = 0
maiores = 0
menor_mulher = 0

while continuar == "s":
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()

    total += 1
    soma_idades += idade

    if sexo == "M":
        homens += 1

    if idade > 18:
        maiores += 1

    if sexo == "F":
        if menor_mulher == 0 or idade < menor_mulher:
            menor_mulher = idade

    continuar = input("Deseja cadastrar outra pessoa? (s/n): ")

if total > 0:
    media = soma_idades / total

    print(f"\nMédia de idade: {media:.1f}")
    print(f"Homens cadastrados: {homens}")
    print(f"Maiores de 18 anos: {maiores}")

    if menor_mulher > 0:
        print(f"Mulher mais jovem: {menor_mulher} anos")
    else:
        print("Nenhuma mulher cadastrada.")
else:
    print("Nenhuma pessoa cadastrada.")