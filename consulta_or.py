from sqlalchemy import or_

from configuracion import Session
from crear_base_entidades import Consultorio

session = Session()

resultado = session.query(
    Consultorio
).filter(
    or_(
        Consultorio.especialidad == "Cirugía",
        Consultorio.especialidad == "Dermatología"
    )
).all()

for consultorio in resultado:
    print(
        consultorio.nombre_numero,
        consultorio.especialidad
    )