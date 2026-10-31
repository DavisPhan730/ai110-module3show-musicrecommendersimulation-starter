# 🎵 Music Recommender Simulation

## Project Summary

This project is a simple music recommendation system that suggests songs based on a user's personal music preferences. It compares song features such as genre, mood, energy, tempo, and valence to a user's taste profile. Each song receives a score based on how closely it matches the user's preferences. The system then ranks the songs and recommends the three highest-scoring matches.

## How The System Works

My recommender uses content-based filtering to suggest songs based on their musical characteristics. Real-world platforms like Spotify use listening history, likes, skips, and playlists to understand what users enjoy. They can also compare users with similar listening habits. My project focuses on matching song attributes with a user's personal preferences.

### Song Features

Each Song object will contain:

- `id`: Unique song identifier
- `title`: Song title
- `artist`: Artist name
- `genre`: Music category
- `mood`: Emotional feeling of the song
- `energy`: How intense the song feels
- `tempo_bpm`: Speed of the song
- `valence`: How positive or happy the song sounds
- `danceability`: How suitable the song is for dancing
- `acousticness`: How acoustic the song sounds

### UserProfile Features

The recommender will use the following sample user profile:

```python
user_profile = {
    "favorite_genre": "rock",
    "favorite_mood": "intense",
    "target_energy": 0.85,
    "target_tempo_bpm": 140,
    "target_valence": 0.55
}
```

### User Profile Evaluation

The proposed user profile should help distinguish between different musical vibes, such as intense rock and chill lofi. However, genre and mood should not completely determine the recommendations. I want the system to consider numerical similarities like energy, tempo, and valence so that songs from different genres can still receive good scores if they have similar characteristics.

### Scoring System

The recommender will use a weighted scoring system with a maximum of 7 points:

- Genre match: 2 points
- Mood match: 1 point
- Energy similarity: 2 points
- Valence similarity: 1 point
- Tempo similarity: 1 point

Genre and mood receive points when they match the user's preferences. Numerical features receive points based on how close they are to the user's preferred values.

For energy and valence, similarity will be calculated using the difference between the song's value and the user's target value.

For tempo, the system will use a 60 BPM tolerance. Songs with values closer to the user's preferences will receive higher scores.

This approach allows songs from different genres to receive good recommendations if their musical characteristics are similar.

### Algorithm Recipe

The recommendation process will follow these steps:

1. Load the user's preferences.
2. Read the songs from `songs.csv`.
3. Compare each song's genre and mood with the user's preferences.
4. Calculate energy, valence, and tempo similarities.
5. Add the points to calculate each song's total score.
6. Sort all songs from highest score to lowest score.
7. Recommend the top three songs.

### Ranking and Recommendations

After calculating each song's score, the recommender sorts the songs from highest to lowest. It then recommends the top three songs that best match the user's preferences.

Songs will not be excluded simply because their genre or mood does not match. They can still receive high scores if their numerical features are similar to the user's preferences.

### Potential Biases

The system may favor songs with exact genre and mood matches, even when songs from other genres have similar musical characteristics. The small dataset may also limit the variety of recommendations. Additionally, numerical features cannot completely capture a song's meaning, lyrics, or personal significance.

---

## Getting Started

### Setup

1. Create a virtual environment:

```bash
python -m venv .venv
```

2. Activate the virtual environment.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Mac or Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Add an example of your program's output after implementation:

```text
Loaded songs: 18
```text
Loaded songs: 18

Top recommendations
========================================
1. Sunrise City
   Artist: Neon Echo
   Score: 6.87 / 7.00
   Reasons: genre match (+2.0); mood match (+1.0); energy similarity (+2.0); valence similarity (+1.0); tempo similarity (+0.9)

2. Gym Hero
   Artist: Max Pulse
   Score: 5.52 / 7.00
   Reasons: genre match (+2.0); mood mismatch (+0.0); energy similarity (+1.7); valence similarity (+1.0); tempo similarity (+0.8)

3. Rooftop Lights
   Artist: Indigo Parade
   Score: 4.88 / 7.00
   Reasons: genre mismatch (+0.0); mood match (+1.0); energy similarity (+1.9); valence similarity (+1.0); tempo similarity (+1.0)
```
Top recommendations
========================================
1. Sunrise City
   Artist: Neon Echo
   Score: 6.87 / 7.00
   Reasons: genre match (+2.0); mood match (+1.0); energy similarity (+2.0); valence similarity (+1.0); tempo similarity (+0.9)

2. Gym Hero
   Artist: Max Pulse
   Score: 5.52 / 7.00
   Reasons: genre match (+2.0); mood mismatch (+0.0); energy similarity (+1.7); valence similarity (+1.0); tempo similarity (+0.8)

3. Rooftop Lights
   Artist: Indigo Parade
   Score: 4.88 / 7.00
   Reasons: genre mismatch (+0.0); mood match (+1.0); energy similarity (+1.9); valence similarity (+1.0); tempo similarity (+1.0)
```

**Screenshot or video (optional):** Insert a screenshot or demo video link here.

---

## Experiments You Tried

Use this section to document the experiments you ran:

- What happened when you changed the weight on genre?
- What happened when you added tempo or valence to the score?
- How did your system behave for different types of users?

---

## Limitations and Risks

Some limitations of the recommender include:

- It only works with a relatively small song catalog.
- It does not understand lyrics or language.
- It may favor certain genres or moods over others.
- Numerical features cannot fully represent someone's musical taste.
- Recommendations depend on the accuracy of the song data and user preferences.

These limitations will be discussed further in the model card.

---

## Reflection

Read and complete `model_card.md`.

Write 1 to 2 paragraphs about what you learned:

- How recommenders turn data into predictions.
- Where bias or unfairness could show up in recommendation systems.
- How changing scoring weights can affect recommendations.