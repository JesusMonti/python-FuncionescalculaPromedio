""" El programa se encarga se obtener el promedio de un alumno y mandar un mensaje en base a su rendimiento
    
    Primero se pregunta en el main cuantas materias se van a promediar, y en base a esto
    se manda a llamar una función que recibe como parametro el numero de materias del alumno para pedir 
    las calificaciones de las materias y almacenarlas en una lista, la cual sera retornada por la función.

    Como segundo paso, se manda a llamar otra función para que calcule el promedio en base a la lista retornada del 
    punto anterior una vez que se calcula el promedio, se manda a llamar una función que en base a su valor mandará 
    mensaje en base a su rendimiento escolar.
"""
def evaluacion(nota):
    print(nota)
    valoracion="Excelente estas aprobado"
    if nota<10 and nota >=8:
        valoracion="Muy bien, estas aprobado"
    elif nota<8 and nota >=6:
        valoracion = "Regular, alcanzaste a pasar"
    elif nota<6 and nota >=0:
        valoracion = "Mal, estas suspendio"
    return valoracion

def introduce_calificaciones(materias):
    calificaciones = list()
    for mat in range(materias):
        cal = int(input(f"Introduzca la {mat+1} primer calificacion"))
        calificaciones.append(cal)
    return calificaciones

def promedio_Alumnos(calificaciones):
    acum=0#Valor acumulado antes del promedio
    promedio=0#Promedio de calificaciones
    for mar in calificaciones:
        acum += mar
    promedio= acum / len(calificaciones)
    print(f"El promedio es {promedio}")
    #Obtenemos su evaluacion
    print(evaluacion(promedio))

#Funcion main
print("Programa para la evaluacion de notas de alumnos")
materias = int(input("Introduzca el numero de materias"))
calificaciones=introduce_calificaciones(materias)
promedio_Alumnos(calificaciones)
print("Gracias, vuelva pronto")