from typing import List
from fastapi import HTTPException, status
from models import FormularioClienteCreate, FormularioClienteUpdate, ApiResponse, FormularioClienteResponse
from repository import formulario_repository
import logging
import uuid

logger = logging.getLogger(__name__)

class FormularioClienteService:
    
    def crear_formulario(self, formulario: FormularioClienteCreate) -> ApiResponse:
        try:
            resultado = formulario_repository.crear_formulario(formulario)
        
        # ✅ Ya no necesitas los logs de debug
            return ApiResponse(
                message=["Formulario creado satisfactoriamente."],
                data=[resultado]
            )
        except Exception as e:
            logger.error(f"Error en servicio crear_formulario: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error interno del servidor al crear el formulario"
            )
    
    def buscar_por_id(self, formulario_id: str) -> ApiResponse:
        try:
            # Validar formato UUID
            try:
                uuid.UUID(formulario_id)
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El ID proporcionado no tiene un formato válido"
                )
            
            resultado = formulario_repository.buscar_por_id(formulario_id)
            if not resultado:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Formulario no encontrado"
                )
            
            return ApiResponse(
                message=["Formulario consultado satisfactoriamente."],
                data=[resultado]
            )
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error en servicio buscar_por_id: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error interno del servidor al consultar el formulario"
            )
    
    def buscar_todos(self) -> ApiResponse:
        try:
            resultados = formulario_repository.buscar_todos()
            if not resultados:
                return ApiResponse(
                    message=["No se encontraron formularios."],
                    data=[]
                )
            
            return ApiResponse(
                message=["Los formularios fueron consultados satisfactoriamente."],
                data=resultados
            )
        except Exception as e:
            logger.error(f"Error en servicio buscar_todos: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error interno del servidor al consultar los formularios"
            )
    
    def actualizar_formulario(self, formulario_id: str, formulario: FormularioClienteUpdate) -> ApiResponse:
        try:
            try:
                uuid.UUID(formulario_id)
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El ID proporcionado no tiene un formato válido"
                )
            
            existente = formulario_repository.buscar_por_id(formulario_id)
            if not existente:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Formulario no encontrado"
                )
            
            resultado = formulario_repository.actualizar_formulario(formulario_id, formulario)
            if not resultado:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Formulario no encontrado"
                )
            
            return ApiResponse(
                message=["Formulario actualizado satisfactoriamente."],
                data=[resultado]
            )
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error en servicio actualizar_formulario: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error interno del servidor al actualizar el formulario"
            )
    
    def eliminar_formulario(self, formulario_id: str) -> ApiResponse:
        try:
            try:
                uuid.UUID(formulario_id)
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="El ID proporcionado no tiene un formato válido"
                )
            
            existente = formulario_repository.buscar_por_id(formulario_id)
            if not existente:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Formulario no encontrado"
                )
            
            eliminado = formulario_repository.eliminar_formulario(formulario_id)
            if not eliminado:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Formulario no encontrado"
                )
            
            return ApiResponse(
                message=["Formulario eliminado satisfactoriamente."],
                data=[]
            )
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error en servicio eliminar_formulario: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error interno del servidor al eliminar el formulario"
            )

formulario_service = FormularioClienteService()
