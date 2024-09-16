import json
import os

from Controller import directoryReader

# Path to the JSON file
JSON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'musicFiles.json'))

# Load the JSON file
def load_music_json() -> dict:
    if not os.path.exists(JSON_PATH):
        # Create empty JSON.
        with open(JSON_PATH, 'w') as f:
            json.dump({}, f)
    with open(JSON_PATH, 'r') as f:
        return json.load(f)

# Save the JSON file
def save_music_json(music_tags: dict) -> None:
    with open(JSON_PATH, 'w') as f:
        json.dump(music_tags, f, indent=4)

# Add a tag to a music file
def add_tag(music_file: str, tag: str) -> None:
    music_tags = load_music_json()
    music_files = load_music_files()  # Load the current list of music files
    if music_file in music_files:  # Ensure the music file exists
        if tag not in music_tags[music_file]:
            music_tags[music_file].append(tag)
        save_music_json(music_tags)

# Remove a tag from a music file
def remove_tag(music_file: str, tag: str) -> None:
    music_tags = load_music_json()
    if music_file in music_tags and tag in music_tags[music_file]:
        music_tags[music_file].remove(tag)
    save_music_json(music_tags)

def update_music_json(music_files: dict) -> None:
    music_tags = load_music_json()
    # Ensure all found music files are in the JSON
    for music_file in music_files:
        if music_file not in music_tags:
            music_tags[music_file] = []
    # Remove entries for music files that no longer exist
    for music_file in list(music_tags.keys()):
        if music_file not in music_files:
            del music_tags[music_file]
    save_music_json(music_tags)

def load_music_files() -> dict:
    music_files = {}
    directories = directoryReader.read_file()  # Read directories from musicFolders.txt
    for directory in directories:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(('.mp3', '.wav', '.flac')):  # Music file extensions
                    music_files[os.path.join(root, file)] = []
    update_music_json(music_files)  # Update JSON with found music files
    music_tags = load_music_json()  # Load updated tags
    for music_file in music_files:
        music_files[music_file] = music_tags.get(music_file, [])
    return music_files