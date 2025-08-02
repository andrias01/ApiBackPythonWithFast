#!/usr/bin/env python3
"""
Script para ejecutar el servidor de desarrollo
"""
import uvicorn
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

if __name__ == "__main__":
    # Obtener configuración del entorno
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    debug = os.getenv("DEBUG", "True").lower() == "true"
    log_level = os.getenv("LOG_LEVEL", "info").lower()
    
    print(f"🚀 Iniciando servidor en http://{host}:{port}")
    print(f"📚 Documentación disponible en http://{host}:{port}/docs")
    print(f"🏥 Health check en http://{host}:{port}/health")
    
    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=debug,
        log_level=log_level,
        access_log=True
    )