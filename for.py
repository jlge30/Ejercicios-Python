for x in range(0,5):#bucle for.
    print("hola")
print(list(range(10,20)))## hacemos una lista 


for y in range(0,20):
    print("Numero: ", y+1)


lista = ["Pedro","Antonio","Jorge","Raul","Raimundo","Teresa"]



for i in lista:#imprimir la lista con un for
    print(i)
    for j in lista:
        print(j)

monedas_encontradas = 5
monedas_magicas = 70
monedas_robadas = 3
monedas = monedas_encontradas



for wek in range(0,15):
    monedas = monedas + monedas_magicas-monedas_robadas
    print("Semana %s = %s"%(wek, monedas))

x = 0
i =0
while x < 10 and i < 20: 
    x = x +1
    i = i + 1
    print(x, i)


for x in range(0, 20):
    print('hello %s' % x)
    if x > 9:
        break


ingredients = ['snails', 'leeches', 'gorilla belly-button lint',
'caterpillar eyebrows', 'centipede toes']

for i in ingredients :
    print(i)

def imprimir(nombre, apellido):# funciones
    print("El nombre completo es: %s %s " %(nombre, apellido))

nom = "Raul"
apell = "Garcia"
imprimir(nom, apell)

def resultado(a, b, c):
    d = a + b -c
    return d

print(resultado(4,8,9))
import time # importamos modulos
print(time.asctime())
print(time.localtime())
import sys# lee y repite lo leido
print(sys.stdin.readline())

def mirarEdad():
    print("¿Cuantos años tienes?")
    edad = int(sys.stdin.readline())
    if edad >= 10 and edad <= 13:
        print("Eres un trasto")
    else:
        print("Vale no eres un trasto")

mirarEdad()





