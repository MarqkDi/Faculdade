#Entrada com validação de escolha
'''
while True:
    print('1 - Comum \n2 - Vip \n3 - Funcionário')
    tipoCliente = int(input('Qual tipo de cliente você é?: '))
    if tipoCliente not in [1, 2, 3]:
        print('Opção inválida!')
        continue
    break
'''

#Entrada simples
print('1 - Comum \n2 - Vip \n3 - Funcionário')
tipoCliente = int(input('Qual tipo de cliente você é?: '))
valor = float(input('Digite o valor da compra: R$'))

if tipoCliente == 1:
    tipoCliente = 'Comum'
elif tipoCliente == 2:
    tipoCliente = 'Vip'
else:
    tipoCliente = 'Funcionário'

#Condições e cálculos de descontos
if (valor >= 2000) and (tipoCliente == 'Vip'):
    desconto = valor * 0.40

elif valor >= 1000:
    if tipoCliente == 'Vip':
        desconto = valor * 0.25

    elif tipoCliente == 'Funcionário':
        desconto = valor * 0.30
    else:
        desconto = valor * 0.20

elif valor >= 500:
    if tipoCliente == 'Vip':
        desconto = valor * 0.15
    elif tipoCliente == 'Funcionário':
        desconto = valor * 0.20
    else:
        desconto = valor * 0.10

else:
    if (valor < 200) and (tipoCliente == 'Funcionário'):
        desconto = 0
    elif tipoCliente == 'Vip':
        desconto = valor * 0.10
    elif tipoCliente == 'Funcionário':
        desconto = valor * 0.15
    else:
        desconto = valor * 0.05

#Saidas
print(f'{"Cartão de cliente":=^50}')
print(f'Tipo do cliente: {tipoCliente}')
print(f'Valor da compra: R${valor:.2f}')
print(f'Valor do desconto: R${desconto:.2f}')
print(f'Valor final com desconto: R${valor - desconto:.2f}')
print(f'{"=" * 50}')