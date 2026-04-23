from entrada import coletarTipo, valCompra
from calculoDesc import descontos

tipo = coletarTipo()
valor = valCompra()
valDesconto = descontos(valor, tipo)

print(f'{"Cartão de cliente":=^50}')
print(f'Tipo do cliente: {tipo}')
print(f'Valor da compra: R${valor:.2f}')
print(f'Valor do desconto: R${valDesconto:.2f}')
print(f'Valor final com desconto: R${valor - valDesconto:.2f}')
print(f'{"=" * 50}')