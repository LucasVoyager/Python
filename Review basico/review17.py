import os

lista = []

while True:
    print('selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    if opcao == 'i':
        os.system('cls')
        valor = input('valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str  = input(
               'escolha o indice para apagar')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('digite numero inteiro')
        except IndexError:
            print('indice invalido')
        except Exception:
            print('erro')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('nada para listar')
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('opção invalida')