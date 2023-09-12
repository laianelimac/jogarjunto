from Aula8verifica import verifica_cep

estados_norte_nordeste = ["AC", "AP", "AM", "PA", "RO", "RR", "TO", "AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]

cep = int(input("Informe o cep: "))

estado = verifica_cep(cep)
estado.lower()
verificador = False


for uf in estados_norte_nordeste:
    if estado in uf:
        verificador = True

if verificador == True:
    print(f"O estado de {estado} é elegível para frete")
else:
    print(f"O estado de {estado} não é elegível para frete")