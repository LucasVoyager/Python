perguntas = [
    {
        'Pergunta': 'Quem descobriu o brasil?',
        'Opções': ['Colombo', 'Pedro alvares', 'Vasco da gama', 'Luiz inacio lula da silva'],
        'Resposta': 'Pedro alvares', 
        },
    {
        'Pergunta': 'Qual das musicas abaixo pertence ao trapper matuê?',
        'Opções':['Novo balanço','Gorilla roxo','44 bulldog','poesia acustica 4'],
        'Resposta': 'Gorilla roxo',
        },

    {
        'Pergunta': 'Quantos estados possuem o brasil?',
        'Opções': ['26','27','22','30'],
        'Resposta': '26',
    },
]

Qtdacertos = 0

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

    for i, opcao in enumerate(opcoes):
        print(f'{i}', opcao)
        print()

    escolha = input('Digite a opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)
    
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    print()

    if acertou:
        Qtdacertos += 1
        print('Acertou :)')
    else:
        print('Errou :(')

print('Você acertou', Qtdacertos)
print('de', len(perguntas), 'perguntas.')
