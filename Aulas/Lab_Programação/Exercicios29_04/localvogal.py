frase = input('Digite uma frase: ')
vogais = 0
for letra in frase:
    letra = letra.lower()
    if letra in 'aeiou':
        vogais += 1
print(f'Tinham {vogais} vogais na frase')