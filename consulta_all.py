from configuracion import Session
from crear_base_entidades import Clinica

session = Session()

clinicas = session.query(
    Clinica
).all()

for clinica in clinicas:

    total_historias = 0

    for consultorio in clinica.consultorios:
        for veterinario in consultorio.veterinarios:
            total_historias += len(
                veterinario.historias
            )

    print(
        f"Clínica: {clinica.nombre}"
    )

    print(
        f"Historias Clínicas: {total_historias}"
    )

    print("-" * 40)