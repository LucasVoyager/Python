def soma(a,b):
    print(f'A = {a} e b = {b}')
    s = a + b
    print(f'A soma  a + b = {s}')

soma(b=4, a=5)
soma(7,2)

def contador(*num):
    tamanho=len(num)
    print(f'recebi os valores{num} e são todos {tamanho} números')

contador(5,4,5,8,4,)
contador(5,8,9,7,5,4)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos+=1

valores = [7,5,0,4]
dobra(valores)
print(valores)