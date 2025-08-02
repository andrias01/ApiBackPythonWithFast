from fastapi import APIRouter, HTTPException, status
from models import FormularioClienteCreate, FormularioClienteUpdate, ApiResponse
from service import formulario_service
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/formulario", tags=["Formulario Cliente"])

@router.post(
    "/create",
    response_model=ApiResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Crear nuevo formulario cliente",
    description="Crea un nuevo formulario cliente con validaciones de negocio"
)
async def crear_formulario(formulario: FormularioClienteCreate):
    try:
        # ✅ CORRECTO - El servicio ya devuelve ApiResponse, devolverlo directamente
        return formulario_service.crear_formulario(formulario)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error en controlador crear_formulario: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al crear el formulario"
        )



@router.get(
    "/all",
    response_model=ApiResponse,
    status_code=status.HTTP_200_OK,
    summary="Obtener todos los formularios",
    description="Obtiene la lista completa de formularios cliente ordenados por fecha de creación"
)
async def buscar_todos():
    try:
        # ✅ El servicio ya devuelve ApiResponse, devolverlo directamente
        return formulario_service.buscar_todos()
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error en controlador buscar_todos: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al obtener los formularios"
        )
    
@router.get(
    "/{id}",
    response_model=ApiResponse,
    status_code=status.HTTP_200_OK,
    summary="Buscar formulario por ID",
    description="Obtiene un formulario específico por su ID único"
)
async def buscar_por_id(id: str):
    try:
        # ✅ El servicio ya devuelve ApiResponse, devolverlo directamente
        return formulario_service.buscar_por_id(id)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error en controlador buscar_por_id: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al buscar el formulario"
        )

@router.put(
    "/{id}",
    response_model=ApiResponse,
    status_code=status.HTTP_200_OK,
    summary="Actualizar formulario cliente",
    description="Actualiza un formulario existente. Solo se actualizan los campos proporcionados"
)
async def actualizar_formulario(id: str, formulario: FormularioClienteUpdate):
    try:
        # ✅ El servicio ya devuelve ApiResponse, devolverlo directamente
        return formulario_service.actualizar_formulario(id, formulario)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error en controlador actualizar_formulario: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al actualizar el formulario"
        )

@router.delete(
    "/{id}",
    response_model=ApiResponse,
    status_code=status.HTTP_200_OK,
    summary="Eliminar formulario cliente",
    description="Elimina un formulario cliente de forma permanente"
)
async def eliminar_formulario(id: str):
    try:
        # ✅ El servicio ya devuelve ApiResponse, devolverlo directamente
        return formulario_service.eliminar_formulario(id)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error en controlador eliminar_formulario: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error interno del servidor al eliminar el formulario"
        )