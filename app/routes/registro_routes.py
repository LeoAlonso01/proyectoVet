from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.registro import Registro

router = APIRouter()

# dependencia para DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/registros")
def crear_registro(nombre: str, descripcion: str, fecha: str, db: Session = Depends(get_db)):
    nuevo = Registro(
        nombre=nombre,
        descripcion=descripcion,
        fecha=fecha
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo