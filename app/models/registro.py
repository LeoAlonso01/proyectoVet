from sqlalchemy import Column, String
from app.database import Base
import uuid

class Registro(Base):
    __tablename__ = "registros"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    fecha = Column(String)