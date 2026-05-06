# ANÁLISE DE DESEMPENHO DE VENDEDORES
 
print("=" * 45)
print("   SISTEMA DE ANÁLISE DE VENDEDORES")
print("=" * 45)
 
num_vendedores = int(input("Quantos vendedores serão analisados? "))
 
ranking = []
 
contador_vendedores = 0
while contador_vendedores < num_vendedores:
    print("\n" + "-" * 45)
    nome = input("Nome do vendedor: ")
    num_dias = int(input("Quantos dias serão analisados? "))
 
    total_geral = 0
    dias_excelentes = 0
    maior_dia = 0
    dia = 1
 
    while dia <= num_dias:
        print(f"\n  DIA {dia}")
        num_vendas = int(input("  Quantidade de vendas: "))
 
        total_dia = 0
 
        for i in range(1, num_vendas + 1):
            valor = float(input(f"  Digite o valor da venda {i}: R$ "))
            total_dia += valor
 
        if total_dia >= 5000:
            if num_vendas > 10:
                classificacao = "Excelente desempenho"
            else:
                if total_dia >= 8000:
                    classificacao = "Ótimo faturamento"
                else:
                    classificacao = "Bom desempenho"
        else:
            if total_dia >= 2000:
                if num_vendas >= 5:
                    classificacao = "Desempenho regular"
                else:
                    classificacao = "Poucas vendas"
            else:
                if total_dia == 0:
                    classificacao = "Nenhuma venda realizada"
                else:
                    classificacao = "Desempenho insuficiente"
 
        print(f"\n  Total do dia  : R$ {total_dia:.2f}")
        print(f"  Classificação : {classificacao}")
 
        total_geral += total_dia
 
        if classificacao == "Excelente desempenho":
            dias_excelentes += 1
 
        if total_dia > maior_dia:
            maior_dia = total_dia
 
        dia += 1
 
    media_diaria = total_geral / num_dias
 
    print(f"\n{'=' * 45}")
    print(f"  RELATÓRIO FINAL — {nome.upper()}")
    print(f"{'=' * 45}")
    print(f"  Total geral vendido          : R$ {total_geral:.2f}")
    print(f"  Média diária de vendas       : R$ {media_diaria:.2f}")
    print(f"  Dias com excelente desempenho: {dias_excelentes}")
    print(f"  Maior valor em um único dia  : R$ {maior_dia:.2f}")
 
    ranking.append([nome, total_geral])
 
    contador_vendedores += 1
 
if num_vendedores > 1:
    for i in range(len(ranking)):
        for j in range(i + 1, len(ranking)):
            if ranking[j][1] > ranking[i][1]:
                ranking[i], ranking[j] = ranking[j], ranking[i]
 
    print(f"\n{'=' * 45}")
    print("         RANKING FINAL DE VENDEDORES")
    print(f"{'=' * 45}")
    for pos in range(len(ranking)):
        print(f"  {pos + 1}. {ranking[pos][0]:<20} R$ {ranking[pos][1]:.2f}")
 
    print(f"\n  Melhor vendedor: {ranking[0][0]} com R$ {ranking[0][1]:.2f}")
 
print(f"\n{'=' * 45}")
print("  Programa encerrado.")