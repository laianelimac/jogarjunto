verificaEmail = False
dominio = 'jogarjuntoinstituto.org'

while verificaEmail == False:
    email = input('Informe seu e-mail completo: ')

    if dominio in email:
        print(f'O e-mail {email} contém {dominio}')
    else:
        print(f'O e-mail {email} não contém {dominio}')
        verificaEmail == True        