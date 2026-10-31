"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        (
            "High-Energy Pop",
            {"genre": "pop", "mood": "happy", "energy": 0.95, "valence": 0.90, "tempo_bpm": 135},
        ),
        (
            "Chill Lofi",
            {"genre": "lofi", "mood": "chill", "energy": 0.25, "valence": 0.45, "tempo_bpm": 75},
        ),
        (
            "Deep Intense Rock",
            {"genre": "rock", "mood": "intense", "energy": 0.90, "valence": 0.45, "tempo_bpm": 150},
        ),
        (
            "Conflicting Preferences",
            {"genre": "rock", "mood": "relaxed", "energy": 0.95, "valence": 0.15, "tempo_bpm": 150},
        ),
    ]

    for profile_name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n{profile_name}")
        print("=" * len(profile_name))
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{rank}. {song['title']} - {song['artist']}")
            print(f"   Score: {score:.2f} / 7.00")
            print(f"   Reasons: {explanation}")
        print()


if __name__ == "__main__":
    main()
