entrada= input('Que horas são?(digite numero inteiros): ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!') 
    elif    hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('isso não é hora, amigo!')

except:
    print('digite apenas numeros inteiros')
