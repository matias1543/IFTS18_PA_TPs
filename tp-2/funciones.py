import math
from classes import Disparo
from statistics import mean

def validacion_numero(cadena):
    return any(char.isdigit() for char in cadena)

def agregar_participante(lista, id_participante):
    nro_participante = id_participante
    lista_disparos = []
    # Agrega los datos del participante
    while True:
        try:
            while True:
                nombre = input("Ingresar el nombre: ")
                apellido = input("Ingresar el apellido: ")
                edad = int(input("Ingresar edad: "))
                sexo = input("Ingresar género (M / F): ")
                if (validacion_numero(nombre) or validacion_numero(apellido) or validacion_numero(sexo)):
                    print("Porfavor, no ingresar números en el nombre, apellido y sexo.")
                elif(sexo != "M" and sexo != "F"):
                    print("Porfavor, ingresar en el genero solamente la letra 'M' o 'F'.")
                else:
                    break
            break
        except ValueError:
            print("Porfavor, ingresar solamente números en la edad.")
    
    # Agrega los disparos del participante
    while len(lista_disparos) != 3:
        print("\nDisparo - {}".format(len(lista_disparos)+1))
        while True:
            try:
                x = float(input("Ingresar coordenada X: "))
                y = float(input("Ingresar coordenada Y: "))
                if(x <= 80 and y <= 80):
                    break
                else:
                    print("Porfavor, ingresar coordenadas menor o igual a 80.")
            except ValueError:
                print("El dato ingresado es incorrecto. Porfavor, ingresar solamente números.")

        distancia = round(math.sqrt(x**2 + y**2), 2)
        print("Distancia de disparo {} -> {}".format(len(lista_disparos)+1, distancia))
        lista_disparos.append(distancia)
    participante = Disparo(nro_participante, nombre, apellido, edad, sexo, lista_disparos, round(min(lista_disparos), 2), round(mean(lista_disparos), 2))
    lista.append(participante)


def menu():
    print("\n***********************************************")
    print("*  Bienvenido al concurso.                    ***")
    print("*  Menu:                                      ***")
    print("*  1. Agregar Participante.                   ***")
    print("*  2. Ver todos los registros.                ***")
    print("*  3. Ver los ganadores.                      ***")
    print("*  4. Ver el ultimo puesto.                   ***")
    print("*  5. Ver cantidad de participantes.          ***")
    print("*  6. Ver participantes ordenados por edad.   ***")
    print("*  7. Ver promedio de todos los disparos.     ***")
    print("*  8. Guardar registros en un archivo csv.    ***")
    print("*  9. Guardar registros en la base de datos.  ***")
    print("*  10. Ver registros de la base de datos.     ***")
    print("*  11. API POST")
    print("*  12. Salir.                                 ***")
    print("*************************************************")

# Salir del menu del concurso
def salir():
    print("\nDesea Salir?\n1.Si\n2.No")
    while True:
        try:
            opcion = int(input("\nSeleccionar la opción a realizar: "))
            if opcion == 1:
                return True
            elif opcion == 2:
                return False
            else:
                print("Porfavor, ingresar solamente las opciones disponibles.")
        except ValueError:
            print("Porfavor, ingresar solamente las opciones disponibles.")