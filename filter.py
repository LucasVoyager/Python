#  filter é um filtro funcional

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

# novosProdutos = [
#     p for p in produtos
#     if p['preco'] > 100
# ]

novosProdutos = filter(
    lambda p: p['preco'] > 10,
    produtos
)

printIter(produtos)
printIter(novosProdutos)