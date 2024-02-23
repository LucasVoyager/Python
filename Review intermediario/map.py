#  map - mapear dados

from functools import partial
from types import GeneratorType


def printIter(iterator):
    print(*list(iterator), sep='\n')
    print()
    

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def increasePer(valor, porcentagem):
    return round(valor*porcentagem, 2)


aumentarDezPorcento = partial(
    increasePer,
    porcentagem= 1.1
)

# novosProdutos = [
#     {**p, 
#      'preco': aumentarDezPorcento(p['preco'])}
#     for p in produtos
# ]

def mudaPrecoProdutos(produto):
    return{**produto, 
              'preco': aumentarDezPorcento(
                  produto['preco']
                )
            }

novosProdutos = map(
    mudaPrecoProdutos,
    produtos
)

NovosProdutosGen = (x for x in produtos)
printIter(produtos)
printIter(novosProdutos)
print(hasattr(novosProdutos, '__iter__'))
print(hasattr(novosProdutos, '__next__'))
print(isinstance(NovosProdutosGen, GeneratorType))

print(list(map(
    lambda x: x**3,
        [1,2,3,4]
    ))
)