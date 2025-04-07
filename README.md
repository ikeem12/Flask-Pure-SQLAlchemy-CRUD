# Flask-Pure-SQLAlchemy-CRUD

## Descripción
Una aplicación básica de Flask que implementa operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos MySQL utilizando SQLAlchemy puro, sin la extensión Flask-SQLAlchemy. Este proyecto está diseñado para practicar y aprender conceptos fundamentales de SQLAlchemy.

## Características
**Operaciones CRUD**: Rutas para añadir, consultar, actualizar y eliminar usuarios.
**Gestión de sesiones**: Uso de un **context manager** para manejar las sesiones de la base de datos de forma segura.

## Tecnologías
- Python 3
- Flask
- SQLAlchemy
- MySQL
- PyMySQL

## Operaciones CRUD
**Añadir usuario**: Accede a http://localhost:5000/add_users para ver el formulario de creación.
**Consultar usuarios**: Accede a http://localhost:5000/get_users para listar los usuarios.
**Actualizar usuario**: Accede a http://localhost:5000/update_user para modificar un usuario existente.
**Eliminar usuario**: Accede a http://localhost:5000/delete_one_user para eliminar un usuario específico, o a http://localhost:5000/delete_all_users para eliminar todos los usuarios.
