""" import pyodbc
 
# Detalles de la conexión
server = 'SRV-SQL.trad.cz,49990'
database = 'TRAD'
username = 'autoconttest'
password = 'Beijer2024'
 
# String de conexión
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
 
# Establecer la conexión
try:
    conn = pyodbc.connect(conn_str)
    print("Succesfully Connection to SQL Server Database")
 
    # Crear un cursor para ejecutar la consulta
    cursor = conn.cursor()
 
    # Consulta SQL para obtener los últimos 10 registros (puedes usar una columna de ID o de fecha para ordenarlos)
    query = "SELECT TOP 10 * FROM dbo.MarkingPPC ORDER BY Created DESC"
    # Ejecutar la consulta
    cursor.execute(query)
 
    # Obtener los resultados
    rows = cursor.fetchall()
 
    # Mostrar los últimos 10 registros
    for row in rows:
        print(row)
 
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()
 
except Exception as e:
    print(f"Error either Database Connection or executing query : {e}") """
    
from datetime import datetime


today = datetime.now()

month = today.strftime('%m')
day = today.strftime('%d')

print(month+day)
