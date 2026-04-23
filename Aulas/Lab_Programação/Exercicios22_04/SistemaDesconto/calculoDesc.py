def descontos(a, b):

    if (a >= 2000) and (b == 'Vip'):
        desconto = a * 0.40
        return desconto

    elif a >= 1000:
        if b == 'Vip':
            desconto = a * 0.25
            return desconto
        elif b == 'Funcionário':
            desconto = a * 0.30
            return desconto
        else:
            desconto = a * 0.20
            return desconto
    
    elif a >= 500:
        if b == 'Vip':
            desconto = a * 0.15
            return desconto
        elif b == 'Funcionário':
            desconto = a * 0.20
            return desconto
        else:
            desconto = a * 0.10
            return desconto
    
    else:
        if (a < 200) and (b == 'Funcionário'):
            return 0
        elif b == 'Vip':
            desconto = a * 0.10
            return desconto
        elif b == 'Funcionário':
            desconto = a * 0.15
            return desconto
        else:
            desconto = a * 0.05
            return desconto