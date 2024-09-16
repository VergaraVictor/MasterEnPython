# Importar modulo
import sqlite3

# Conexiòn
conexion = sqlite3.connect('pruebas.db')

# Crear tabla
cursor = conexion.cursor()

# Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo VARCHAR(255), "+
"descripcion text, "+
"precio int(255)"+
")")

# Guardar cambios
conexion.commit()

# Insertar datos
cursor.execute("INSERT INTO productos VALUES (NULL, 'Segundo producto', 'descripción de mi producto', 550)")
conexion.commit()

# Listar datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

for producto in productos:
    print("Titulo: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)

# Cerrar conexión
conexion.close()