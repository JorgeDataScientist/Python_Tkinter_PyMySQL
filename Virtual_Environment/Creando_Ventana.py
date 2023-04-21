import tkinter as tk
from tkinter import *
from F_DataBase import insertarDatos as DID


# Crear Funciones
# -------------------------------------------------------------
def salir():
    ventana.destroy()


# Crear la ventana
# -------------------------------------------------------------
ventana = tk.Tk()
# Agregar título
ventana.title("Formulario de Registro")
# Establecer tamaño de la ventana
ventana.geometry("290x620")
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
# Cuadro de texto que almacena el 'Nombre'
ed0 = tk.Entry(ventana, width=23)
ed0.place(x=10, y=imagen.height() + 50)

# Insertando etiquetas 'Nombre'
e1 = tk.Label(ventana, text='Nombre', bg='gray', fg='white')
e1.place(x=10, y=imagen.height() + 90)
# Cuadro de texto que almacena el 'Nombre'
DID.nom = tk.Entry(ventana, width=23)
DID.nom.place(x=10, y=imagen.height() + 120)

# Insertando etiquetas 'Apellido Paterno'
e2 = tk.Label(ventana, text='Apellido Paterno', bg='gray', fg='white')
e2.place(x=10, y=imagen.height() + 160)
# Cuadro de texto que almacena el 'Apellido Paterno'
DID.apeP = tk.Entry(ventana, width=23)
DID.apeP.place(x=10, y=imagen.height() + 190)

# Insertando etiquetas 'Apellido Materno'
e3 = tk.Label(ventana, text='Apellido Materno', bg='gray', fg='white')
e3.place(x=10, y=imagen.height() + 230)
# Cuadro de texto que almacena el 'Apellido Materno'
DID.apepM = tk.Entry(ventana, width=23)
DID.apepM.place(x=10, y=imagen.height() + 260)

# Insertando etiquetas 'Cedula de Identidad'
e3 = tk.Label(ventana, text='Cedula de Identidad', bg='gray', fg='white')
e3.place(x=10, y=imagen.height() + 300)
# Cuadro de texto que almacena el 'Cedula de Identidad'
DID.ci = tk.Entry(ventana, width=23)
DID.ci.place(x=10, y=imagen.height() + 330)

# Insertando etiquetas 'Email'
e3 = tk.Label(ventana, text='Email', bg='gray', fg='white')
e3.place(x=10, y=imagen.height() + 370)
# Cuadro de texto que almacena el 'Email'
DID.email = tk.Entry(ventana, width=23)
DID.email.place(x=10, y=imagen.height() + 400)

# Crear Botones
# -------------------------------------------------------------
# Insertando Boton 'Registrar'
boton1 = tk.Button(ventana, text='Registrar', fg='Black', width=15, command= DID)
boton1.place(x=10, y=imagen.height() + 440)

# Insertando Boton 'Consultar'
boton2 = tk.Button(ventana, text='Consultar', fg='Black', width=15)
boton2.place(x=boton1.winfo_x() + boton1.winfo_width() + 150, y=imagen.height() + 440)

# # Insertando Boton 'Actualizar'
boton3 = tk.Button(ventana, text='Actualizar', fg='Black', width=15)
boton3.place(x=10, y=imagen.height() + 470)

# # Insertando Boton 'Eliminar'
boton4 = tk.Button(ventana, text='Eliminar', fg='Black', width=15)
boton4.place(x=boton3.winfo_x() + boton3.winfo_width() + 150, y=imagen.height() + 470)

# # Insertando Boton 'Salir'
boton5 = tk.Button(ventana, text='Salir', fg='red', width=15, font=('Arial', 8, 'bold'), command=salir)
boton5.place(x=10, y=imagen.height() + 500)

# -------------------------------------------------------------
# Ejecutar el bucle principal de eventos
ventana.mainloop()
