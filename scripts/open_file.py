import openpyxl

def open_file_excel(path:str, data: str):
    '''
    Open file.xlsx 
    
    Args:
        rute (str): the path of file to open
        data (str): the data set file from sql query
        
    Returns:
        list: Data of the file  
        
    Raises:
        Exceptions: If the file is not found at the path or If there error in the opening the file
    
    '''
    # define rute
    
    path_file = path
    
    try:
        #open the file
        book = openpyxl.load_workbook(path_file)
        print("Archivo abierto exitosamente.")
        #found pag day report
        pag = book['0913']
        
        for i, fila in enumerate(data):
            for j, valor in enumerate(fila):
                pag.cell(row=i+14, column=j+1, value=valor)        
        
        print("Datos escritos en la hoja con éxito.")
        
        book.save(path_file)
        print("Cambios guardados exitosamente.") 
        
        
        book.close()
    except FileNotFoundError:
        print("El archivo no fue encontrado en la ruta especificada.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        
    
    
    
    
    