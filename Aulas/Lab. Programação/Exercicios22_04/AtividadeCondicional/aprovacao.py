def calculoMedia(a, b):
    media = (a * 0.7 + b * 0.3)
    return media

def analiseSituacao(a, b, c):

    if (a >= 8) and (b >= 90):
        return 'Aprovado com Mérito!'
    elif (a >= 7) and (b >= 75):
        return 'Aprovado direto!'
    elif (a < 5) and (c >= 8):
        return 'Reprovado com bom desempenho em trabalho!'
    elif ((a > 5) and (a < 7)) or ((b > 60) and (b < 74)):
        return 'Recuperação!'
    else:
        return 'Reprovado!'