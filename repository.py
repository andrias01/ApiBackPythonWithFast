import uuid
from typing import List, Optional
from datetime import datetime
from database import db_connection
from models import FormularioClienteCreate, FormularioClienteUpdate, FormularioClienteResponse
import logging
import psycopg2.extras

logger = logging.getLogger(__name__)

class FormularioClienteRepository:
    
    def generar_uuid_unico(self) -> str:
        """Genera un UUID único que no exista en la base de datos"""
        with db_connection.get_db_connection() as conn:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            
            max_intentos = 5
            for _ in range(max_intentos):
                nuevo_uuid = str(uuid.uuid4())
                
                cursor.execute(
                    "SELECT COUNT(*) AS total FROM formulario_cliente WHERE id = %s",
                    (nuevo_uuid,)
                )
                
                if cursor.fetchone()["total"] == 0:
                    return nuevo_uuid
            
            raise Exception("No se pudo generar un UUID único después de varios intentos")
    
    def crear_formulario(self, formulario: FormularioClienteCreate) -> FormularioClienteResponse:
        """Crear un nuevo formulario cliente"""
        try:
            with db_connection.get_db_connection() as conn:
                cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
                
                nuevo_id = self.generar_uuid_unico()
                fecha_actual = datetime.now()

                cursor.execute("""
                    INSERT INTO formulario_cliente 
                    (id, nombre_completo, email, telefono, mensaje, created_at, updated_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    RETURNING id, nombre_completo, email, telefono, mensaje, created_at, updated_at
                """, (
                    nuevo_id,
                    formulario.nombre_completo,
                    formulario.email,
                    formulario.telefono,
                    formulario.mensaje,
                    fecha_actual,
                    fecha_actual
                ))
                
                resultado = cursor.fetchone()
                conn.commit()
                
                return FormularioClienteResponse(**resultado)
                
        except Exception as e:
            logger.error(f"Error creando formulario: {e}")
            raise
    
    def buscar_por_id(self, formulario_id: str) -> Optional[FormularioClienteResponse]:
        """Buscar formulario por ID"""
        try:
            with db_connection.get_db_connection() as conn:
                cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
                
                cursor.execute("""
                    SELECT id, nombre_completo, email, telefono, mensaje, created_at, updated_at
                    FROM formulario_cliente
                    WHERE id = %s
                """, (formulario_id,))
                
                resultado = cursor.fetchone()
                
                if resultado:
                    return FormularioClienteResponse(**resultado)
                
                return None
                
        except Exception as e:
            logger.error(f"Error buscando formulario por ID: {e}")
            raise
    
    def buscar_todos(self) -> List[FormularioClienteResponse]:
        """Obtener todos los formularios"""
        try:
            with db_connection.get_db_connection() as conn:
                cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
                
                cursor.execute("""
                    SELECT id, nombre_completo, email, telefono, mensaje, created_at, updated_at
                    FROM formulario_cliente
                    ORDER BY created_at DESC
                """)
                
                resultados = cursor.fetchall()
                
                return [FormularioClienteResponse(**resultado) for resultado in resultados]
                
        except Exception as e:
            logger.error(f"Error obteniendo todos los formularios: {e}")
            raise
    
    def actualizar_formulario(self, formulario_id: str, formulario: FormularioClienteUpdate) -> Optional[FormularioClienteResponse]:
        """Actualizar un formulario existente"""
        try:
            with db_connection.get_db_connection() as conn:
                cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
                
                campos_actualizar = []
                valores = []
                
                if formulario.nombre_completo is not None:
                    campos_actualizar.append("nombre_completo = %s")
                    valores.append(formulario.nombre_completo)
                
                if formulario.email is not None:
                    campos_actualizar.append("email = %s")
                    valores.append(formulario.email)
                
                if formulario.telefono is not None:
                    campos_actualizar.append("telefono = %s")
                    valores.append(formulario.telefono)
                
                if formulario.mensaje is not None:
                    campos_actualizar.append("mensaje = %s")
                    valores.append(formulario.mensaje)

                # Siempre actualizar updated_at
                campos_actualizar.append("updated_at = %s")
                valores.append(datetime.now())
                
                if not campos_actualizar:
                    return self.buscar_por_id(formulario_id)
                
                valores.append(formulario_id)
                
                consulta = f"""
                    UPDATE formulario_cliente 
                    SET {', '.join(campos_actualizar)}
                    WHERE id = %s
                    RETURNING id, nombre_completo, email, telefono, mensaje, created_at, updated_at
                """
                
                cursor.execute(consulta, valores)
                resultado = cursor.fetchone()
                
                if resultado:
                    conn.commit()
                    return FormularioClienteResponse(**resultado)
                
                return None
                
        except Exception as e:
            logger.error(f"Error actualizando formulario: {e}")
            raise
    
    def eliminar_formulario(self, formulario_id: str) -> bool:
        """Eliminar un formulario por ID"""
        try:
            with db_connection.get_db_connection() as conn:
                cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
                
                cursor.execute("""
                    DELETE FROM formulario_cliente
                    WHERE id = %s
                """, (formulario_id,))
                
                filas_afectadas = cursor.rowcount
                conn.commit()
                
                return filas_afectadas > 0
                
        except Exception as e:
            logger.error(f"Error eliminando formulario: {e}")
            raise

# Instancia global del repositorio
formulario_repository = FormularioClienteRepository()
