import os
import shutil
import tkinter as tk
from tkinter import filedialog
import uuid

def generate_random_name():
    return str(uuid.uuid4().hex)

def rename_and_open_file():
    file_to_rename = filedialog.askopenfilename(title="Select a file to rename")
    if not file_to_rename:
        return

    try:
        random_name = generate_random_name()
        file_extension = os.path.splitext(file_to_rename)[1]
        new_file_name = os.path.join(os.path.dirname(file_to_rename), random_name + file_extension)
        shutil.move(file_to_rename, new_file_name)
        os.startfile(new_file_name)

    except Exception as e:
        print(f"Error: {e}")

root = tk.Tk()
root.title("Random File Renamer and Opener")

button = tk.Button(root, text="Rename and Open File", command=rename_and_open_file)
button.pack(pady=20)

root.mainloop()