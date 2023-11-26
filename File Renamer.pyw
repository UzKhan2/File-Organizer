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
    before_count_base = get_file_count(folder_path)
    before_count_subfolders = 0

    for root, dirs, files in os.walk(folder_path):
        before_count_subfolders += len(files)

        for filename in files:
            try:
                # Generate a random name using uuid
                random_name = generate_random_name()

                # Get the file extension from the original file
                file_extension = os.path.splitext(filename)[-1].lower()

                # Create the destination path with the new random name and original extension
                new_file_name = os.path.join(root, f"{random_name}{file_extension}")

                # Rename the file using shutil.move
                shutil.move(os.path.join(root, filename), new_file_name)

            except Exception as e:
                print(f"Error: {e}")

    after_count_base = get_file_count(folder_path)
    after_count_subfolders = before_count_subfolders
    return (before_count_base, before_count_subfolders), (after_count_base, after_count_subfolders)

def rename_specific_types(folder_path):
    for root, dirs, files in os.walk(folder_path):
        pic_counter = 1
        vid_counter = 1
        for filename in files:
            file_extension = os.path.splitext(filename)[-1].lower()
            if file_extension in {'.jpg', '.png', '.jpeg'}:
                new_filename = os.path.join(root, f"{os.path.basename(root)} pic {pic_counter}{file_extension}")
                pic_counter += 1
            elif file_extension in {'.mp4', '.ts', '.mov'}:
                new_filename = os.path.join(root, f"{os.path.basename(root)} vid {vid_counter}{file_extension}")
                vid_counter += 1
            else:
                continue
            os.rename(os.path.join(root, filename), new_filename)

def select_folder():
    folder_path = filedialog.askdirectory(initialdir="F:/")

    if not folder_path:
        result_label.config(text="No folder selected. Please choose a folder.")
        return

    if os.path.isdir(folder_path):
        (before_count_base, before_count_subfolders), (after_count_base, after_count_subfolders) = rename_files_to_random(folder_path)
        rename_specific_types(folder_path)
        
        result_text = f"Renaming in '{folder_path}' completed.\n" \
		      f"Files before renaming (Base folder): {before_count_base}\n" \
                      f"Files after renaming (Base folder): {after_count_base}\n" \
                      f"Files before renaming (All subfolders): {before_count_subfolders}\n" \
                      f"Files after renaming (All subfolders): {after_count_subfolders}\n" \
                      f"Total files before renaming: {before_count_base + before_count_subfolders}\n" \
                      f"Total files after renaming: {after_count_base + after_count_subfolders}"

        # Check if renaming was successful
        if (before_count_base + before_count_subfolders) == (after_count_base + after_count_subfolders):
            result_text += "\nRename Successful"
            result_label.config(fg="green")
        else:
            result_text += "\nRename Failed"
            result_label.config(fg="red")

        # Store the last three results in a list
        result_history = result_label.cget("text").split("\n")[-7:]
        result_history.append(result_text)

        # Update the result_label with the last three results
        result_label.config(text="\n".join(result_history))
    else:
        result_label.config(text=f"'{folder_path}' is not a valid folder.")

def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    update_mode()

def update_mode():
    global dark_mode
    if dark_mode:
        root.configure(bg=dark_bg)
        select_folder_button.config(bg=dark_bg, fg=dark_fg)
        result_label.config(bg=dark_bg, fg=dark_fg)
        toggle_mode_button.config(text="Light Mode", bg=dark_bg, fg=dark_fg)
        
        # Update color configuration for successful/failed message
        result_history = result_label.cget("text").split("\n")
        if "Rename Successful" in result_history[-1]:
            result_label.config(fg="green")
        elif "Rename Failed" in result_history[-1]:
            result_label.config(fg="red")
    else:
        root.configure(bg=light_bg)
        select_folder_button.config(bg=light_bg, fg=light_fg)
        result_label.config(bg=light_bg, fg=light_fg)
        toggle_mode_button.config(text="Dark Mode", bg=light_bg, fg=light_fg)

        # Update color configuration for successful/failed message
        result_history = result_label.cget("text").split("\n")
        if "Rename Successful" in result_history[-1]:
            result_label.config(fg="green")
        elif "Rename Failed" in result_history[-1]:
            result_label.config(fg="red")

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
toggle_mode_button = tk.Button(root, text="Light Mode", command=toggle_mode, bg=dark_bg, fg=dark_fg)
toggle_mode_button.pack(side=tk.BOTTOM, anchor=tk.SE, padx=10, pady=10)

# Run the Tkinter event loop
# root.attributes('-fullscreen', True)  # Start in fullscreen mode
root.state("zoomed") 
update_mode()
root.mainloop()
