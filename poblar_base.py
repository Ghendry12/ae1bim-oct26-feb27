from datetime import date

from configuracion import Session

from crear_base_entidades import (
    Clinica,
    Consultorio,
    Veterinario,
    HistoriaClinica
)

session = Session()

# CLINICAS

clinica1 = Clinica(
    nombre="Veterinaria Animal Care",
    direccion="Cuenca - Av. Solano",
    veterinario_responsable="Dr. Carlos Pérez"
)

clinica2 = Clinica(
    nombre="Mascotas Felices",
    direccion="Loja - Av. Universitaria",
    veterinario_responsable="Dra. Ana Torres"
)

# CONSULTORIOS

consultorio1 = Consultorio(
    nombre_numero="Consultorio 101",
    especialidad="Medicina General",
    clinica=clinica1
)

consultorio2 = Consultorio(
    nombre_numero="Consultorio 102",
    especialidad="Cirugía",
    clinica=clinica1
)

consultorio3 = Consultorio(
    nombre_numero="Consultorio 201",
    especialidad="Dermatología",
    clinica=clinica2
)

# VETERINARIOS

vet1 = Veterinario(
    nombres="Luis",
    apellidos="Maldonado",
    correo="luis@gmail.com",
    licencia_profesional="LIC001",
    consultorio=consultorio1
)

vet2 = Veterinario(
    nombres="María",
    apellidos="Romero",
    correo="maria@gmail.com",
    licencia_profesional="LIC002",
    consultorio=consultorio2
)

vet3 = Veterinario(
    nombres="Jorge",
    apellidos="León",
    correo="jorge@gmail.com",
    licencia_profesional="LIC003",
    consultorio=consultorio3
)

# HISTORIAS CLINICAS

h1 = HistoriaClinica(
    fecha_atencion=date(2026, 10, 10),
    diagnostico="Gastritis",
    tratamiento="Medicamentos",
    nombre_mascota="Firulais",
    veterinario=vet1
)

h2 = HistoriaClinica(
    fecha_atencion=date(2026, 10, 15),
    diagnostico="Dermatitis",
    tratamiento="Shampoo medicado",
    nombre_mascota="Luna",
    veterinario=vet3
)

h3 = HistoriaClinica(
    fecha_atencion=date(2026, 10, 20),
    diagnostico="Fractura",
    tratamiento="Cirugía",
    nombre_mascota="Rocky",
    veterinario=vet2
)

session.add_all([
    clinica1,
    clinica2,
    consultorio1,
    consultorio2,
    consultorio3,
    vet1,
    vet2,
    vet3,
    h1,
    h2,
    h3
])

session.commit()

print("Base de datos poblada correctamente")