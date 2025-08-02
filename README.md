# API Formulario Cliente

API REST desarrollada con FastAPI para la gestión de formularios de clientes con validaciones de negocio y conexión a PostgreSQL.

## 🚀 Características

- **CRUD completo** para formularios de cliente
- **Validaciones de negocio** robustas
- **Generación automática de UUID** únicos
- **Arquitectura por capas** (Controller → Service → Repository)
- **Documentación automática** con Swagger
- **Manejo de errores** centralizado
- **Logging** configurado
- **Conexión a PostgreSQL** con psycopg2

## 📋 Requisitos

- Python 3.8+
- PostgreSQL 12+
- pip (gestor de paquetes de Python)

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/andrias01/ApiBackPythonWithFast.git
cd ApiBackPythonWithFast
```

### 2. Crear entorno virtual

```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos

Ejecuta el script SQL para crear la tabla:

```sql
-- Conectarse a PostgreSQL y ejecutar:
-- database.sql (ver archivo del proyecto)
```

### 5. Configurar variables de entorno

Edita el archivo `.env` con tus credenciales:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=LocalBaseDatosJava
DB_USER=postgres
DB_PASSWORD=123456
```

## 🏃‍♂️ Ejecución

### Método 1: Ejecutar directamente

```bash
python main.py
```

### Método 2: Usar el script de ejecución

```bash
python run_server.py
```

### Método 3: Usar uvicorn directamente

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

La API estará disponible en: `http://localhost:8000`

## 📚 Documentación

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **Health Check**: `http://localhost:8000/health`

## 🛣️ Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/formulario/create` | Crear nuevo formulario |
| GET | `/formulario/{id}` | Buscar formulario por ID |
| GET | `/formulario/all` | Obtener todos los formularios |
| PUT | `/formulario/{id}` | Actualizar formulario |
| DELETE | `/formulario/{id}` | Eliminar formulario |

## 📄 Estructura de datos

### FormularioClienteCreate (POST)

```json
{
  "nombre_completo": "Juan Carlos Pérez",
  "email": "juan.perez@gmail.com",
  "telefono": 3001234567,
  "mensaje": "Estoy interesado en obtener más información."
}
```

### Respuesta de la API

```json
{
  "message": [
    "Formulario creado satisfactoriamente."
  ],
  "data": [
    {
      "id": "0947276d-7453-4009-adea-ab5b6a7b9b97",
      "nombre_completo": "Juan Carlos Pérez",
      "email": "juan.perez@gmail.com",
      "telefono": 3001234567,
      "mensaje": "Estoy interesado en obtener más información."
    }
  ]
}
```

## ✅ Validaciones de negocio

### Nombre completo
- Mínimo 2 palabras (nombre y apellido)
- Solo letras, espacios, guiones y apostrofes
- Máximo 255 caracteres

### Email
- Formato válido con @ y .
- Validación automática con Pydantic

### Teléfono
- Entre 7 y 15 dígitos
- Solo números
- Acepta teléfonos fijos y celulares

### Mensaje
- Máximo 500 palabras
- No puede estar vacío

## 🧪 Ejemplos de uso

Ejecuta los ejemplos incluidos:

```bash
python test_examples.py
```

### Crear formulario con curl

```bash
curl -X POST "http://localhost:8000/formulario/create" \
     -H "Content-Type: application/json" \
     -d '{
       "nombre_completo": "María González",
       "email": "maria@gmail.com",
       "telefono": 3001234567,
       "mensaje": "Necesito información sobre apartamentos."
     }'
```

### Buscar todos los formularios

```bash
curl -X GET "http://localhost:8000/formulario/all"
```

### Buscar por ID

```bash
curl -X GET "http://localhost:8000/formulario/{id}"
```

### Actualizar formulario

```bash
curl -X PUT "http://localhost:8000/formulario/{id}" \
     -H "Content-Type: application/json" \
     -d '{
       "telefono": 3009876543,
       "mensaje": "Mensaje actualizado"
     }'
```

### Eliminar formulario

```bash
curl -X DELETE "http://localhost:8000/formulario/{id}"
```

## 🏗️ Arquitectura del proyecto

```
├── main.py              # Aplicación principal FastAPI
├── controller.py        # Controladores/Endpoints
├── service.py          # Lógica de negocio
├── repository.py       # Acceso a datos
├── models.py           # Modelos Pydantic
├── database.py         # Configuración de BD
├── requirements.txt    # Dependencias
├── .env               # Variables de entorno
├── run_server.py      # Script de ejecución
├── test_examples.py   # Ejemplos y tests
└── README.md          # Documentación
```

## 🔧 Configuración de desarrollo

### Variables de entorno disponibles

```env
# Base de datos
DB_HOST=localhost
DB_PORT=5432
DB_NAME=LocalBaseDatosJava
DB_USER=postgres
DB_PASSWORD=123456

# Servidor
HOST=0.0.0.0
PORT=8000
DEBUG=True
LOG_LEVEL=INFO
```

## 🐛 Resolución de problemas

### Error de conexión a PostgreSQL

1. Verificar que PostgreSQL esté ejecutándose
2. Verificar credenciales en el archivo `.env`
3. Verificar que la base de datos existe

### Error de dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Error de permisos

En Linux/Mac, asegúrate de tener permisos de ejecución:

```bash
chmod +x run_server.py
```

## 📝 Códigos de respuesta HTTP

- `200 OK`: Operación exitosa
- `201 Created`: Formulario creado exitosamente
- `400 Bad Request`: Datos de entrada inválidos
- `404 Not Found`: Formulario no encontrado
- `422 Unprocessable Entity`: Error de validación
- `500 Internal Server Error`: Error interno del servidor

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

---

**¡Listo para usar! 🎉**

Para cualquier duda o problema, revisa la documentación en `/docs` o crea un issue en el repositorio.