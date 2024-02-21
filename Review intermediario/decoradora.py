#decoradores com parâmetros
def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_func(func):
        print('Decoradora 1')
    
        def aninhada(*args, **kwargs):
            print('parametros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res 
        return aninhada
    return fabrica_de_func
    

@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

times = fabrica_de_decoradores()(lambda x,y: x*y)
tenMoreFive = soma(10,5)
tenPlusFive = times(10,5)
print(tenMoreFive)
print(tenPlusFive)