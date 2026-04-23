def listaTriangulo():
    while True:

        entrada = input('Digite os três valores separados por espaço: ')
        lista = entrada.split()
        if len(lista) != 3:
            print('Digite exatamente 3 valores!')
            continue

        listaFlo = []
        erro = False

        for item in lista:
            try:
                listaFlo.append(float(item))
            except ValueError:
                print('Digite apenas Números!')
                erro = True
                break
        
        if erro:
            continue
        
        listaFlo = sorted(listaFlo)
        return listaFlo