# Pokedex Ecosystem - Advanced Data Synchronization & Management

Este proyecto es una **adaptación y evolución profesional** de un trabajo grupal realizado originalmente para la asignatura **Análisis y Diseño de Sistemas de Información (ADSI)**. La versión presente en este repositorio ha sido refactorizada para cumplir con estándares de arquitectura limpia y gestión automatizada de datos.

## 🚀 Descripción
Plataforma web desarrollada en **Python/Flask** para la gestión y análisis del ecosistema Pokémon. El sistema destaca por su **arquitectura de datos auto-reparable** sincronizada con la PokeAPI externa.

## 🛠️ Características de Ingeniería
* **Auto-Healable Architecture:** Implementación de un motor de escaneo en el `GestorBD` que verifica la integridad de la base de datos local (SQLite). Si detecta registros incompletos, activa un trabajador de sincronización que consume la **PokeAPI** para hidratar y persistir los datos faltantes automáticamente.
* **Modularidad con Blueprints:** Aplicación estructurada mediante el patrón **Factory** y **Blueprints**, permitiendo el aislamiento total de componentes (Admin, Equipos, Chatbot, Compatibilidad de Tipos).
* **Persistencia Robusta:** Esquema SQL avanzado que gestiona relaciones complejas como cadenas evolutivas y multiplicadores de daño dinámicos por tipo.

## 🏗️ Stack Tecnológico
* **Backend:** Python 3.12 / Flask
* **Persistencia:** SQLite (Sincronización vía pokebase API)
* **Frontend:** Jinja2 templates / CSS3 Custom Properties

## ⚙️ Instalación y Uso

1.  **Preparación del entorno:**
    Crea un entorno virtual e instala las dependencias necesarias:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

2.  **Configuración de Rutas:**
    El sistema utiliza rutas absolutas configuradas en `config.py` para asegurar la portabilidad de la base de datos y los esquemas SQL. Asegúrate de que el archivo `identifier.sqlite` se genere correctamente en la raíz.

3.  **Ejecución del Servidor:**
    Lanza la aplicación ejecutando el script de entrada:
    ```bash
    python run.py
    ```
    El servidor se iniciará por defecto en `http://localhost:1111`.

---

**Nota Académica:** Proyecto desarrollado originalmente por Eneko Rodríguez, Urko Horas, Aimar Larriba, Iván Salazar y Aitor Cotano como parte de la asignatura de Análisis y Diseño de Sistemas de Información en el grado de Ingeniería Informática de Gestión y Sistemas de Información.

## ⚖️ Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
