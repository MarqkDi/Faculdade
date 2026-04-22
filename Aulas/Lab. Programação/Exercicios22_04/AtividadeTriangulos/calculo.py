def clasTriangulo (a):

    retangulo = False

    if ((a[0] + a[1]) > a[2]):
            if ((a[0] ** 2) + (a[1] ** 2)) == (a[2] ** 2):
                 retangulo = True
            if (a[0] == a[1]) and (a[0] == a[2]): return 'Equilátero', retangulo
            elif a[0] == a[1] == a[2]: return 'Isóceles', retangulo
            elif (a[0] != a[1]) and (a[0] != a[2]) and (a[1] != a[2]): return 'Escaleno', retangulo
    
    else:
        if (a[0] + a[1]) == a[2]: return True, False
        else: return None, False