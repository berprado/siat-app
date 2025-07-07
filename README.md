DOCUMENTACIÓN DEL SCRIPT
=========================

Este script configura un entorno completo para el desarrollo de un sistema SIAT con FastAPI (backend) y React (frontend).

Componentes
------------

1. **Validación de herramientas:** Asegura que `python`, `pip`, `npm`, y `git` estén disponibles en el sistema.
2. **Gestión de carpeta del proyecto:** Borra el proyecto existente si el usuario lo autoriza.
3. **Estructura del proyecto:** Crea carpetas `backend` y `frontend` dentro de `siat-app`.
4. **Entorno virtual:** Crea y activa un entorno virtual para aislar dependencias Python.
5. **Archivos backend:**
   - `main.py`: Servidor FastAPI básico + endpoint `/soap/verificar-comunicacion`
   - `config.py`: Clase Settings con variables leídas desde `.env`
   - `soap_client.py`: Cliente Zeep para consumir método `verificarComunicacion()`
   - `.env`, `.env.example`: Variables de entorno configurables
   - `requirements.txt`: Dependencias
6. **React frontend:** Se genera plantilla con Vite + React. Componente `App.jsx` llama al endpoint backend.
7. **Script `run.ps1`:** Lanza backend y frontend simultáneamente en terminales separadas.
8. **Control de versiones:** Se crea repo Git y `.gitignore` con exclusiones estándar.

Uso
----

```bash
# Clonar proyecto
https://github.com/berprado/siat-app

# Iniciar entorno en Windows PowerShell
cd siat-app
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
./setup_project.ps1

# Activar entorno y correr servidor backend
venv\Scripts\Activate.ps1
cd backend
uvicorn main:app --reload

# Iniciar frontend
cd ../frontend/siat-ui
npm run dev

# Ejecutar ambos automáticamente
./run.ps1
```

Dependencias backend
---------------------

- `fastapi[all]`
- `python-dotenv`
- `zeep`
- `pydantic`
- `pydantic-settings`

Licencia
---------

Uso interno para integrar servicios SIAT con estructura limpia y modular.

Repositorio GitHub
-------------------

<https://github.com/berprado/siat-app>

Badges
-------

![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/fastapi-uvicorn-green)
![React](https://img.shields.io/badge/react-frontend-blue)
