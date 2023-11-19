def soma (s,z,x):
    print(f'{s=}, {z=}, {x=}',' |', 's + z + x = ', x + z + x)

soma(1,2,3)

def soma1(x,y,z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma1(5 , 2)
soma1(5 , 3, 6)
soma1(8, 9, 1)
soma1(2 , 3)

def soma3(x,y):
    return x + y

soma32 = soma3(1,2)
soma42 = soma3(5,6)

print(soma32 + soma42)

def soma34(*args):
    total = 0
    for numero in args:
        print('Tota', total, numero)
        total = total + numero
        print('Total', total)
    print(total)

soma34(1,2,3,4,5,6)