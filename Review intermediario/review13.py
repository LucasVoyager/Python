def executa(funcao, *args):
    return funcao(*args)


duplica = executa(
    lambda m: lambda n: n * m,
    2
)

print(duplica(2))

print(
    executa(
    lambda x, y : x + y,
    2,3
))

print(executa(
    lambda *args: sum(args),
    1,5,8,9,6,3,20,52
))