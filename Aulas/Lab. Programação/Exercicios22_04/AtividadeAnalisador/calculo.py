def natureza(a):
    if a > 0: return 'Positiva'
    elif a < 0: return 'Negativa'
    else: return 'Neutra'

def par(a):
    if a % 2 == 0: return 'Par'
    else: return 'Ímpar'

def multiplo(a):
    mult3 = False
    mult5 = False
    mult7 = False

    if a % 3 == 0: 
        mult3 = True
    if a % 5 == 0: 
        mult5 = True
    if a % 7 == 0: 
        mult7 = True
    
    return mult3, mult5, mult7