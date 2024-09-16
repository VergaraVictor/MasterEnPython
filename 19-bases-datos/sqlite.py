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

# Cerrar conexión
conexion.close()