def generaPares(limite):# funcion normal
    num = 1
    miLista=[]
    while num<limite: 
        miLista.append(num*2)
        num +=1
    return miLista

print(generaPares(9))

# funcion generador

def generaPares(limite):# funcion normal
    num = 1
  
    while num<limite: 
        yield num * 2 # es lo que nos va a devolver paso a paso

        num +=1
devuelvePares = generaPares(10)

for i in devuelvePares: 
    print(i)


def generaPares(limite):# funcion normal
    num = 1
  
    while num<limite: 
        yield num * 2 # es lo que nos va a devolver paso a paso

        num +=1

devuelvePares = generaPares(10)
print("Comienzo la llamada a la funcion")
print(next(devuelvePares))# primera llamada

print("Mas código")

print(next(devuelvePares))# segunda llamada

print("Mas código")

print(next(devuelvePares))# tercera llamada
