NOME, SNOME = input("Digite seu nome e sobrenome: ").split(' ')
IDADE = int(input("Digite sua idade: "))
SAL = float(input("Digite o seu salário: "))
COD = int(input("Digite seu código de funcionário: "))

NOME = NOME.capitalize()
SNOME = SNOME.capitalize()
SAL = f"R${SAL}"
IDADE = f"{IDADE} anos"
COD = f"{COD:06d}"

resultado = "Resultado"
print(f"{'RESULTADO':=^30}")
print(f"Nome completo: {NOME} {SNOME}")
print(f"Idade: {IDADE: ^15}")
print(f"Salário: {SAL: ^15}")
print(f"Código: {COD: ^15}")
print('=' * 30)
