import json

pessoa = {
    'nome': 'lucas barros',
    'idade': 23,
    'altura': 1.81
}

with open('pessoaJson.json', 'w') as arquivo:
    json.dump(pessoa, arquivo)

