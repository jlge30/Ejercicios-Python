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
milista.extend(["Antonio","Raul","Clara"])# añadir más listas
print(milista)
print(milista.index("Raul"))# nos devuelve el primer indice donde está un valor
print("Pepe" in milista)# nos devuelve verdadero o falso, busca valores en la búsqueda
milista.extend([False, 2])# se pueden añadir elementos de difernte tipo a la misma lista
print(milista)
milista.remove("Raul")#elimina elementos de una lista
print(milista)
milista.remove("Raul")
print(milista)
milista.pop()#elimina el último elemento de una lista
print(milista)
milista1= ["Juan","Santos","Con","Yo"]
milista3 = milista + milista1#juntamos listas con el más
print(milista3)
milista1= ["Juan","Santos","Con","Yo"]*3 # multiplico la lista por 3
print(milista1)
#Tuplas no se pueden mover dentro de las mismas
mitupla = ("hola", "Pedro","Joaquin","Pedro",12,True)
print(mitupla)
print("hola")
print(mitupla[2])#escojo un elemento
mitupla1 = tuple(milista1)#convierto una lista en tupla
print(mitupla1)
milista11 = list(mitupla)#convierto en lista una tupla
print(milista11)
print(mitupla.count("Pedro"))#cuento elementos de la tupla
print(len(mitupla))# longitud de la tupla
mitupla3 = ("Juan", 12,2, 2022)
nombre, dia, mes, agno = mitupla3 #desempaquetado de tupla
print(nombre)
print(dia)
print(mes)
print(agno)