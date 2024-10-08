import os
import time

directory = r'ваш/каталог'  # Укажите путь к вашему каталогу

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)  # Формирование полного пути к файлу
        filetime = os.path.getmtime(filepath)  # Получение времени последнего изменения файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)  # Получение размера файла
        parent_dir = os.path.dirname(filepath)  # Получение родительской директории файла

        print(
            f'Обнаружен файл: {file}, Путь: {filepath}'
            f', Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}'
             )