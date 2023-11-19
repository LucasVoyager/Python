nome = input('digite seu nome')
idade = int(input('digite sua idade'))

if nome and idade:
    print(f'{nome} tem {idade} anos')
    print(f'seu nome invertido é {nome[::-1]}')
    if' ' in nome:
        print(f'nome contem espaços')
    else:
        print(f'nome não contem espaços{nome}')
    print(f'seu nome tem {len(nome)}')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}' )
else:
    print('você não digitou nada')
