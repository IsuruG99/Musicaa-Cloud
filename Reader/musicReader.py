import json
import os
from contextlib import nullcontext

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

def manage_tag(music_file: str, tag: str) -> bool:
    if not tag or not music_file:
        return
    try:
        music_tags = load_music_json()
    except json.decoder.JSONDecodeError:
        return False
    if not load_music_files():
        return False

    music_files = load_music_files()
    if music_file in music_files:
        if tag not in music_tags[music_file]:
            music_tags[music_file].append(tag)
        else:
            music_tags[music_file].remove(tag)
        save_music_json(music_tags)
        return True

def update_music_json(music_files: dict) -> bool:
    try:
        music_tags = load_music_json()
    except json.decoder.JSONDecodeError:
        return False

    for music_file in music_files:
        if music_file not in music_tags:
            music_tags[music_file] = []
    for music_file in list(music_tags.keys()):
        if music_file not in music_files:
            del music_tags[music_file]
    save_music_json(music_tags)
    return True

def load_music_files() -> dict:
    music_files = {}
    directories = directoryReader.read_file()
    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(('.mp3', '.wav', '.flac')):
                    normalized_path = os.path.normpath(os.path.join(root, file))
                    music_files[normalized_path] = []
    if not update_music_json(music_files):
        print("Error updating music files.")
        return music_files
    music_tags = load_music_json()
    for music_file in music_files:
        music_files[music_file] = music_tags.get(music_file, [])
    return music_files