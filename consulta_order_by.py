from configuracion import Session
from crear_base_entidades import Clinica

session = Session()

resultado = session.query(
    Clinica
).order_by(
    Clinica.nombre
).all()

for clinica in resultado:
    print(clinica.nombre)