import pymysql

bd = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    db='Python_TKinter_PyMySQL'
    )

cursor = bd.cursor()

# cursor.execute("DROP TABLE IF EXISTS registro")
cursor.execute("CREATE TABLE registro (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, nombre VARCHAR(50), apellido_paterno VARCHAR(50), apellido_materno VARCHAR(50), cedula_identidad VARCHAR(15), email VARCHAR(100))")