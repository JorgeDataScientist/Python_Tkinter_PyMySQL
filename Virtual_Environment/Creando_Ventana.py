import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql
import webbrowser


# Crear Funciones
# -------------------------------------------------------------

def insertarDatos():
    """
    Primero, se establece una conexión con la base de datos MySQL local utilizando los parámetros de conexión, como la dirección del host, el nombre de usuario, la contraseña y el nombre de la base de datos.
    """
    try:
        bd = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db='Python_TKinter_PyMySQL'
        )
        """
        A continuación, se crea un objeto cursor que se utiliza para ejecutar consultas SQL en la base de datos.
        """
        cursor = bd.cursor()
        
        """
        Luego se define una consulta SQL que se va a ejecutar para insertar los datos en la tabla. Esta consulta tiene parámetros que se asignarán más adelante en la función.
        """
        sql = "INSERT INTO registro(id, nombre, apellido_paterno, apellido_materno, cedula_identidad, email) VALUES (%s, %s, %s, %s, %s, %s)"
        
        """
        A continuación, se crean una variable llamada valores que contiene los valores de los parámetros que se asignarán en la consulta SQL. Los valores se obtienen de las entradas de usuario id1, nom, apeP, apeM, ci y email respectivamente.
        """
        valores = (id1.get() ,nom.get(), apeP.get(), apeM.get(), ci.get(), email.get())
        
        """
        Luego, se ejecuta la consulta SQL utilizando el método execute() del objeto cursor y se asignan los valores de los parámetros utilizando la variable valores.
        """
        cursor.execute(sql, valores)

        """Después de ejecutar la consulta, se confirma la transacción utilizando el método commit() de la conexión a la base de datos."""
        bd.commit()

        """
        Se eliminan los valores ingresados por el usuario de las entradas de texto nom, apeP, apeM, ci, email e id1.
        """
        nom.delete(0, 'end')
        apeP.delete(0, 'end')
        apeM.delete(0, 'end')
        ci.delete(0, 'end')
        email.delete(0, 'end')
        id1.delete(0, 'end')

        """La función show() es llamada para mostrar los datos de la tabla actualizados."""
        show()

        """
        Se muestra un mensaje de aviso utilizando la biblioteca messagebox para indicar que el registro se ha insertado correctamente.
        """
        messagebox.showinfo(message='Registro Exitoso', title='Aviso')

        """
        Si se produce un error en la ejecución de la consulta SQL, se muestra un mensaje de error utilizando la biblioteca messagebox. La transacción se deshace utilizando el método rollback() de la conexión a la base de datos.
        """
    except pymysql.Error as e:
        messagebox.showinfo(message='Error en la conexión o consulta: {}'.format(str(e)), title='Aviso')
        bd.rollback()

        """
        Por último, se cierra el objeto cursor y la conexión a la base de datos utilizando los métodos close().
        """
    finally:
        cursor.close()
        bd.close()


def eliminar():
    # La función "eliminar" comienza con una declaración condicional "if" que utiliza la función "messagebox.askyesno". Esta función muestra una ventana de diálogo que pregunta al usuario si está seguro de que desea eliminar el registro. Si el usuario hace clic en "sí", la función continúa con el proceso de eliminación. Si el usuario hace clic en "no", la función simplemente termina sin hacer nada.
    if messagebox.askyesno("Confirmar eliminación", "¿Está seguro que desea eliminar el registro?"):
        try:
            bd = pymysql.connect(
                host='localhost',
                user='root',
                passwd='',
                db='Python_TKinter_PyMySQL'
            )
            """
            A continuación, se crea un objeto cursor que se utiliza para ejecutar consultas SQL en la base de datos.
            """
            cursor = bd.cursor()

            # Consulta SQL con parámetros
            sql = "DELETE FROM registro WHERE id=%s"

            # Ejecución segura de la consulta
            cursor.execute(sql, (id1.get(),))
            bd.commit()
            nom.delete(0, 'end')
            apeP.delete(0, 'end')
            apeM.delete(0, 'end')
            ci.delete(0, 'end')
            email.delete(0, 'end')
            id1.delete(0, 'end')
            show()
            messagebox.showinfo(message='Se Elimino el Registro', title='Aviso')
        except pymysql.Error as e:
            # Mensaje de error en caso de fallo en la conexión o ejecución de la consulta
            messagebox.showinfo(message='No se Elimino el Registro {}'.format(str(e)), title='Aviso')
            bd.rollback()
        finally:
            cursor.close()
            bd.close()
    else:
        # Acciones a realizar si el usuario decide no eliminar el registro
        pass


def actualizar():
    try:
        bd = pymysql.connect(
            host='localhost',
            user='root',
            passwd='',
            db='Python_TKinter_PyMySQL'
        )
        cursor = bd.cursor()

        # Consulta SQL con parámetros
        sql = "UPDATE registro SET nombre=%s, apellido_paterno=%s, apellido_materno=%s, cedula_identidad=%s, email=%s WHERE id=%s"

        # Ejecución segura de la consulta
        cursor.execute(sql, (nom.get(), apeP.get(), apeM.get(), ci.get(), email.get(), id1.get()))
        bd.commit()
        nom.delete(0, 'end')
        apeP.delete(0, 'end')
        apeM.delete(0, 'end')
        ci.delete(0, 'end')
        email.delete(0, 'end')
        id1.delete(0, 'end')
        show()
        messagebox.showinfo(message='Se actualizó el registro', title='Aviso')
    except pymysql.Error as e:
        # Mensaje de error en caso de fallo en la conexión o ejecución de la consulta
        messagebox.showinfo(message='No se actualizó el registro: {}'.format(str(e)), title='Aviso')
        bd.rollback()
    finally:
        cursor.close()
        bd.close()


def consulta():
    # Primero se comprueba si se ha proporcionado un ID para la consulta a través del objeto id1. Si no se ha proporcionado, se muestra un mensaje de información y se detiene la función. En caso contrario, se continúa con la consulta.
    if(id1.get()==""):
        messagebox.showinfo("Obteniendo Datos de Consulta")
    else:
        try:
            bd = pymysql.connect(
                host='localhost',
                user='root',
                passwd='',
                db='Python_TKinter_PyMySQL'
            )
            cursor = bd.cursor()

            """
            Se eliminan los datos actuales en los campos de entrada nom, apeP, apeM, ci, y email.
            """
            cursor.execute("SELECT * FROM registro WHERE id=%s", (id1.get(),))

            nom.delete(0, 'end')
            apeP.delete(0, 'end')
            apeM.delete(0, 'end')
            ci.delete(0, 'end')
            email.delete(0, 'end')

            """
            Se recupera el primer registro de la consulta utilizando el método fetchone() del cursor. Si se encuentra un registro, se inserta la información correspondiente en los campos de entrada nom, apeP, apeM, ci, y email. En caso contrario, se muestra un mensaje de información indicando que no se encontró ningún registro con el ID proporcionado.
            """
            row = cursor.fetchone()
            if row:
                nom.insert(0, row[1])
                apeP.insert(0, row[2])
                apeM.insert(0, row[3])
                ci.insert(0, row[4])
                email.insert(0, row[5])
            else:
                messagebox.showinfo("Aviso", "No se encontró ningún registro con ese ID")

            bd.close()

            """
            Si se produce algún error durante la ejecución de la consulta, se muestra un mensaje de error indicando la causa del problema.
            """
        except pymysql.Error as e:
            messagebox.showerror("Error", "Ocurrió un error en la consulta: {}".format(e))


def show():
    bd = pymysql.connect(
        host='localhost',
        user='root',
        passwd='',
        db='Python_TKinter_PyMySQL'
    )
    cursor = bd.cursor()
    cursor.execute("SELECT * FROM registro")

    """
    Se utiliza la función "fetchall" del cursor para obtener todos los registros que cumplen con la consulta SQL.
    """
    rows = cursor.fetchall()

    """
    Se utiliza el método "delete" del objeto "list" para borrar todos los elementos que se encuentren en el listado que se va a mostrar en la interfaz gráfica.
    """
    list.delete(0, list.size())

    """
    Se realiza un ciclo "for" que itera sobre los registros obtenidos en el paso 4. Por cada registro, se genera una cadena de texto con los valores de los campos que se desean mostrar.
    """
    for row in rows:
        insertarDatos = f"{row[0]} {row[1]} {row[2]} {row[3]}"
        """
        Se utiliza el método "insert" del objeto "list" para agregar la cadena de texto generada en el paso anterior al final del listado que se va a mostrar en la interfaz gráfica.
        """
        list.insert(list.size() + 1, insertarDatos)
    """
    Se cierra la conexión a la base de datos mediante el método "close" del objeto "bd".
    """
    bd.close()


def salir():
    ventana.destroy()


def abrir_linkedin(event):
    webbrowser.open_new("https://www.linkedin.com/in/jljorge/")

def cambiar_cursor_a_mano(event):
    event.widget.config(cursor="hand2")

def restaurar_cursor_original(event):
    event.widget.config(cursor="")


# Crear la ventana
# -------------------------------------------------------------
ventana = tk.Tk()
# Agregar título
ventana.title("Formulario de Registro")
# Establecer tamaño de la ventana
ventana.geometry("355x620")
# No permitir cambiar el tamaño de la ventana
ventana.resizable(False, False)
# Color de Fondo
ventana.configure(background="light cyan")

# Cargamos una imagen utilizando el método PhotoImage() y especificando la ruta de la imagen en el argumento file
imagen = tk.PhotoImage(file='../Imagenes/tkinter.png')
# Utilizamos el método subsample() para reducir el tamaño de la imagen por un factor de 6
imagen = imagen.subsample(6, 6)
# Creamos una etiqueta con el método Label() y especificando la imagen en el argumento image y el color de fondo de la imagen
label = tk.Label(image=imagen, bg="light cyan")
# Empaquetamos la etiqueta dentro de la ventana con el método pack()
label.place(x=1, y=1)

# Crear Etiquetas y Cuadros de Textos
# --------------------------------------------------------------
# Insertando etiquetas 'Id'
e0 = tk.Label(ventana, text='Id', bg='gray', fg='white')
e0.place(x=10, y=imagen.height() + 20)
# Cuadro de texto que almacena el 'Id'
id1 = tk.Entry(ventana, width=23)
id1.place(x=10, y=imagen.height() + 50)

# Insertando etiquetas 'Nombre'
e1 = tk.Label(ventana, text='Nombre', bg='gray', fg='white')
e1.place(x=10, y=imagen.height() + 90)
# Cuadro de texto que almacena el 'Nombre'
nom = tk.Entry(ventana, width=23)
nom.place(x=10, y=imagen.height() + 120)

# Insertando etiquetas 'Apellido Paterno'
e2 = tk.Label(ventana, text='Apellido Paterno', bg='gray', fg='white')
e2.place(x=10, y=imagen.height() + 160)
# Cuadro de texto que almacena el 'Apellido Paterno'
apeP = tk.Entry(ventana, width=23)
apeP.place(x=10, y=imagen.height() + 190)

# Insertando etiquetas 'Apellido Materno'
e3 = tk.Label(ventana, text='Apellido Materno', bg='gray', fg='white')
e3.place(x=10, y=imagen.height() + 230)
# Cuadro de texto que almacena el 'Apellido Materno'
apeM = tk.Entry(ventana, width=23)
apeM.place(x=10, y=imagen.height() + 260)

# Insertando etiquetas 'Cedula de Identidad'
e4 = tk.Label(ventana, text='Cedula de Identidad', bg='gray', fg='white')
e4.place(x=10, y=imagen.height() + 300)
# Cuadro de texto que almacena el 'Cedula de Identidad'
ci = tk.Entry(ventana, width=23)
ci.place(x=10, y=imagen.height() + 330)

# Insertando etiquetas 'Email'
e5 = tk.Label(ventana, text='Email', bg='gray', fg='white')
e5.place(x=10, y=imagen.height() + 370)
# Cuadro de texto que almacena el 'Email'
email = tk.Entry(ventana, width=23)
email.place(x=10, y=imagen.height() + 400)

# Crear Botones
# -------------------------------------------------------------
# Insertando Boton 'Registrar'
boton1 = tk.Button(ventana, text='Registrar', fg='Black', width=15, command=insertarDatos)
boton1.place(x=40, y=imagen.height() + 440)

# Insertando Boton 'Consultar'
boton2 = tk.Button(ventana, text='Consultar', fg='Black', width=15, command=consulta)
boton2.place(x=boton1.winfo_x() + boton1.winfo_width() + 180, y=imagen.height() + 440)

# # Insertando Boton 'Actualizar'
boton3 = tk.Button(ventana, text='Actualizar', fg='Black', width=15, command=actualizar)
boton3.place(x=40, y=imagen.height() + 470)

# # Insertando Boton 'Eliminar'
boton4 = tk.Button(ventana, text='Eliminar', fg='Black', width=15, command=eliminar)
boton4.place(x=boton3.winfo_x() + boton3.winfo_width() + 180, y=imagen.height() + 470)

# # Insertando Boton 'Salir'
boton5 = tk.Button(ventana, text='Salir', fg='red', width=15, font=('Arial', 8, 'bold'), command=salir)
boton5.place(x=40, y=imagen.height() + 500)

# # Insertando Boton 'Show'
boton6 = tk.Button(ventana, text='Ver DataBase', fg='blue', width=15, font=('Arial', 8, 'bold'), command=show)
boton6.place(x=boton5.winfo_x() + boton5.winfo_width() + 180, y=imagen.height() + 500)

# Asignamos la función abrir_linkedin al evento de clic en la etiqueta
label.bind("<Button-1>", abrir_linkedin)
# Asignamos la función cambiar_cursor_a_mano al evento de entrada del ratón en la etiqueta
label.bind("<Enter>", cambiar_cursor_a_mano)
# Asignamos la función restaurar_cursor_original al evento de salida del ratón de la etiqueta
label.bind("<Leave>", restaurar_cursor_original)


# Crear Lista
# -------------------------------------------------------------
list = Listbox(ventana)
list.configure(width=30, height=25)
list.place(x=160, y=100)

# -------------------------------------------------------------
# Ejecutar el bucle principal de eventos
ventana.mainloop()
