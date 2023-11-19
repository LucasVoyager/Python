def multiplica(*num):
    numero = input("digite o numero: ")
    numero = int(numero)
    numero *=2
    print(f'{numero=}')
    return numero

multiplica()

def par_impar(*num):
    numero = int(input('digite o numero inteiro: '))
    if numero is int:
        print('somente inteiro')
    else:
        numero_par_impar = numero % 2 
        if numero_par_impar == 0:
            print('numero par')
        else:
            print('numero impar') 

par_impar()
