import os
from tkinter import Tk, filedialog

def get_folder_path(starting_path=None):
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(initialdir=starting_path)
    return folder_path

def rename_files(folder_path):
    folder_name = os.path.basename(folder_path)
    pic_counter = 1
    vid_counter = 1
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = os.path.splitext(filename)[-1].lower()
            if file_extension in {'.jpg', '.png'}:
                new_filename = os.path.join(folder_path, f"{folder_name} pic {pic_counter}{file_extension}")
                pic_counter += 1
            elif file_extension in {'.mp4'}:
                new_filename = os.path.join(folder_path, f"{folder_name} vid {vid_counter}{file_extension}")
                vid_counter += 1
            else:
                continue
            os.rename(os.path.join(folder_path, filename), new_filename)

# Example Usage
starting_path = "F:\\"
folder_path = get_folder_path(starting_path)

if folder_path:
    rename_files(folder_path)
else:
    print("No folder selected.")
