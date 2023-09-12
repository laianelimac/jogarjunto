from aula8ativ2 import times

matriculas = []

while len(matriculas) < 5:
    matricula = int(input("Digite o numero de sua matricula: "))
    matriculas.append(matricula)

    grupos = times(matricula)
    
    print(grupos)

