import os
from tkinter import Tk, filedialog

def get_folder_path():
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(initialdir="F:/")
    return folder_path

def rename_files_in_folder(folder_path):
    folder_name = os.path.basename(folder_path)
    pic_counter = 1
    vid_counter = 1
    
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = os.path.splitext(filename)[-1].lower()
            if file_extension in {'.jpg', '.png', '.jpeg'}:
                new_filename = os.path.join(folder_path, f"{folder_name} pic {pic_counter}{file_extension}")
                pic_counter += 1
            elif file_extension in {'.mp4', '.ts', '.mov'}:
                new_filename = os.path.join(folder_path, f"{folder_name} vid {vid_counter}{file_extension}")
                vid_counter += 1
            else:
                continue
            os.rename(os.path.join(folder_path, filename), new_filename)

def main():
    while True:
        folder_path = get_folder_path()

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
