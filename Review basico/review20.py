import random

def gera_cpf():
    cpf = [random.randint(0,9) for _ in range(9)]
    soma = sum((i + 1) * digit for i, digit in enumerate(cpf))
    resto = soma % 11
    if resto < 2:
        cpf.append(0)
    else:
        cpf.append(11 - resto)
    soma = sum((i + 2) * digit for i, digit in enumerate(cpf))
    resto = soma % 11
    if resto < 2:
        cpf.append(0)
    else:
        cpf.append(11 - resto)
    return ''.join(map(str,cpf))

if __name__ == "__main__":
    cpf = gera_cpf()
    print('cpf gerado: ', cpf)
