def clasTriangulo (a):

    retangulo = False

    if ((a[0] + a[1]) > a[2]):
            if ((a[0] ** 2) + (a[1] ** 2)) == (a[2] ** 2):
                 retangulo = True
            if a[0] == a[1] == a[2]: return 'Equilátero', retangulo
            elif (a[0] == a[1]) or (a[0] == a[2]) or (a[1] == a[2]): return 'Isóceles', retangulo
            else: return 'Escaleno', retangulo
    
    elif (a[0] + a[1]) == a[2]: return 'Equilatero', False
    else: return None, False