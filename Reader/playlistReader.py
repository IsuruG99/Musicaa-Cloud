import os


def get_file() -> str:
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'playlist.txt'))
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("")
    return path

def read_file() -> list:
    path = get_file()
    with open(path, "r", encoding="utf-8") as f:
        return f.read().splitlines()

# take a dict, overwrite the file with the dict
def update_playlist(playlist: dict) -> None:
    path = get_file()
    try:
        with open(path, "w", encoding="utf-8") as f:
            for music_file in playlist.keys():
                f.write(music_file + "\n")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
    return
