from fastapi import FastAPI
from app.database import engine, Base
from app.routes import registro_routes

# importar modelos para que SQLAlchemy los registre
from app.models import registro  

app = FastAPI()
app.include_router(registro_routes.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"msg": "API con SQLite 🚀"}

