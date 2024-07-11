import funciones as fn

trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

sueldos_trabajadores={}

while True: 
    print("---BIENVENIDO A MENU ASIGNACION Y CLASIFICACION DE SUELDOS---")
    print("1. Inicializar datos: ")
    print("2. Asignar sueldos aleatorios: ")
    print("3. Clasificar sueldos: ")
    print("4. Ver estadìsticas:  ")
    print("5. Reporte de sueldos: ")
    print("6. Salir del programa: ")

    opcion=int(input("Seleccione Opcion (1-6): "))

    if opcion ==1:
        sueldos_trabajadores={trabajador: 0 for trabajador in trabajadores}
        print("Inicializando: ",trabajadores)
    elif opcion==2:
        if not trabajadores:
            print("debe inicializar datos primero")
        else:
            sueldos_trabajadores=fn.asignar_sueldos_aleatorios(trabajadores)
    elif opcion ==3:
        if sueldos_trabajadores:
            fn.clasificar_sueldos(trabajadores)
        else:
            print("debe asignar valor en sueldos aleatorios")
    elif opcion ==4:
        if sueldos_trabajadores:
            max_sueldo,min_sueldo,promedio_sueldo,media_geometrica=fn.ver_estadisticas(sueldos_trabajadores)
            if max_sueldo is not None:
                print("Crédito máximo: $", max_sueldo)
                print("Crédito mínimo: $", min_sueldo)
                print("Promedio créditos: $", promedio_sueldo)
                print("Media geometrica: ", media_geometrica)
            else:
                print("primero debe asignar créditos")
    elif opcion ==5:
        if sueldos_trabajadores:
            fn.reporte_sueldo(sueldos_trabajadores)
        else:
            print("Asigne sueldos aleatorios")
    else:
        opcion==6
        print("Finalizando programa...")
        print("Desarrollado por Gabriela Huenchullan")
        print("RUT 18783180-6")
  




    

    
  
