entrada = input('digite seu nome: ')

try:
    nome_user = str(entrada)

    if len(nome_user) <= 4:
        print('seu nome é muito curto!')
    elif len(nome_user) >= 5 and len(nome_user) <=6:
        print('seu nome é normal!')
    elif len(nome_user) > 6:
        print('seu nome é muito grande!')
except:
    print('o nome digitado é invalido!')
