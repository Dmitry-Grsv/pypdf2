import os
from PyPDF2 import PdfWriter

def merge_pdf(path=None, merged_output='merged_output.pdf'):
    """Эта функция производит объединение файлов PDF"""

    # Объявили пустой документ.  
    merged_pdf = PdfWriter()

    # Формируем список файлов в заданной директории.  
    list_of_pdf = os.listdir(path)

    # Цикл чтения файлов из списка, добавление к объявленному документу.  
    for pdf_f in list_of_pdf:
        if '.pdf' in pdf_f:
            with open(path+pdf_f, 'rb') as pdf_file:
                merged_pdf.append(fileobj=pdf_file)

    # Запись документа в файл.  
    with open(path+merged_output, 'wb') as output_file:
        merged_pdf.write(output_file)

# Запрос директории, имени выходного файла.  
def merge_pdf_in_directory(path=''):
    """Эта функция запрашивает путь к файлам"""

    print(path)
    agreement = input('Is it a right path? y/n/stop:')
    
    if agreement == 'n':
        path = input('Write directory of files or skip for merging files in current directory:')
        if path:
            path = path + '\\'
        else:
            path = os.getcwd() + '\\'
        merge_pdf_in_directory(path)

    elif agreement == 'y':
        merged_output = input('Name merged file:') + '.pdf'
        merge_pdf(path, merged_output)
        print('Working on it')
    
    elif agreement == 'stop':
        print('See you again!')

merge_pdf_in_directory()