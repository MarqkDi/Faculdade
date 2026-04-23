LEI_ANT = float(input("Digite a leitura anterior: "))
LEI_ATU = float(input("Digite a leitura atual: "))
VAL_KWH = float(input("Qual o valor do KW/h?: R$"))
PERC_ICMS = int(input("Digite o percentual (%) do ICMS: "))
PERC_ILUPU = int(input("Digite o percentual (%) de iluminação pública: "))
PERC_BANDTARIF = int(input("Digite o percentual (%) da bandeira tarifárica: "))

CONSU = LEI_ATU - LEI_ANT
VAL_BASE_CONTA = CONSU * VAL_KWH
VAL_BANDTARIFA = VAL_BASE_CONTA * (PERC_BANDTARIF / 100)
VAL_ICMS = VAL_BASE_CONTA * (PERC_ICMS / 100)
VAL_ILUPU = VAL_BASE_CONTA * (PERC_ILUPU / 100)
VAL_TOTAL = VAL_BASE_CONTA + VAL_BANDTARIFA + VAL_ICMS + VAL_ILUPU

print(f"O seu consumo foi de {CONSU:.2f}KW/h")
print(f"O valor base de sua conta é R${VAL_BASE_CONTA:.2f}".replace('.', ','))
print(f"O valor do ICMS é de R${VAL_ICMS:.2f}".replace('.', ','))
print(f"O valor da taxa de iluminação pública foi R${VAL_ILUPU:.2f}".replace('.', ','))
print(f"O valor da bandeira tarifárica é de R${VAL_BANDTARIFA:.2f}".replace('.', ','))
print(f"O valor total da sua conta é R${VAL_TOTAL:.2f}".replace('.', ','))