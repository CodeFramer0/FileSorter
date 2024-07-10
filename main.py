import os
import shutil

def sort_files(source_folder):
    # Пройти по всем файлам в исходной папке
    for filename in os.listdir(source_folder):
        # Проверить, является ли элемент файлом
        if os.path.isfile(os.path.join(source_folder, filename)):
            # Разбить имя файла на части
            parts = filename.split('_')
            if len(parts) < 2:
                continue  # Пропустить файлы, не соответствующие шаблону
            
            # Имя файла и директории
            file_name = parts[-1]
            directories = parts[:-1]
            
            # Создать путь до новой директории
            new_directory_path = os.path.join(sorted_folder, *directories)
            new_file_path = os.path.join(new_directory_path, file_name)
            
            # Создать директорию, если её нет
            os.makedirs(new_directory_path, exist_ok=True)
            
            # Переместить файл в новую директорию
            shutil.move(os.path.join(source_folder, filename), new_file_path)
            print(f"Moved: {filename} -> {new_file_path}")

# Пример использования
source_folder = "sorting"  # Замените на путь к вашей папке для файлов на сортировку
sorted_folder = "sorted" # Замените на путь к вашей папке для отсортированных файлов
sort_files(source_folder)
