Parras TODO
Aplicación web para la gestión de tareas pendientes, desarrollada con Django.
Permite crear, listar y administrar tareas asociadas a registros de una API externa.

Características principales
✅ Crear tareas pendientes con título, estado de completado y relación con un registro de API.
✅ Visualizar y listar las tareas existentes.
✅ Validación para garantizar que cada tarea tenga un registro de API asociado.
✅ Compatible con SQLite por defecto.

Requisitos
Python 3.11+

Django 5.2+

SQLite (o cualquier base de datos compatible con Django)

Instalación
Clona el repositorio:

bash
Copiar
Editar
git clone https://github.com/<usuario>/<repositorio>.git
cd <repositorio>
Crea y activa un entorno virtual:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate    # en Linux/Mac
venv\Scripts\activate       # en Windows
Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Aplica migraciones:

bash
Copiar
Editar
python manage.py migrate
Inicia el servidor de desarrollo:

bash
Copiar
Editar
python manage.py runserver
Accede en tu navegador a: http://127.0.0.1:8000/

Uso
Para crear una tarea pendiente, dirígete a /tasks/create/ y llena el formulario.
Recuerda seleccionar o especificar un ID de Api válido, ya que es obligatorio para guardar la tarea.

Estructura básica
tasks/models.py → Modelos para PendingTask y Api.

tasks/views.py → Vistas basadas en clase para listar y crear tareas.

tasks/forms.py → Formulario para crear tareas.

tasks/templates/ → Plantillas HTML para las vistas.

Autor
Desarrollado por Ximena Charleene Rodríguez Cacho.

