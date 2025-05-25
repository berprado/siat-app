from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENABLE_CORS: bool = False
    WSDL_URL: str
    WSDL_URL_SYNC: str
    WSDL_URL_CODIGOS: str
    WSDL_URL_OPERACIONES: str
    WSDL_URL_AJUSTE: str
    WSDL_URL_REVERSION: str
    WSDL_URL_FACTURACION: str
    API_KEY: str
    CODIGO_AMBIENTE: int
    CODIGO_PUNTO_VENTA: int
    CODIGO_EMPRESA: int
    CODIGO_SISTEMA: str
    CODIGO_SUCURSAL: int
    CODIGO_MODALIDAD: int
    CUIS: str
    NIT: int
    MYSQL_HOST: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_PORT: int
    RAZON_SOCIAL: str
    DEPARTAMENTO: str
    DIRECCION: str
    MUNICIPIO: str
    NOMBRE_SUCURSAL: str
    TELEFONO: str
    DESCUENTO: int
    CODIGO_DOCUMENTO_SECTOR: int
    CODIGO_TIPO_EMISION: int
    CODIGO_TIPO_FACTURA: int
    DESCRIPCION_TIPO_FACTURA: str
    SUBTITULO: str
    ACTIVIDAD_ECONOMICA: int
    CODIGO_PRODUCTO_SIN: int
    NUMERO_SERIE: str
    NUMERO_IMEI: str
    PRIVATE_KEY_PASSWORD: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"
