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


edad2 = int(input("Introduce tu edad"))

if edad2 < 100 and edad2 > 0: 
    print("Edad correcto")
else: 
    print("Edad incorrecta")


salario_presidente = int(input("Introduce salario del presidente"))
print("Salario del presidente", str(salario_presidente))
salario_director = int(input("Introduce salario del director"))
print("Salario del director", str(salario_director))
salario_jefe_area = int(input("Introduce salario del jefe de area"))
print("Salario del jefe de area", str(salario_jefe_area))
salario_administrativo = int(input("Introduce salario del administrativo"))
print("Salario del administrativo", str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_director:
    print("Todo está correcto")
else:
    print("Algo falla en la empresa")

print("Programa Becas")
distancia_escuela = int(input("Introduce la distancia a la escuela"))
print("Distancia a la escuela: ", distancia_escuela)
num_hermanos = int(input("Introduce los hermanos que tienes en la escuela"))
print("Numero de hermanos: ", num_hermanos)
salario = int(input("Introduce el salario"))
print("Salario: ", salario)

if distancia_escuela > 40 and num_hermanos > 2 and salario <= 20000:
    print("Te corresponde la beca")
else: 
    print("NO te corresponde ninguna beca")

print("Asignaturas año 2021")
print("Asignaturas optativas: Matematicas, Lengua, Informatica")
opcion = input("Introduce la asignatura")
asignatura = opcion.lower()# trasforma la escritura en minusculas.

if asignatura in ("matematicas", "lengua", "informatica"):
    print("Has elegido " + asignatura)
else:
    print("La asignatura escogida no es correcta")







