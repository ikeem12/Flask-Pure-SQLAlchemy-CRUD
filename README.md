# Flask-Pure-SQLAlchemy-CRUD

## Descripción
Esta es una aplicación sencilla desarrollada con Flask que lleva a cabo operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos MySQL, utilizando SQLAlchemy puro, sin la ayuda de la extensión Flask-SQLAlchemy. El objetivo de este proyecto es practicar y entender los conceptos básicos de SQLAlchemy.

## Características
**Operaciones CRUD**: Incluye rutas para añadir, consultar, actualizar y eliminar usuarios.
**Gestión de sesiones**: Utiliza un **context manager** que permite manejar las sesiones de la base de datos de manera segura.
**Inicialización Inteligente**: Implementa Dockerize para garantizar que la aplicación solo se inicia cuando la base de datos MySQL está completamente lista para aceptar conexiones.

## Tecnologías
- Python 3
- Flask
- SQLAlchemy
- MySQL
- PyMySQL
- Docker & Dockerize

## Dockerize
La imagen de Docker de la aplicación hace uso de **Dockerize** para asegurarse de que el servicio de MySQL esté en funcionamiento antes de que la aplicación Flask comience. Esto se logra al añadir un comando de espera en el Dockerfile o en el archivo de configuración de Docker Compose, por ejemplo:

```dockerfile
CMD ["dockerize","-wait", "tcp://db:3306", "--timeout", "30s"]
```

## Operaciones CRUD
- **Añadir usuario**: Accede a http://localhost:5000/add_users para ver el formulario de creación.
- **Consultar usuarios**: Accede a http://localhost:5000/get_users para listar los usuarios.
- **Actualizar usuario**: Accede a http://localhost:5000/update_user para modificar un usuario existente.
- **Eliminar usuario**: Accede a http://localhost:5000/delete_one_user para eliminar un usuario específico, o a http://localhost:5000/delete_all_users para eliminar todos los usuarios.