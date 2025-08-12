# Mentorix – Backend de Gestión de Proyectos

Mentorix es una aplicación desarrollada en **Django** que permite gestionar proyectos, tareas, miembros e incidencias (issues) con filtrado por habilidades (skills). Está pensada para empresas que desean optimizar la organización y el seguimiento de su trabajo.

## 🚀 Características
- Gestión de proyectos con información detallada.
- CRUD de tareas con fechas límite, estados y asignación de responsables.
- Administración de miembros con filtrado por habilidades.
- Gestión de incidencias (issues) para seguimiento de problemas.
- API REST documentada con **Django REST Framework**.
- Filtrado y búsqueda avanzada.
- Utiliza **Django REST Framework** para la creación de la API y su documentación.

## 🛠 Tecnologías utilizadas
- **Python 3**
- **Django** (Django REST Framework)
- **SQLite / PostgreSQL**
- **CORS Headers** para integración con frontend.

## 📂 Estructura del proyecto
Mentorix/ <br>
├── 📄 init.py # Inicializa el paquete principal <br>
├── 📄 asgi.py # Configuración ASGI para despliegues asincrónicos <br>
├── 📄 settings.py # Configuración global del proyecto Django <br>
├── 📄 urls.py # Enrutamiento de URLs principal <br>
├── 📄 wsgi.py # Configuración WSGI para el servidor web <br> 

gestor/ <br>
├── 📂 migrations/ # Migraciones de base de datos <br>
│ ├── 📄 init.py # Inicializa el módulo de migraciones <br>
├── 📄 init.py # Inicializa la aplicación 'gestor' <br>
├── 📄 admin.py # Configuración del panel de administración <br>
├── 📄 apps.py # Configuración de la aplicación <br>
├── 📄 models.py # Modelos y estructura de la base de datos <br>
├── 📄 serializers.py # Serializadores para API REST <br>
├── 📄 tests.py # Pruebas unitarias <br>
├── 📄 urls.py # Enrutamiento específico de la app 'gestor' <br>
├── 📄 views.py # Vistas y controladores de la lógica de negocio <br>
