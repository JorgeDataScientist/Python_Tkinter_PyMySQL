import pymysql
from tkinter import messagebox

def insertarDatos():
    bd = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='Python_TKinter_PyMySQL'
        )

    cursor = bd.cursor()

    sql = f`INSERT INTO registro('nombre', 'apellido_paterno', 'apellido_materno', 'cedula_identidad', 'email') VALUES {nombre}, {apellido_paterno}, {apellido_materno}, {cedula_identidad}, {email}`



    
    try:
        cursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message='Registro Exitoso', title='Aviso')
    except:
        bd.rollback()
        messagebox.showinfo(message='No Registrado', title='Aviso')

    bd.close()

    # cursor.execute("DROP TABLE IF EXISTS registro")
    # cursor.execute("CREATE TABLE registro (id INT PRIMARY KEY, nombre VARCHAR(50), apellido_paterno VARCHAR(50), apellido_materno VARCHAR(50), cedula_identidad VARCHAR(15), email VARCHAR(100))")

    