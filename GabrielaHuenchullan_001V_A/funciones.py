import statistics #geometric median  
import random
import csv

def asignar_sueldos_aleatorios(trabajadores):
    sueldos_trabajadores={}  #sueldos de $300.000 y $2.500.000 que recorra 10 
    for trabajador in trabajadores: 
        sueldo= random.randint(300000,10,2500000)
        sueldos_trabajadores[trabajador]=sueldo
        print("sueldos asignados correctamente")
        print(sueldo)
    return sueldos_trabajadores

def clasificar_sueldos(trabajadores): #para clasificar sueldos segun menor a 800 mil pesos entre 800mil y 2 millones y màs de 2millones
    menor_800000={}
    entre_800000_2000000={}
    mayor_2000000={}


    for trabajador, sueldo in trabajadores.items():
        if sueldo <800000:
            menor_800000[trabajador] = sueldo

        elif sueldo >=800000:
            entre_800000_2000000[trabajador]=sueldo
        else:
            sueldo >2000000
            mayor_2000000[trabajador]=sueldo

    print("sueldos menores a $800.000 TOTAL: ",len(menor_800000)) 
    for trabajador,sueldo in menor_800000.items():
        print(trabajador,": $", sueldo)

    print("sueldos entre $800.000 y $2.000.000 TOTAL: ",len(entre_800000_2000000))
    for trabajador,sueldo in entre_800000_2000000.items():
        print(trabajador,": $", sueldo)

    print("sueldos mayor a $2.000.000 TOTAL: ",len(mayor_2000000))
    for trabajador,sueldo in mayor_2000000.items():
        print(trabajador,": $", sueldo)

    
def ver_estadisticas(sueldos_trabajadores): #estadisticas de sueldos màs alto, sueldo mas bajo, promedio de sueldos, y media geometrica
    sueldos=list(sueldos_trabajadores.values()) 

    if not sueldos_trabajadores:
        print("no se han asignados sueldos aún")
        return None,None,None

    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)
    promedio_sueldo = sum(sueldos) / len(sueldos)
    media_geometrica= statistics.median(sueldos)

    return max_sueldo,min_sueldo,promedio_sueldo,media_geometrica

def reporte_sueldo(sueldos_trabajadores): #función para mostrar el detalle de los sueldos de los trabajadores, según la siguiente regla de negocio, salud, afp, sueldo liquido

    with open('reportes_sueldos.csv','w',newline='') as archivo:
            escritor = csv.writer(archivo,delimiter=',')

            #escribir encabezados

            escritor.writerow(['Nombre trabajador','Sueldo base','Descuento Salud','descuento AFP','sueldo liquido'])
            

            for trabajador,sueldo in sueldos_trabajadores.items():
                escritor.writerow([trabajador,sueldo])

            print("Reporte generado correctamente en reportes_sueldos.csv")




       
       


