def saudacao(msg,nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

print(
    executa(saudacao, 'bom dia', 'lucas')
)

print(
    executa(saudacao, 'bom dia', 'jonatan')
)