def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero  
        return total

multiplicacao = multiplica(10,2,3,4,5)
print(multiplicacao)

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'

outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))

