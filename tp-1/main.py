import funciones
from classes import Concurso

# Agregando participantes y disparos
lista_participantes = []

# Menu del concurso.  
concurso = Concurso(lista_participantes)

while True:
    funciones.menu()
    while True:
        try:
            opcion = int(input("\nSeleccionar la opción que desea realizar: "))
            break
        except ValueError:
            print("\nPorfavor, ingresar una de las opciones del menu.")
    if opcion == 1:
        while True:
            while True:
                try:
                    nro_partic = int(input("\nIngresar el número del participante: "))
                    break
                except ValueError:
                    print("Porfavor, ingresar unicamente números.")
            if nro_partic == 999:
                break
            elif not lista_participantes:
                funciones.agregar_participante(lista_participantes, nro_partic)
            else:
                boolean = True
                for participante in lista_participantes:
                    if participante.nro_participante == nro_partic:
                        print("El 'nro de participante' ingresado ya se encuentra en el sistema.\nPorfavor, ingresar otro número.")
                        boolean = False
                if boolean:
                    funciones.agregar_participante(lista_participantes, nro_partic)
    elif opcion == 2:
        concurso.ver_registros()
        input("\nPresionar un boton para continuar...")
    elif opcion == 3:
        concurso.ver_ganadores()
        input("\nPresionar un boton para continuar...")
    elif opcion == 4:
        concurso.ver_ultimo_puesto()
        input("\nPresionar un boton para continuar...")
    elif opcion == 5:
        concurso.ver_cantidad_participantes()
        input("\nPresionar un boton para continuar...")
    elif opcion == 6:
        concurso.ver_participantes_ordenados_por_edad()
        input("\nPresionar un boton para continuar...")
    elif opcion == 7:
        concurso.ver_participantes_promedios()
        input("\nPresionar un boton para continuar...")
    elif opcion == 8:
        concurso.guardar_csv()
        print("Se guardo exitosamente en el archivo 'participantes.csv'")
        input("\nPresionar un boton para continuar...")
    elif opcion == 9:
        break
    else:
        print("Porfavor, ingresar solamente las opciones disponibles.")
