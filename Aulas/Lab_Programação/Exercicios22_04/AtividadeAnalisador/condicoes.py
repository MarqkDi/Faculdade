def analise(mult3, mult5, mult7, parImp, natureza):
    if mult3 and mult5 and mult7: return 'Número Raro'
    elif mult3 and mult5 and not mult7: return 'FizzBuzz Especial'
    elif (natureza == 'Negativa') and (parImp == 'Par'): return 'Número negativo, Par problemático'
    else: return None