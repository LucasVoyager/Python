lista = [
    {'nome': 'lucas', 'Sobrenome':'Barros'},
    {'nome': 'jonatan', 'sobrenome': 'eric'},    
]

lista.sort(key=lambda item:item['nome'])

for item in lista:
    print(item)

