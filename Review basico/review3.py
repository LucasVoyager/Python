nome = str(input('digite seu nome'))
encontrar = str(input('digite o que deseja encontrar'))

if encontrar in nome: 
    print(f'{encontrar} está contido em {nome}')     
else:
    print(f'{encontrar} não está contido em {nome}') 
          