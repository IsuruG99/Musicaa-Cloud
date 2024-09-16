from PyQt5.QtWidgets import QWidget, QListWidget
from Controller import directoryReader

def button_clicked(parent: QWidget, sign: str, qlist: QListWidget) -> None:
    if sign == "+" or sign == "-":
        directoryReader.select_folder(parent, sign, qlist)


def manage_dir_list(dirlist: QListWidget = None) -> None:
    if dirlist is not None:
        directoryReader.list_view(dirlist)