from db_setup import Base
from sqlalchemy import Column, Integer, Float, String

class ModelParticipante(Base):
    __tablename__ = "participante"
    
    id = Column(Integer, primary_key=True)
    nro_participante = Column(Integer, nullable=False)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    edad = Column(Integer, nullable=False)
    sexo = Column(String(1), nullable=False)
    primer_disparo = Column(Float, nullable=False)
    segundo_disparo = Column(Float, nullable=False)
    tercer_disparo = Column(Float, nullable=False)
    mejor_disparo = Column(Float, nullable=False)
    promedio_disparo = Column(Float, nullable=False)

    def __str__(self):
        return "Id: {} | Nro Participante: {} | Nombre: {} | Apellido: {} | Edad: {} | Genero: {} | Dispario 1: {} | Disparo 2: {} | Disparo 3: {} | Mejor Disparo: {} | Promedio Disparo: {}".format(
            self.id, self.nro_participante, self.nombre, self.apellido, self.edad, self.sexo, self.primer_disparo, self.segundo_disparo, self.tercer_disparo, self.mejor_disparo, self.promedio_disparo            
        )