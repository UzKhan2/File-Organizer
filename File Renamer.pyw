import os
import shutil
import tkinter as tk
from tkinter import filedialog
import uuid

def generate_random_name():
    return str(uuid.uuid4().hex)

def get_file_count(folder_path):
    return len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

def rename_files_to_random(folder_path):
    before_count = get_file_count(folder_path)

    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            try:
                # Generate a random name using uuid
                random_name = generate_random_name()

                # Get the file extension from the original file
                file_extension = os.path.splitext(filename)[-1].lower()

                # Create the destination path with the new random name and original extension
                new_file_name = os.path.join(folder_path, f"{random_name}{file_extension}")

                # Rename the file using shutil.move
                shutil.move(os.path.join(folder_path, filename), new_file_name)

            except Exception as e:
                print(f"Error: {e}")

    after_count = get_file_count(folder_path)
    return before_count, after_count

def rename_specific_types(folder_path):
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

def select_folder():
    folder_path = filedialog.askdirectory(initialdir="F:/")

    if not folder_path:
        result_label.config(text="No folder selected. Please choose a folder.")
        return

    if os.path.isdir(folder_path):
        before_count, after_count = rename_files_to_random(folder_path)
        rename_specific_types(folder_path)
        result_label.config(text=f"Renaming in '{folder_path}' completed.\n"
                                f"Files before renaming: {before_count}\n"
                                f"Files after renaming: {after_count}")
    else:
        result_label.config(text=f"'{folder_path}' is not a valid folder.")

def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    update_mode()

def update_mode():
    if dark_mode:
        root.configure(bg=dark_bg)
        select_folder_button.configure(bg=dark_bg, fg=dark_fg)
        result_label.configure(bg=dark_bg, fg=dark_fg)
        toggle_mode_button.config(text="Switch to Light Mode", bg=dark_bg, fg=dark_fg)
    else:
        root.configure(bg=light_bg)
        select_folder_button.configure(bg=light_bg, fg=light_fg)
        result_label.configure(bg=light_bg, fg=light_fg)
        toggle_mode_button.config(text="Switch to Dark Mode", bg=light_bg, fg=light_fg)

# Initial mode settings
dark_mode = True
dark_bg = '#2E2E2E'
dark_fg = '#FFFFFF'
light_bg = '#FFFFFF'
light_fg = '#000000'

# GUI setup
root = tk.Tk()
root.title("File Renamer")

def toggle_fullscreen(event=None):
    # Toggle fullscreen mode
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

# Set the minimum size (width, height) of the window
root.minsize(400, 300)

def on_escape(event=None):
    # Exit fullscreen mode on Escape key
    root.attributes('-fullscreen', False)

# Bind the F11 key to toggle fullscreen mode
root.bind('<F11>', toggle_fullscreen)
root.bind('<Escape>', on_escape)

# Select folder button
select_folder_button = tk.Button(root, text="Select Folder", command=select_folder)
select_folder_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Toggle Mode button
toggle_mode_button = tk.Button(root, text="Switch to Light Mode", command=toggle_mode, bg=dark_bg, fg=dark_fg)
toggle_mode_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

# Run the Tkinter event loop
# root.attributes('-fullscreen', True)  # Start in fullscreen mode
root.state("zoomed") 
update_mode()
root.mainloop()
