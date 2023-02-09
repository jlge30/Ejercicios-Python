edad = int(input("Introduce tu edad"))

if edad < 18:
    print("Eres menor de edad NO puedes pasar")
elif edad > 100:
    print("Edad incorrecta")
else:
     print("Puedes pasar")

nota_alumno = int(input("Introduce la nota del examen"))

if nota_alumno < 5: 
    print("Insufciente")
elif nota_alumno < 6 :
    print("Suficiente")
elif nota_alumno < 7 :
    print("Bien")
elif nota_alumno < 9 :
    print("Notable")
else:
    print("Sobresaliente")






