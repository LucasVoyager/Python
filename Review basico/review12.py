while True:
    numero1 = input('digite um numero: ')
    numero2 = input('digie outro numero: ')
    operador= input('digite o operador: ')

    numero_validos= None
    num_1_float = 0
    num_2_float = 0
    
    try:
         num_1_float = float(numero1)
         num_2_float = float(numero2)
         numero_validos= True
    except:
        numero_validos = None
    
    if numero_validos is None:
        print('alguns dos numeros são invalidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('operador invalido')
        continue

    print('realizando o calculo!')
    if operador == '+':
        print(num_1_float+num_2_float)
    elif operador == '-':
        print(num_1_float-num_2_float)
    elif operador == '*':
        print(num_1_float*num_2_float)
    elif operador == '/':
        print(num_1_float/num_2_float)
    else:
     print('nunca deveria chegar neste codigo')

    sair = input('quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break
