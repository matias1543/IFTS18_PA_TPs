import csv
import os
import requests
from model_participante import ModelParticipante
from db_setup import Base, session, engine

class Participante:
    def __init__(self, nro_participante, nombre, apellido, edad, sexo):
        self.nro_participante = nro_participante
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

    def __str__(self):
        return "Nro de participante: {}, Nombre: {}, Apellido: {}, Edad: {}, Género: {}".format(self.nro_participante, self.nombre, self.apellido, self.edad, self.sexo)


class Disparo(Participante):
    def __init__(self, nro_participante, nombre, apellido, edad, sexo, disparos, mejor_disparo, promedio_disparo):
        Participante.__init__(self, nro_participante, nombre, apellido, edad, sexo)
        self.disparos = disparos
        self.mejor_disparo = mejor_disparo
        self.promedio_disparo = promedio_disparo

    def __repr__(self):
        return repr((self.nro_participante, self.nombre, self.apellido, self.edad, self.mejor_disparo))

class Concurso:
    participantes = []

    def __init__(self, participantes):
        self.participantes = participantes

    def ordenar_lista_mejor_disparo(self, participantes):
        if not participantes:
            return False
        else:
            return sorted(self.participantes, key=lambda participante: participante.mejor_disparo)

    def ver_registros(self):
        if not self.participantes:
            print("\nNo hay participantes registrados.")
        else :
            for participante in self.participantes:
                print("{}, Disp1: {}, Disp2: {}, Disp3: {}, MejorDisp: {}, PromDisp: {}".format(participante, participante.disparos[0], participante.disparos[1],participante.disparos[2], participante.mejor_disparo, participante.promedio_disparo))

    def ver_ganadores(self):
        lista_ordenada = self.ordenar_lista_mejor_disparo(self.participantes)
        if lista_ordenada == False:
            print("\nNo hay participantes registrados.")
        elif len(lista_ordenada) == 1:
            print("\n1er Puesto => {}, Mejor disparo: {}\n".format(lista_ordenada[0], lista_ordenada[0].mejor_disparo))
        elif len(lista_ordenada) == 2:
            print("\n1er Puesto => {}, Mejor disparo: {}\n2do Puesto => {}, Mejor disparo: {}\n".format(lista_ordenada[0], lista_ordenada[0].mejor_disparo, lista_ordenada[1], lista_ordenada[1].mejor_disparo))
        else:
            print("\n1er Puesto => {}, Mejor disparo: {}\n2do Puesto => {}, Mejor disparo: {}\n3er Puesto => {}, Mejor disparo: {}".format(
                lista_ordenada[0], lista_ordenada[0].mejor_disparo, lista_ordenada[1], lista_ordenada[1].mejor_disparo, lista_ordenada[2], lista_ordenada[2].mejor_disparo
                ))

    def ver_ultimo_puesto(self):
        lista_ordenada = self.ordenar_lista_mejor_disparo(self.participantes)
        if lista_ordenada == False:
            print("\nNo hay participantes registrados.")
        else:
            print("\nUltimo Puesto => {}, Mejor disparo: {}".format(lista_ordenada[-1],lista_ordenada[-1].mejor_disparo))        

    def ver_cantidad_participantes(self):
        print("\nCantidad de participantes: {}".format(len(self.participantes)))

    def ver_participantes_ordenados_por_edad(self):
        if not self.participantes:
            print("\nNo hay participantes registrados.")
        else:
            lista_ordenada = sorted(self.participantes, key=lambda participante: participante.edad)
            for participante in lista_ordenada:
                print(participante)
    
    def ver_participantes_promedios(self):
        if not self.participantes:
            print("\nNo hay participantes registrados.")
        else:
            for participante in self.participantes:
                print("{}, Promedio Disparo: {}".format(participante, participante.promedio_disparo))

    def guardar_csv(self):
        if not self.participantes:
            print("\nNo hay participantes registrados.")
        else:
            with open("participantes.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Nro Part", "Nombre", "Apellido", "Edad", "Sexo", "Disp1", "Disp2", "Disp3", "MejorDip", "PromDisp"])
                for participante in self.participantes:
                    writer.writerow([participante.nro_participante, participante.nombre, participante.apellido, participante.edad, participante.sexo,
                                            participante.disparos[0], participante.disparos[1], participante.disparos[2], participante.mejor_disparo,
                                            participante.promedio_disparo])
            print("Se guardo exitosamente en el archivo 'participantes.csv'")

    def guardar_db(self):
        if not self.participantes:
            print("\nNo hay participantes registrados.")
        else:
            Base.metadata.create_all(engine)

            for participante in self.participantes:
                registro = ModelParticipante()
                registro.nro_participante = participante.nro_participante
                registro.nombre = participante.nombre
                registro.apellido = participante.apellido
                registro.edad = participante.edad
                registro.sexo = participante.sexo
                registro.primer_disparo = participante.disparos[0]
                registro.segundo_disparo = participante.disparos[1]
                registro.tercer_disparo = participante.disparos[2]
                registro.mejor_disparo = participante.mejor_disparo
                registro.promedio_disparo = participante.promedio_disparo
                session.add(registro)
                session.commit()
            print("Datos guardados exitosamente.")

    def ver_registros_db(self):
        registros = session.query(ModelParticipante).all()
        for registro in registros:
            print(registro)

    def api_get(self):
        lista_ordenada = self.ordenar_lista_mejor_disparo(self.participantes)

        if lista_ordenada == False:
            print("\nNo hay participantes registrados.")
        else: 
            url = "http://13.58.21.137/flask/api/v2/{}/{}".format(lista_ordenada[0].nombre, lista_ordenada[0].mejor_disparo)
            response = requests.get(url)
            responseJSON = response.json()
            print("Fecha: {}\nmensaje: {}\nNombre: {}\nPremio: {}\nToken: {}".format(
                responseJSON['fecha'], responseJSON['mensaje'], responseJSON['nombre'], responseJSON['premio'], responseJSON['token']
            ))
