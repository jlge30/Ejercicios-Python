import math

i = 1

while i <= 10:
    i = i + 1
    print("Estoy en el bucle "+ str(i))

print("Esto fuera del bucle")
edad = int(input("Introduce tu edad: "))

while edad < 8 or edad > 100:
    print("Edad incorrecta")
    edad = int(input("Introduce tu edad: "))


print("Gracias por darnos el dato")
print("Edad del aspirante: "+ str(edad)+ " años" )

print("--------Programa de calculo rai cuadrada-------")
numero = int(input("Introduce un numero por favor: "))
intentos = 0

while numero < 0: 
    intentos = intentos + 1
    print("No se puede hallar la raiz cuadrada")
    if intentos == 2: 
        print("Has consumido el número máximo de intentos")
        break; # para salir del bucle
    numero = int(input("Introduce de nuevo numero por favor: "))

if intentos < 2: 
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de "+str(numero)+" es: ", solucion)


for letra in "Python":
    if letra =="h":
        continue #excluyo y vuelvo al principio del bucle.
    print("Viendo la letra: ", letra)

#contar caracteres sin espacio en blanco
nombre = "Esto es una prueba"
contador = 0
for i in nombre:
    if i==" ":
        continue
    contador +=1

print("Numero de caracteres: ", contador)