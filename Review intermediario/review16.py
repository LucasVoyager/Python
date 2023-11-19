lista = ['a', 1, 1.1, True, [0,1,2], (1,2), {0,1}, {'nome': 'Lucas'}]

for item in lista:
    if isinstance(item,set):
        print('SET')
        item.add(5)
        print(item, isinstance(item,set))
    elif isinstance(item,str):
        print('STRING')
        print(item.upper())
    elif isinstance(item,(int,float)):
        print('NUMBER')
        print(item, item)
    else:
        print('outro')
        print(item)
