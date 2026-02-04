import os
import shutil
import tkinter as tk
from tkinter import messagebox
from datetime import date

class FileCopyCreateDirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Change Save Files for Seemless Mod or Base Game")
        self.root.geometry("400x150")  # Set window size
        self.root.resizable(False, False)  # Prevent resizing

        # Add a label for instructions
        tk.Label(root, text="Picture this ...\nChange Save Files for Seemless Mod or Base Game", font=("Arial", 10)).pack(pady=10)

        tk.Button(root, text="Seemless Mod", command=self.run, font=("Arial", 12), bg="lightblue", fg="black").pack(pady=10)
        tk.Button(root, text="Base Game", command=self.base_game).pack()
        self.file1 = "NR0000.sl2"
        self.file2 = "NR0000.sl2.bak"
        self.mod_save_nb = "NR0000.co2"
        self.mod_save_b = "NR0000.co2.bak"
        self.base_dir = os.getcwd()
        self.new_dir = "BASE_GAME_SAVES"
        self.current_date = str(date.today())

    def base_game(self):
        try:
            os.rename(self.mod_save_nb, self.file1)
            os.rename(self.mod_save_b, self.file2)

            self.root.destroy()  # Close the window after success
        except Exception as e:
            messagebox.showinfo("Class!", "Files are now set for Base Game")

    def run(self):
        target_dir = os.path.join(self.base_dir, self.new_dir)

        try:
            os.makedirs(target_dir, exist_ok=True)


            base = os.path.basename(self.file1)
            name, original_ext = os.path.splitext(base)
            dest = os.path.join(target_dir, name+ "-" + self.current_date + original_ext)
            shutil.copy2(self.file1, dest)
            new_src_name = os.path.join(self.base_dir, self.mod_save_nb)
            os.rename(self.file1, new_src_name)
            

            base = os.path.basename(self.file2)
            name, original_ext = os.path.splitext(base)
            dest = os.path.join(target_dir, name+ "-" + self.current_date + original_ext)
            shutil.copy2(self.file2, dest)
            new_src_name = os.path.join(self.base_dir, self.mod_save_b)
            os.rename(self.file2, new_src_name)

            messagebox.showinfo("Class!", "Files are now set for Seemless Mod")
            self.root.destroy()  # Close the window after success

        except Exception as e:
            messagebox.showerror("Error", "File are already set for Seemless Mod")

if __name__ == "__main__":
    root = tk.Tk()
    FileCopyCreateDirApp(root)
    root.mainloop()
