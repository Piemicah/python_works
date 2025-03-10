import os
import shutil
from ui_organizer import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication, QFileDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys


class Organizer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_setups()
        self.mydir = os.getcwd().replace("\\", "/")
        self.setTitle()
        self.setWindowIcon(QIcon("folderIcon.ico"))

    def ui_setups(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(725, 537)
        self.ui.label.setStyleSheet("font-weight:bold")
        self.ui.btn_dir.clicked.connect(self.select_directory)
        self.ui.btn_organize.clicked.connect(self.organize_handler)

    def setTitle(self):
        self.setWindowTitle(f"FILE ORGANIZER 1.0  path={self.mydir}")

    def select_directory(self):
        self.mydir = (
            QFileDialog.getExistingDirectoryUrl(self, "Select Directory")
            .path()
            .lstrip("/")
        )
        if self.mydir != "":
            self.setTitle()
        while self.is_current():
            QMessageBox.warning(
                self,
                "Directory Warning",
                "You must select a directory other than current",
            )

            self.mydir = (
                QFileDialog.getExistingDirectoryUrl(self, "Select Directory")
                .path()
                .lstrip("/")
            )

    def is_current(self):
        return self.mydir == os.getcwd().replace("\\", "/")

    def organize_handler(self):
        if self.mydir == "":
            self.mydir = os.getcwd().replace("\\", "/")

        if self.is_current():
            QMessageBox.warning(
                self,
                "Directory Warning",
                "You must select a directory other than current",
            )
            return
        files = os.listdir(self.mydir)
        print(files)
        image_formats = ["jpeg", "jpg", "png", "tiff", "tga", "bmp", "webp", "ico"]
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
        doc_formats = ["doc", "docx", "txt", "pdf", "xlsx", "pptx", "epub"]
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
                QMessageBox.critical(self, "Transfer error", str(ex))
                return
        QMessageBox.information(
            self, "Success Info", "Directory Successfully Organized!"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("folderIcon.ico"))
    win = Organizer()
    win.show()
    app.exec()
