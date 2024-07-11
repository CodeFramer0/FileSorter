import os
import shutil




SOURCE_FOLDER = "sorting"
SORTED_FOLDER = "sorted"

def sort_files(source_folder):
    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)):
            parts = filename.split('_')
            if len(parts) < 2:
                continue  

            file_name = parts[-1]
            directories = parts[:-1]
            
            
            new_directory_path = os.path.join(SORTED_FOLDER, *directories)
            new_file_path = os.path.join(new_directory_path, file_name)
            
            os.makedirs(new_directory_path, exist_ok=True)
            
            shutil.move(os.path.join(source_folder, filename), new_file_path)
            print(f"Moved: {filename} -> {new_file_path}")


if __name__ == '__main__':
    sort_files(SOURCE_FOLDER)
