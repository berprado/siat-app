from zeep import Client
from zeep.transports import Transport
from config import Settings
from dotenv import load_dotenv
import requests

load_dotenv()
settings = Settings()

session = requests.Session()
session.headers.update({
    "apikey": settings.API_KEY
})

client = Client(wsdl=settings.WSDL_URL, transport=Transport(session=session))

def verificar_comunicacion():
    response = client.service.verificarComunicacion()
    # Extraer descripción del mensaje si existe
    try:
        return {
            "descripcion": response['mensajesList'][0]['descripcion'],
            "transaccion": response['transaccion']
        }
    except Exception:
        return {"error": "Respuesta inesperada", "raw": response}
