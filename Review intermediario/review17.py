lista = []
tupla = ()
dicionario = {}
conjunto = set()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
verdade = True
intervalo = range(0)

def falsy(valor):
    return 'falsy' if not valor else 'truthy'

print(f'Teste', falsy('Teste'))
print(f'{lista=}', falsy(lista))
print(f'{tupla=}', falsy(tupla))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}',falsy(conjunto))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{verdade=}', falsy(verdade))
print(f'{intervalo=}', falsy(intervalo))
