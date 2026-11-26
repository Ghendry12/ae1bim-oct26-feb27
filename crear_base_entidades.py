from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from configuracion import Base
from configuracion import engine


class Clinica(Base):

    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    direccion = Column(String(150))
    veterinario_responsable = Column(String(100))

    consultorios = relationship(
        "Consultorio",
        back_populates="clinica"
    )


class Consultorio(Base):

    __tablename__ = "consultorios"

    id = Column(Integer, primary_key=True)
    nombre_numero = Column(String(50))
    especialidad = Column(String(100))

    clinica_id = Column(
        Integer,
        ForeignKey("clinicas.id")
    )

    clinica = relationship(
        "Clinica",
        back_populates="consultorios"
    )

    veterinarios = relationship(
        "Veterinario",
        back_populates="consultorio"
    )


class Veterinario(Base):

    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True)
    nombres = Column(String(100))
    apellidos = Column(String(100))
    correo = Column(String(100))
    licencia_profesional = Column(String(50))

    consultorio_id = Column(
        Integer,
        ForeignKey("consultorios.id")
    )

    consultorio = relationship(
        "Consultorio",
        back_populates="veterinarios"
    )

    historias = relationship(
        "HistoriaClinica",
        back_populates="veterinario"
    )


class HistoriaClinica(Base):

    __tablename__ = "historias_clinicas"

    id = Column(Integer, primary_key=True)
    fecha_atencion = Column(Date)
    diagnostico = Column(String(200))
    tratamiento = Column(String(200))
    nombre_mascota = Column(String(100))

    veterinario_id = Column(
        Integer,
        ForeignKey("veterinarios.id")
    )

    veterinario = relationship(
        "Veterinario",
        back_populates="historias"
    )


Base.metadata.create_all(engine)

print("Base de datos creada correctamente")

