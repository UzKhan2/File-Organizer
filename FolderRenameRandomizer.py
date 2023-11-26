import os
import shutil
import tkinter as tk
from tkinter import filedialog
import uuid

def generate_random_name():
    return str(uuid.uuid4().hex)

def rename_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            try:
                random_name = generate_random_name()
                file_extension = os.path.splitext(filename)[-1].lower()
                new_file_name = os.path.join(folder_path, f"{random_name}{file_extension}")
                shutil.move(os.path.join(folder_path, filename), new_file_name)
                print(f"File renamed successfully: {filename} -> {new_file_name}")

            except Exception as e:
                print(f"Error: {e}")

def main():
    while True:
        folder_path = filedialog.askdirectory(initialdir="C:/")

        if not folder_path:
            print("No folder selected.")
            break

        if os.path.isdir(folder_path):
            rename_files_in_folder(folder_path)
            print(f"Renaming in '{folder_path}' completed.")
        else:
            print(f"'{folder_path}' is not a valid folder.")

if __name__ == '__main__':
    main()