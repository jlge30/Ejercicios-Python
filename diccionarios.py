midiccionario = {"Alemana": "Berlin", "Espagna": "Madrid", "Inglaterra":"Londres"}#creados de diccionarios
print(midiccionario["Espagna"])
print(midiccionario)
midiccionario["Italia"]="Barcelona"#añado un elemento al diccionario
print(midiccionario)
midiccionario ["Italia"] = "Roma"#modifico el diccionario
print(midiccionario)
del midiccionario["Alemana"]#eliminar un valor del diccionario
print(midiccionario)
midiccionario1 = {"Alemana": "Berlin", "Jordan": 23, "Inglaterra":56}
print(midiccionario1)
mitupla = ["Alemana", "Espagna", "Inglaterra"]
midiccionario2 = {mitupla[0]:"Berlin",mitupla[1]:"Madrid",mitupla[2]:"Londres"}# asignar valores desde una tupla
print(midiccionario2)
midiccionario3 ={23:"Jordan", "Nombre": "Michael", "Equipo": "Bulls", "anillos":{"temporadas":[1995,1996,1998]}}#diccionario dentro de otro
print(midiccionario3)
print(midiccionario3["anillos"])
print(midiccionario3.keys())#imprime las claves del diccionario
print(midiccionario3.values())#imprime los valores
print(len(midiccionario3))#longitud del diccionario


