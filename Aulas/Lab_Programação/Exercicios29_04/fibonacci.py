fim = int(input('Digite um valor: '))
a, b, c = 0, 0, 1
for i in range(fim):
    a = a + b
    print(a)
    b = c
    c = a