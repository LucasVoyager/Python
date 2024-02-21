#functions decoradoras e decoradores(decorators)
#decoradores no python são syntax sugar

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('decoradora')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        # resultado += 'qualquer coisa'
        print(f'seu resultado foi {resultado}')
        print('função foi decorada')
        return resultado
    return interna
# decoradora a primeira

@criar_funcao
# syntax sugar
def inverte_strings(string):
    print(f'{inverte_strings.__name__}')
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')
    
invertida = inverte_strings('123')
print(invertida)