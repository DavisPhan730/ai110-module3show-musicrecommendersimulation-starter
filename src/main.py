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

    # Starter example profile
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "valence": 0.82,
        "tempo_bpm": 122,
    }

    recommendations = recommend_songs(user_prefs, songs, k=3)

    print("\nTop recommendations")
    print("=" * 40)
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']}")
        print(f"   Artist: {song['artist']}")
        print(f"   Score: {score:.2f} / 7.00")
        print(f"   Reasons: {explanation}")
        print()


if __name__ == "__main__":
    main()
