#  Agrupando valores - groupby
# alunos = ['a','a','a', 'b','b','b', 'c','c','c']
# for aluno in alunosAgrupados:
    # print(aluno)

from itertools import groupby

alunos = [
    {'nome': 'Lucas', 'Nota': 'a'},
    {'nome': 'Lucas', 'Nota': 'b'},
    {'nome': 'Lucas', 'Nota': 'c'},
    {'nome': 'Gabriel', 'Nota': 'a'},
    {'nome': 'Gabriel', 'Nota': 'b'},
    {'nome': 'Gabriel', 'Nota': 'c'},
    {'nome': 'Maria', 'Nota': 'b'},
    {'nome': 'Jonatan', 'Nota': 'b'},
    {'nome': 'Jonatan', 'Nota': 'c'},
    {'nome': 'Jonatan', 'Nota': 'a'},
]

def ordena(aluno):
    return aluno['Nota']

alunosAgrupados = sorted(alunos, key=ordena)

grupos = groupby(alunosAgrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)