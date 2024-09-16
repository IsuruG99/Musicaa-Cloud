import os

from PyQt5.QtWidgets import QFileDialog, QWidget, QListWidget


# Get file, create if not existing.
def get_file() -> str:
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'musicFolders.txt'))
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("")
    return path


# Read the file and return the contents.
# File contains a list of URIs. or None.
def read_file() -> list:
    path = get_file()
    with open(path, "r") as f:
        return f.read().splitlines()


# Add a single URI to the file, to last line.
def add_uri(sign: str, uri: str = "") -> bool:
    path = get_file()
    uris = read_file()

    if sign == "+":
        if uri in uris:
            return False
        uris.append(uri)
    elif sign == "-":
        if uris:
            uris.pop()

    with open(path, "w") as f:
        f.writelines(uri + "\n" for uri in uris)
    return True


# Select a folder and add it to the file, then call list_view().
def select_folder(parent: QWidget, sign: str, qlist: QListWidget) -> None:
    if sign == "-":
        add_uri(sign)
    elif sign == "+":
        folder = QFileDialog.getExistingDirectory(parent, "Select Folder")
        if folder and add_uri(sign, folder):
            list_view(qlist)
    else:
        return None
    list_view(qlist)


# Update the list view with the contents of the file.
def list_view(qlist: QListWidget) -> None:
    uris = read_file()
    qlist.clear()
    for uri in uris:
        qlist.addItem(uri)


