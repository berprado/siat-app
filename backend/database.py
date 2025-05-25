from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import Settings

settings = Settings()

# Crear motor de base de datos utilizando la URL de conexión de settings
engine = create_engine(settings.DATABASE_URL)

# Crear clase base para definir modelos
Base = declarative_base()

# Crear fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener una instancia de la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
