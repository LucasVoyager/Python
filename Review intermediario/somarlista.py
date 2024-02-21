def somarList (la, lb):
     intervalo_maximo = min(len(la), len(lb))
     return [
         (la[i] + lb[i]) for i in range(intervalo_maximo)
     ]

la = [1,2,3,4,5,6,7]
lb = [1,2,3,4]
print(list(somarList(la, lb)))


