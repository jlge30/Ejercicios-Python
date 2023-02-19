for i in ["Primavera", "Verano", "Otoño", "Invierno"]:
    print(i)

for i in ["Primavera", "Verano", "Otoño", "Invierno"]:
    print(i, end = "")# lo imprime todo en la misma linea sin espacios

print()
for i in ["Primavera", "Verano", "Otoño", "Invierno"]:
    print(i, end = " ")# lo imprime todo en la misma linea con espacios
print()
for i in "hola como estas":
    print(i, end =" ")# recorre caracter a caracter con un espacio y lo imprime con un espacio

print()

#METODO PARA SABER SI UNA CADENA TIENE UN CARACTER ESPECIFICO, EJE. SABER SI EL CORREO ES OK.
email = False

correo = input("Introduce el correo electronico: ")

for i in correo:
    if i == "@":
        email = True

if email:
    print("El correo es OK incialmente: ", correo)
else:
    print("El correo es NO ES OK: ", correo)
  
contador = 0

#correo = input("Introduce el correo electronico: ")

for i in correo:
    if i == "@" or i == ".":
        contador = contador +1

if contador >= 2:
    print("El correo es OK finalmente: ", correo)
else:
    print("El correo es NO ES OK le falta el dominio: ", correo)


