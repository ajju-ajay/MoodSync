import json
import random
from pathlib import Path

# Dataset location
DATA_FILE = Path(__file__).parent / "data" / "songs.json"


def load_songs():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def recommend_songs(emotion, language="All"):

    songs = load_songs()
    recommendations = []

    for song in songs:

        if song["emotion"].lower() == emotion.lower():

            if language == "All" or song["language"] == language:
                recommendations.append(song)

    random.shuffle(recommendations)

    return recommendations