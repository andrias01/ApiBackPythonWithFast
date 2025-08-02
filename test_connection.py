#!/usr/bin/env python3
import psycopg2
from psycopg2.extras import RealDictCursor
import traceback

def test_database_connection():
    """Probar conexión a la base de datos"""
    try:
        print("🔍 Probando conexión a PostgreSQL...")

        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="LocalBaseDatosJava",
            user="postgres",
            password="123456",
            cursor_factory=RealDictCursor
        )

        cursor = connection.cursor()

        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ Conexión exitosa!")
        print(f"📊 PostgreSQL version: {version[0]}")

        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'formulario_cliente'
            );
        """)
        table_exists = cursor.fetchone()[0]

        if table_exists:
            print("✅ La tabla 'formulario_cliente' existe")
            cursor.execute("SELECT COUNT(*) FROM formulario_cliente;")
            count = cursor.fetchone()[0]
            print(f"📝 Registros en la tabla: {count}")
        else:
            print("❌ La tabla 'formulario_cliente' NO existe")

        connection.close()
        return True

    except psycopg2.OperationalError as e:
        print("❌ Error de conexión:", e)
        traceback.print_exc()
        return False

    except Exception as e:
        print("❌ Error inesperado:", e)
        traceback.print_exc()  # 🔹 Esto muestra la traza completa
        return False

if __name__ == "__main__":
    print("🧪 Test de conexión a PostgreSQL")
    print("=" * 50)
    test_database_connection()
    print("=" * 50)
    print("✅ Test completado")
