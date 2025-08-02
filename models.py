from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List
from datetime import datetime
import re


class FormularioClienteCreate(BaseModel):
    nombre_completo: str = Field(..., min_length=2, max_length=255, description="Nombre completo del cliente")
    email: EmailStr = Field(..., description="Email válido del cliente")
    telefono: int = Field(..., description="Número de teléfono")
    mensaje: str = Field(..., min_length=1, max_length=500, description="Mensaje del cliente")

    @validator('nombre_completo')
    def validate_nombre_completo(cls, v):
        if not re.match(r'^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s\-\'\.]+$', v.strip()):
            raise ValueError('El nombre solo puede contener letras, espacios, guiones y apóstrofes')

        palabras = v.strip().split()
        if len(palabras) < 2:
            raise ValueError('Debe ingresar nombre y apellido')

        return v.strip().title()

    @validator('telefono')
    def validate_telefono(cls, v):
        telefono_str = str(v)
        if not re.match(r'^\d{7,15}$', telefono_str):
            raise ValueError('El teléfono debe tener entre 7 y 15 dígitos')
        return v

    @validator('mensaje')
    def validate_mensaje(cls, v):
        palabras = len(v.strip().split())
        if palabras > 500:
            raise ValueError('El mensaje no puede exceder las 500 palabras')
        return v.strip()


class FormularioClienteUpdate(BaseModel):
    nombre_completo: Optional[str] = Field(None, min_length=2, max_length=255)
    email: Optional[EmailStr] = None
    telefono: Optional[int] = None
    mensaje: Optional[str] = Field(None, min_length=1, max_length=500)

    @validator('nombre_completo')
    def validate_nombre_completo(cls, v):
        if v is not None:
            if not re.match(r'^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ\s\-\'\.]+$', v.strip()):
                raise ValueError('El nombre solo puede contener letras, espacios, guiones y apóstrofes')

            palabras = v.strip().split()
            if len(palabras) < 2:
                raise ValueError('Debe ingresar nombre y apellido')

            return v.strip().title()
        return v

    @validator('telefono')
    def validate_telefono(cls, v):
        if v is not None:
            telefono_str = str(v)
            if not re.match(r'^\d{7,15}$', telefono_str):
                raise ValueError('El teléfono debe tener entre 7 y 15 dígitos')
        return v

    @validator('mensaje')
    def validate_mensaje(cls, v):
        if v is not None:
            palabras = len(v.strip().split())
            if palabras > 500:
                raise ValueError('El mensaje no puede exceder las 500 palabras')
            return v.strip()
        return v


class FormularioClienteResponse(BaseModel):
    id: str
    nombre_completo: str
    email: str
    telefono: int
    mensaje: str
    created_at: datetime
    updated_at: datetime

class ApiResponse(BaseModel):
    message: list[str]
    data: list[FormularioClienteResponse]  # ✅ Ahora coincide con lo que devuelves
