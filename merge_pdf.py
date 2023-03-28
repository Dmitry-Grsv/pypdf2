"""Скрипт объединения файлов PDF.""" 
import os
from PyPDF2 import PdfWriter

def merge_pdf(path=None, merged_output='merged_output.pdf'):
    """Эта функция производит объединение файлов PDF."""

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
def merge_pdf_in_directory(path=os.getcwd()):
    """Эта функция запрашивает путь к файлам."""

    # Вывод пути по умолчанию, запрос у пользователя на продолжение.  
    print(path)
    agreement = input('Is it a right path? y/n/stop:')
    
    # Проверка ответа пользователя.  
    if agreement == 'n':
        # Запрос пользовательского пути к файлам.  
        path = input('Write directory of files or skip for merging files in current directory:')
        if path:
            path = path + '\\'
        else:
            path = os.getcwd() + '\\'
        # Вызов функции с обновленным пользовательским путем к файлам.  
        merge_pdf_in_directory(path)

    elif agreement == 'y':
        # Запрос имени выходного файла.  
        merged_output = input('Name merged file:') + '.pdf'
        print('Working on it')
        # Вызов функции, объединяющей файлы PDF.  
        merge_pdf(path, merged_output)
         
    elif agreement == 'stop':
        print('See you again!')

if __name__ == '__main__':
    merge_pdf_in_directory()