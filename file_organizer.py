import tkinter as tk
from tkinter import messagebox
import os
import shutil
import tkinter.filedialog as dialog


# main class
class Organizer:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("600x400")
        self.root.resizable(False, False)
        self.ui()
        self.mydir = os.getcwd().replace("\\", "/")

    def ui(self):
        self.btn_folder = tk.Button(
            self.root, text="Select a folder", command=self.select_directory
        )
        self.btn_folder.grid(row=0, column=0, pady="80", padx="120")

        self.btn_organize = tk.Button(
            self.root, text="Organize", command=self.organize_handler
        )
        self.btn_organize.grid(row=0, column=1)

    def select_directory(self):
        self.mydir = dialog.askdirectory()
        while self.is_current():
            messagebox.showwarning(
                "Directory Warning", "You must select a directory other than current"
            )
            self.mydir = dialog.askdirectory()

    def is_current(self):
        return self.mydir == os.getcwd().replace("\\", "/")

    def organize_handler(self):
        if self.is_current():
            messagebox.showwarning(
                "Directory Warning", "You must select a directory other than current"
            )
            return
        files = os.listdir(self.mydir)
        image_formats = ["jpeg", "jpg", "png", "tiff", "tga", "bmp"]
        video_formats = [
            "mp4",
            "mkv",
            "avi",
            "wmv",
            "webm",
            "avchd",
            "flv",
            "asf",
            "3gp",
        ]
        doc_formats = ["doc", "docx", "txt", "pdf", "xlsx", "pptx"]
        audio_formats = [
            "mp3",
            "m4a",
            "wav",
            "aiff",
            "ogg",
            "aac",
            "wma",
        ]
        compressed_formats = ["rar", "zip", "tgz", "7z", "arj", "xz", "arc"]

        folder_names = [
            "Images",
            "Videos",
            "Documents",
            "Folders",
            "Others",
            "Music",
            "Compressed",
        ]

        folders = [os.path.join(self.mydir, f) for f in folder_names]

        for folder in folders:
            if not os.path.exists(folder):
                os.mkdir(folder)

        for file in files:
            filepath = f"{self.mydir}/{file}"
            format = file.split(".")[-1]
            try:
                if format.lower() in image_formats:
                    dest = f"{self.mydir}/Images/{file}"
                    shutil.move(filepath, dest)
                if format.lower() in video_formats:
                    dest = f"{self.mydir}/Videos/{file}"
                    shutil.move(filepath, dest)
                if format.lower() in doc_formats:
                    dest = f"{self.mydir}/Documents/{file}"
                    shutil.move(filepath, dest)
                if format.lower() in audio_formats:
                    dest = f"{self.mydir}/Music/{file}"
                    shutil.move(filepath, dest)
                if format.lower() in compressed_formats:
                    dest = f"{self.mydir}/Compressed/{file}"
                    shutil.move(filepath, dest)
                if os.path.isdir(filepath) and file not in folder_names:
                    dest = f"{self.mydir}/Folders/{file}"
                    shutil.move(filepath, dest)
                if os.path.isfile(filepath):
                    dest = f"{self.mydir}/Others/{file}"
                    shutil.move(filepath, dest)
            except Exception as ex:
                messagebox.showerror("transfer error", str(ex))


root = tk.Tk()

app = Organizer(root)
root.mainloop()
