linhas = int(input("Quantas linhas você quer? "))

for i in range(1, linhas + 1):
    espacos = " " * (linhas - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacos + asteriscos)