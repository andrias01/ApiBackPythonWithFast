from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from controller import router as formulario_router
import logging
import uvicorn

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Crear la aplicación FastAPI
app = FastAPI(
    title="API Formulario Cliente",
    description="API para gestión de formularios de clientes con validaciones de negocio",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios específicos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir los routers
app.include_router(formulario_router)

# Endpoint de salud
@app.get("/health", tags=["Health Check"])
async def health_check():
    """Endpoint para verificar el estado de la API"""
    return {
        "status": "healthy",
        "message": "API Formulario Cliente funcionando correctamente",
        "version": "1.0.0"
    }

# Endpoint raíz
@app.get("/", tags=["Root"])
async def root():
    """Endpoint raíz de la API"""
    return {
        "message": "Bienvenido a la API de Formulario Cliente",
        "documentation": "/docs",
        "health": "/health"
    }

# Manejador global de excepciones
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Error no manejado: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "message": ["Error interno del servidor"],
            "data": []
        }
    )

# Manejador de excepciones HTTP
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": [str(exc.detail)],
            "data": []
        }
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )