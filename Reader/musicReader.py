import json
import os

from Reader import directoryReader

JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'musicFiles.json'))

def load_music_json() -> dict:
    if not os.path.exists(JSON_PATH):
        with open(JSON_PATH, 'w') as f:
            json.dump({}, f)
    with open(JSON_PATH, 'r') as f:
        return json.load(f)

def save_music_json(music_tags: dict) -> None:
    with open(JSON_PATH, 'w') as f:
        json.dump(music_tags, f, indent=4)

def add_tag(music_file: str, tag: str) -> None:
    if not tag or not music_file:
        return
    music_tags = load_music_json()
    music_files = load_music_files()
    if music_file in music_files:
        if tag not in music_tags[music_file]:
            music_tags[music_file].append(tag)
        else:
            music_tags[music_file].remove(tag)
        save_music_json(music_tags)

def remove_tag(music_file: str, tag: str) -> None:
    music_tags = load_music_json()
    if music_file in music_tags and tag in music_tags[music_file]:
        music_tags[music_file].remove(tag)
    save_music_json(music_tags)

def update_music_json(music_files: dict) -> None:
    music_tags = load_music_json()
    for music_file in music_files:
        if music_file not in music_tags:
            music_tags[music_file] = []
    for music_file in list(music_tags.keys()):
        if music_file not in music_files:
            del music_tags[music_file]
    save_music_json(music_tags)

def load_music_files() -> dict:
    music_files = {}
    directories = directoryReader.read_file()
    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(('.mp3', '.wav', '.flac')):
                    music_files[os.path.join(root, file)] = []
    update_music_json(music_files)
    music_tags = load_music_json()
    for music_file in music_files:
        music_files[music_file] = music_tags.get(music_file, [])
    return music_files