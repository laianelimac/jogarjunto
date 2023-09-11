import requests

squad ={
    "Priscila": "41192005",
    "Giovana": "03817070",
    "Mylena": "13142342",
    "Layane": "40285001"
}

for nome, cep in squad.items():
    

    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    data = response.json()
    cidade = data['localidade']
    print(f'{nome} mora em {cidade}')