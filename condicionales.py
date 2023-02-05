print("--------------Programa evaluacion notas----------")
def evaluacion(nota):#funcion
    valoracion = "aprobado"
    if nota < 5:#condicional
        valoracion = "suspenso"
    if nota > 8:
        valoracion = "!!!sobresaliente!!!!"
    
    return valoracion

print(evaluacion(4))
print(evaluacion(8))
print(evaluacion(9))
nota = int(input("Introduce la nonta: "))# cambiamos el tipo de dato
print(evaluacion(nota))
nota1 = input("Introduce la nonta1: ")
print(evaluacion(int(nota)),"y ", evaluacion(int(nota1)))# cambiamos el tipo de dato
print("hola")
