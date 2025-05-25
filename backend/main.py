from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from config import Settings
from sqlalchemy.orm import Session
import soap_client
import database

# Cargar variables de entorno y configuración
load_dotenv()
settings = Settings()

# Inicializar aplicación FastAPI
app = FastAPI(title="SIAT API", description="API para integración con servicios SIAT")

# Configurar CORS si está habilitado
if settings.ENABLE_CORS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.get("/")
def root():
    return {"message": "Hello SIAT"}

@app.get("/soap/verificar-comunicacion")
def verificar():
    return soap_client.verificar_comunicacion()
