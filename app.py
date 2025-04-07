from flask import  Flask, request
from sqlalchemy import create_engine, Integer, String, select, delete, update
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped
from contextlib import contextmanager

app = Flask(__name__)

engine = create_engine('mysql+pymysql://root:johancar12@localhost:3306/prueba_sqlalchemy', echo=True)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)

Base.metadata.create_all(engine)

@app.route('/')
def index():
    return "Hello, World!"

@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

@app.route('/add_users', methods=['GET','POST'])
def add_user():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        
        with get_session() as session:
            new_user = User(username=username, email=email)
            session.add(new_user)
        return f"User added: {username}!"
    else:
        # Muestra un formulario HTML simple para añadir usuarios
        return '''
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Email: <input type="text" name="email"><br>
            <input type="submit" value="Add User">
        </form>
        '''

@app.route('/get_users')
def get_users():
    with get_session() as session:
        stmt = select(User)
        users = session.execute(stmt).scalars().all()
        users_list = [
            {"username": user.username, "email": user.email}
            for user in users
        ]
    return "<br>".join([f"Username: {u['username']}, Email: {u['email']}" for u in users_list])

@app.route('/delete_all_users')
def delete_all_users():
    with get_session() as session:
        stmt = delete(User)
        session.execute(stmt)
        return "All users deleted!"

@app.route('/delete_one_user', methods=['GET','POST'])
def delete_one_user():
    if request.method == 'POST':
        username = request.form.get('username')
        
        with get_session() as session:
            """
                stmt = select(User).where(User.username == username)
                user = session.execute(stmt).scalar_one_or_none()
                if user:
                    session.delete(user)
                    return f"User {username} deleted!"
                else:
                    return f"User {username} not found!"
            """
            
            # Alternativa usando el método delete directamente, pero permite verificar si ha surtido efecto en una fila
            # en lo personal creo que es mejor esta opcion, ya que no es necesario hacar un consulta adicional a la base de datos para verificar si el usuario existe
            stmt = delete(User).where(User.username == username)
            result = session.execute(stmt)

            # verficar si almenos una fila fue afectada
            if result.rowcount == 0:
                print(result.rowcount)
                return f"User {username} not found!"
            else:
                print(result.rowcount)
                return f"User {username} deleted!"
            

            # Alternativa usando el método delete directamente, pero no permite verificar si el usuario existe
            """
                session.execute(delete(User).where(User.username == username))
                return f"User {username} deleted!"
            """
    else:
        # Muestra un formulario HTML simple para eliminar usuario
        return '''
        <form method="POST">
            Username: <input type="text" name="username"><br>
            <input type="submit" value="Delete User">
        </form>
        '''

@app.route('/update_user', methods=['GET','POST'])
def update_user():
    if request.method == 'POST':
        username = request.form.get('username')
        new_username = request.form.get('new_username')
        new_email = request.form.get('new_email')

        with get_session() as session:
            # stmt = select(User).where(User.username == username)
            # user = session.execute(stmt).scalar_one_or_none()
            # if user:
                    
            #     return f"User {username} updated!"
            # else:
            #     return f"User {username} not found!"

            stmt = update(User).where(User.username == username).values(username=new_username, email=new_email)
            result = session.execute(stmt)

            if result.rowcount == 0:
                return f"User {username} not found!"
            else:
                return f"User {username} updated!"
    else:
        # Muestra un formulario HTML simple para actualizar usuario
        return '''
        <form method="POST">
            Username: <input type="text" name="username"><br>
            New Username: <input type="text" name="new_username"><br>
            New Email: <input type="text" name="new_email"><br>
            <input type="submit" value="Update User">
        </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)