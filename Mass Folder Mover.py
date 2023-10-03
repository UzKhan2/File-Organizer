import os
from tkinter import Tk, filedialog
import shutil

def get_folder_path():
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path

def flatten_folder(folder_path):
    file_counts = {}  # Keeps track of duplicate file names

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            src_path = os.path.join(root, file)

            # Handle duplicate names
            if file in file_counts:
                file_counts[file] += 1
                base_name, ext = os.path.splitext(file)
                new_file = f"{base_name} {file_counts[file]}{ext}"
                dest_path = os.path.join(folder_path, new_file)
            else:
                file_counts[file] = 0
                dest_path = os.path.join(folder_path, file.replace('_', ' '))

            shutil.move(src_path, dest_path)

def main():
    folder_path = get_folder_path()
    if folder_path:
        if os.path.isdir(folder_path):
            flatten_folder(folder_path)
            print(f"Flattened contents of '{folder_path}'")
        else:
            print(f"'{folder_path}' is not a valid folder.")
    else:
        print("No folder selected.")

if __name__ == '__main__':
    main()
