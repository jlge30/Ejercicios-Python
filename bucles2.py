for i in range(5):
    print(f"Valor de i: {i}")#funcion f en impresion

for i in range(5,20):
    print(f"Valor de i: {i}")#funcion f en impresion va desde el 5 hasta el 20

for i in range(5,19, 3):
    print(f"Valor de i: {i}")#funcion f en impresion va desde el 5 hasta el 19 de tres en tres

print(len("hola como estas"))# nos devuelve la longitud de la cadena.
#evaluamos si una cadena de texto tiene una @
valido = False

email= input("Introduce el mail: ")

for i in range(len(email)):
    if email[i] =="@":
        valido = True

if valido:
    print("El correo es OK")
else: 
    print("El correo no es Ok")
