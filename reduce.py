# reduce - reduzir iteraveis em um unico valor

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def funcReduce(acumulador, produto):
    print('acumulador', acumulador)
    print('Produto', produto)
    print()
    return acumulador + produto['preco']
    
    
# total = 0
# for p in produtos:
#     total += p['preco']
    
# print(total)

total = reduce(
    funcReduce,
    produtos,
    0
)
print('total é', total)