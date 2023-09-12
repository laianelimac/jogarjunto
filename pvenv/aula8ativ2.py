def times(matricula):
    numero = matricula
    
    if numero % 2 == 0:
        return "AZUL"

    else:
        return "AMARELO"

matricula = int(input("Digite a sua matricula: "))
grupo = times(matricula) 

if grupo == "AZUL":
    print("VOCÊ ESTÁ NO TIME AZUL")
else:
    print("VOCÊ ESTÁ NO TIME AMARELO ")    