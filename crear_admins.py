import hashlib
import sqlite3
from config import Config


def crear_admins():
    print(f"--- Conectando a: {Config.DB_PATH} ---")

    # 1. Datos de los 5 administradores (Usuario, Clave, Nombre, Apellido, DNI, Email)
    # El último valor 'ADMIN' se pone fijo en la consulta SQL
    admins = [
        ('erodriguez', 'erodriguez', 'Eneko', 'Rodríguez', '00000000A', 'erodriguez@gmail.com'),
        ('uhoras', 'uhoras', 'Urko', 'Horas', '00000001B', 'uhoras@gmail.com'),
        ('alarriba', 'alarriba', 'Aimar', 'Larriba', '00000002C', 'alarriba@gmail.com'),
        ('acotano', 'acotano', 'Aitor', 'Cotano', '00000003D', 'acotano@gmail.com'),
        ('isalazar', 'isalazar', 'Iván', 'Salazar', '00000004E', 'isalazar@gmail.com'),
        # Cuenta pública para la demo: permite a los visitantes probar el panel de administración
        ('admin', 'admin', 'Demo', 'Admin', '00000005F', 'admin@demo.local')
    ]

    try:
        conn = sqlite3.connect(Config.DB_PATH)
        cursor = conn.cursor()

        # 2. SQL de Inserción forzando el rol 'ADMIN'
        sql = """
              INSERT INTO Users (username, password, name, surname, dni, email, role)
              VALUES (?, ?, ?, ?, ?, ?, 'ADMIN') \
              """

        count = 0
        for admin in admins:
            # El login compara el hash SHA-256 de la contraseña, así que se guarda igual
            username, password, *resto = admin
            hashed_pw = hashlib.sha256(password.encode()).hexdigest()
            try:
                cursor.execute(sql, (username, hashed_pw, *resto))
                print(f"✅ Usuario creado: {admin[0]}")
                count += 1
            except sqlite3.IntegrityError as e:
                print(f"⚠️  Saltado {admin[0]}: Ya existe (Error: {e})")

        conn.commit()
        conn.close()
        print(f"\n--- Proceso terminado. {count} admins nuevos creados. ---")

    except Exception as e:
        print(f"❌ Error general conectando a la BD: {e}")


if __name__ == "__main__":
    crear_admins()