def descontos(a, b):

    if (a >= 2000) and (b == 'Vip'):
        desconto = a * (40 / 100)
        return desconto

    elif a >= 1000:
        if b == 'Vip':
            desconto = a * (25 / 100)
            return desconto
        elif b == 'Funcionário':
            desconto = a * (30 / 100)
            return desconto
        else:
            desconto = a * (20 / 100)
            return desconto
    
    elif a >= 500:
        if b == 'Vip':
            desconto = a * (15 / 100)
            return desconto
        elif b == 'Funcionário':
            desconto = a * (20 / 100)
            return desconto
        else:
            desconto = a * (10 / 100)
            return desconto
    
    elif a < 500:
        if (a < 200) and (b == 'Funcionário'):
            return 0
        elif b == 'Vip':
            desconto = a * (10 / 100)
            return desconto
        elif b == 'Funcionário':
            desconto = a * (15 / 100)
            return desconto
        else:
            desconto = a * (5 / 100)
            return desconto