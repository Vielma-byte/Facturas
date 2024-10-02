import psycopg2
import bcrypt


def hash(password):
    password_encoded = password.encode()
    salt = bcrypt.gensalt(15)

    hashed_password = bcrypt.hashpw(password_encoded, salt)

    return hashed_password.decode()


conexion1 = psycopg2.connect(database="usuarios", 
                             user="postgres", 
                             password="Vielma")

cursor1=conexion1.cursor()

sql="insert into users(usuario, contraseña_hash) values (%s,%s)"
datos=("admin2", hash("admin"))
cursor1.execute(sql, datos)

conexion1.commit()
conexion1.close() 

