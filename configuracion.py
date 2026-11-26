from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

cadena_base_datos = "sqlite:///clinicas_veterinarias.db"

engine = create_engine(cadena_base_datos)

Base = declarative_base()

Session = sessionmaker(bind=engine)