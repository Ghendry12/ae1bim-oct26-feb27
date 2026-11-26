from configuracion import Session
from crear_base_entidades import Veterinario

session = Session()

resultado = session.query(
    Veterinario
).filter(
    Veterinario.licencia_profesional == "LIC001"
).all()

for veterinario in resultado:
    print(
        veterinario.nombres,
        veterinario.apellidos
    )