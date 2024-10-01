import openpyxl
from datetime import datetime

def file_turn_report_excel(path:str, new_path:str, turn:str, data: str):
    '''
    Open file.xlsx  turns day
    
    Args:
        path (str): the path of file to open
        new_path: the new path of file.xlsx to save
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
        sheet = book['Format']        
        
        for i, fila in enumerate(data):
            for j, valor in enumerate(fila):
                sheet.cell(row=i+14, column=j+1, value=valor)        
        
        print("Datos escritos en la hoja con éxito.")
        print (new_path)
        
        book.save(f'{new_path}/Summary_inspection_line_Trad_Repor_turn{turn}.xlsx')
        print("Cambios guardados exitosamente.") 
        
        
        book.close()
    except FileNotFoundError:
        print("El archivo no fue encontrado en la ruta especificada.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        
        

    
import openpyxl
from datetime import datetime

def file_day_summary(path: str, new_path: str, data: list):
    '''
    Open file.xlsx turns day
    
    Args:
        path (str): the path of file to open
        new_path (str): the new path of file.xlsx to save
        data (list): the data set file from sql query
        
    Returns:
        None
        
    Raises:
        Exceptions: If the file is not found at the path or if there is an error in opening the file.
    '''   
    
    today = datetime.now()
    month = today.strftime('%m')
    day = today.strftime('%d')
    name_new_sheet = f"{month}{day}"
    
    try:
        # Open the file
        book = openpyxl.load_workbook(path)
        print("Archivo abierto exitosamente.")
        
        # Find the format page
        sheet = book['Format']
        
        # Create a new sheet
        new_sheet = book.create_sheet(title=name_new_sheet)
        
        # Copy the content and formats from the original sheet to the new sheet
        for row in sheet.iter_rows():
            for cell in row:
                new_cell = new_sheet.cell(row=cell.row, column=cell.column, value=cell.value)
                
                # Copying cell styles safely
                if cell.has_style:
                    new_cell.font = cell.font.copy()
                    new_cell.border = cell.border.copy()
                    new_cell.fill = cell.fill.copy()
                    new_cell.number_format = cell.number_format
                    """ new_cell.alignment = cell.alignment """
        
        # Write data into the new sheet
        for i, fila in enumerate(data):
            for j, valor in enumerate(fila):
                new_sheet.cell(row=i+14, column=j+1, value=valor)     
                
        new_sheet.merge_cells('AJ11:AQ11')
        new_sheet.merge_cells('AR11:AY11')
        new_sheet.merge_cells('BC11:BJ11')
        new_sheet.merge_cells('BL11:BS11')
        
        
        print("Datos escritos en la hoja con éxito.")
        
        # Save the workbook to the new path
        book.save(f"{new_path}/Summary_inspection_line_Trad_Report.xlsx")
        print("Cambios guardados exitosamente.") 
        
        # Close the workbook
        book.close()
    except FileNotFoundError:
        print("El archivo no fue encontrado en la ruta especificada.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

