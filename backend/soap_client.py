from zeep import Client
from config import Settings
from dotenv import load_dotenv

load_dotenv()
settings = Settings()

client = Client(wsdl=settings.WSDL_URL)

def verificar_comunicacion():
    response = client.service.verificarComunicacion()
    return {"resultado": response}
