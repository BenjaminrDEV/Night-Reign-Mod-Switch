import os
import shutil
import tkinter as tk
from tkinter import messagebox
from datetime import date


class FileCopyCreateDirApp:
    def __init__(self, root):
        self.root = root
        root.title("Change Save Files for Seemless Mod or Base Game")
        root.geometry("400x150")
        root.resizable(False, False)

        tk.Label(
            root,
            text="Picture this ...\nChange Save Files for Seemless Mod or Base Game",
            font=("Arial", 10),
        ).pack(pady=10)

        tk.Button(root, text="Seemless Mod", command=self.enable_mod,
                  font=("Arial", 12), bg="lightblue").pack(pady=10)

        tk.Button(root, text="Base Game", command=self.enable_base).pack()

        # File names
        self.base_save = "NR0000.sl2"
        self.base_backup = "NR0000.sl2.bak"
        self.mod_save = "NR0000.co2"
        self.mod_backup = "NR0000.co2.bak"

        self.base_dir = os.getcwd()
        self.backup_dir = os.path.join(self.base_dir, "BASE_GAME_SAVES")
        self.today = str(date.today())

    # Helpers

    def _dated_copy(self, filename):
        """Copy file into backup folder with date appended."""
        name, ext = os.path.splitext(filename)
        dest = os.path.join(self.backup_dir, f"{name}-{self.today}{ext}")
        shutil.copy2(filename, dest)

    #Actions

    def enable_base(self):
        """Restore base game saves."""
        try:
            os.rename(self.mod_save, self.base_save)
            os.rename(self.mod_backup, self.base_backup)
            self.root.destroy()
        except Exception:
            messagebox.showinfo("Info", "Files are now set for Base Game")

    def enable_mod(self):
        """Backup base saves and switch to mod saves."""
        try:
            os.makedirs(self.backup_dir, exist_ok=True)

            # Backup current base saves
            self._dated_copy(self.base_save)
            self._dated_copy(self.base_backup)

            # Rename to mod format
            os.rename(self.base_save, self.mod_save)
            os.rename(self.base_backup, self.mod_backup)

            messagebox.showinfo("Info", "Files are now set for Seemless Mod")
            self.root.destroy()

        except Exception:
            messagebox.showerror("Error", "Files are already set for Seemless Mod")

#app entry point

if __name__ == "__main__":
    root = tk.Tk()
    FileCopyCreateDirApp(root)
    root.mainloop()
