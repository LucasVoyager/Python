# combinations, permutations and product - itertools

from itertools import combinations, permutations, product

def printIter(Iterator):
    print(*list(Iterator), sep='\n')
    print()

pessoas = [
    'João', 'Joana', 'Luiz', 'Leticia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliester']
]

# printIter(combinations(pessoas, 2))
# printIter(permutations(pessoas, 2))
printIter(product(*camisetas))


