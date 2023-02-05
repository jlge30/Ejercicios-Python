#funciones
def imprimir():
    print("holafdas mundo")
    print("holafdas mundo")
    print("holafdas mundo")


imprimir()
imprimir()
num1 = 5
num2 = 7
print(num1 + num2)

def sumar( a, b):# funciones con retorno
    c = a + b
    return c

def sumar_sin_retornon(a, b):
    c = a + b
    print(c)

print(sumar ( 8, 10))
sumar_sin_retornon(8,9)
# listas
milista= ["Ana","Andres","jose","hola"]
print(milista)#im prime todo
print(milista[2])#imprime el 2
print(milista[0:2])#imprime desde el cero al 2
milista.append("Juana")#añade elementos
print(milista)
milista.insert(3,"Raul")#añade elementos en una posición concreta
print(milista)
milista.extend(["Antonio","Felipe","Clara"])# añadir más listas
print(milista)
