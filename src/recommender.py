import csv
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load song records from a CSV file."""
    path = Path(csv_path)
    if not path.is_absolute():
        path = Path(__file__).resolve().parent.parent / path

    with path.open(newline="", encoding="utf-8") as csv_file:
        songs = []
        for row in csv.DictReader(csv_file):
            row["id"] = int(row["id"])
            row["tempo_bpm"] = int(row["tempo_bpm"])
            for field in ("energy", "valence", "danceability", "acousticness"):
                row[field] = float(row[field])
            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and explain the score."""
    score = 0.0
    reasons = []

    genre = user_prefs.get("genre", user_prefs.get("favorite_genre"))
    if genre is not None:
        if song["genre"].casefold() == genre.casefold():
            score += 2.0
            reasons.append("genre match (+2.0)")
        else:
            reasons.append("genre mismatch (+0.0)")

    mood = user_prefs.get("mood", user_prefs.get("favorite_mood"))
    if mood is not None:
        if song["mood"].casefold() == mood.casefold():
            score += 1.0
            reasons.append("mood match (+1.0)")
        else:
            reasons.append("mood mismatch (+0.0)")

    energy_target = user_prefs.get("energy", user_prefs.get("target_energy"))
    if energy_target is not None:
        energy_points = 2.0 * max(0.0, 1.0 - abs(song["energy"] - energy_target))
        score += energy_points
        reasons.append(f"energy similarity (+{energy_points:.1f})")

    valence_target = user_prefs.get("valence", user_prefs.get("target_valence"))
    if valence_target is not None:
        valence_points = max(0.0, 1.0 - abs(song["valence"] - valence_target))
        score += valence_points
        reasons.append(f"valence similarity (+{valence_points:.1f})")

    tempo_target = user_prefs.get("tempo_bpm", user_prefs.get("target_tempo_bpm"))
    if tempo_target is not None:
        tempo_points = max(0.0, 1.0 - abs(song["tempo_bpm"] - tempo_target) / 60.0)
        score += tempo_points
        reasons.append(f"tempo similarity (+{tempo_points:.1f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 3):
    """Return the top-k songs ranked by preference score with explanations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, reasons))

    ranked_songs = sorted(scored_songs, key=lambda recommendation: recommendation[1], reverse=True)
    return [
        (song, score, "; ".join(reasons))
        for song, score, reasons in ranked_songs[:max(0, k)]
    ]
