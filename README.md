# 🎵 Music Recommender Simulation

## Project Summary

This project is a simple music recommendation system that suggests songs based on a user's personal music preferences. It compares song features such as genre, mood, energy, tempo, and valence to a user's taste profile. Each song receives a score based on how closely it matches the user's preferences. The system then ranks the songs and recommends the highest-scoring matches.

## How The System Works

My recommender uses content-based filtering to suggest songs based on their musical characteristics. Real-world platforms like Spotify use listening history, likes, skips, and playlists to understand what users enjoy. They can also compare users with similar listening habits. My project focuses on matching song attributes with a user's personal preferences.

### Song Features

Each Song object contains:

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

The recommender uses the following sample user profile:

```python
user_profile = {
    "favorite_genre": "rock",
    "favorite_mood": "intense",
    "target_energy": 0.85,
    "target_tempo_bpm": 140,
    "target_valence": 0.55
}
```

### Scoring System

The recommender uses a weighted scoring system with a maximum of 7 points:

- Genre match: 2 points
- Mood match: 1 point
- Energy similarity: 2 points
- Valence similarity: 1 point
- Tempo similarity: 1 point

Genre and mood receive points when they match the user's preferences. Numerical features receive points based on how close they are to the user's preferred values.

For energy and valence, similarity is calculated using the difference between the song's value and the user's target value.

For tempo, the system uses a 60 BPM tolerance. Songs with values closer to the user's preferences receive higher scores.

This approach allows songs from different genres to receive good recommendations if their musical characteristics are similar.

### Algorithm Recipe

The recommendation process follows these steps:

1. Load the user's preferences.
2. Read the songs from `songs.csv`.
3. Compare each song's genre and mood with the user's preferences.
4. Calculate energy, valence, and tempo similarities.
5. Add the points to calculate each song's total score.
6. Sort all songs from highest score to lowest score.
7. Return the highest-ranked recommendations.

### Ranking and Recommendations

After calculating each song's score, the recommender sorts the songs from highest to lowest. It then recommends the songs that best match the user's preferences.

Songs are not excluded simply because their genre or mood does not match. They can still receive high scores if their numerical features are similar to the user's preferences.

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

Run the tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

The following is an example of the High-Energy Pop profile using the original 7-point scoring system.

```text
Loaded songs: 18

High-Energy Pop
===============
1. Sunrise City - Neon Echo
   Score: 6.40 / 7.00
   Reasons: genre match (+2.0); mood match (+1.0); energy similarity (+1.7); valence similarity (+0.9); tempo similarity (+0.7)

2. Gym Hero - Max Pulse
   Score: 5.78 / 7.00
   Reasons: genre match (+2.0); mood mismatch (+0.0); energy similarity (+2.0); valence similarity (+0.9); tempo similarity (+0.9)

3. Rooftop Lights - Indigo Parade
   Score: 4.35 / 7.00
   Reasons: genre mismatch (+0.0); mood match (+1.0); energy similarity (+1.6); valence similarity (+0.9); tempo similarity (+0.8)
```

---

## Experiments You Tried

### Experiment 1: Testing Different User Profiles

I tested the recommender using four different user profiles to see how well it responds to different musical preferences.

The four profiles were:

- High-Energy Pop
- Chill Lofi
- Deep Intense Rock
- Conflicting Preferences

Each profile was tested against the same dataset of 18 songs. The recommender returned the top five recommendations for each profile.

### High-Energy Pop Results

```text
High-Energy Pop
===============
1. Sunrise City - Neon Echo
   Score: 7.14 / 8.00

2. Gym Hero - Max Pulse
   Score: 6.74 / 8.00

3. Rooftop Lights - Indigo Parade
   Score: 5.97 / 8.00

4. Neon Fever - The Mirrorballs
   Score: 5.53 / 8.00

5. Storm Runner - Voltline
   Score: 5.14 / 8.00
```

### Chill Lofi Results

```text
Chill Lofi
==========
1. Library Rain - Paper Lanterns
   Score: 7.40 / 8.00

2. Midnight Coding - LoRoom
   Score: 7.16 / 8.00

3. Spacewalk Thoughts - Orbit Bloom
   Score: 6.43 / 8.00

4. Focus Flow - LoRoom
   Score: 6.18 / 8.00

5. Glass Garden - Elian Rowe
   Score: 5.48 / 8.00
```

### Deep Intense Rock Results

```text
Deep Intense Rock
=================
1. Storm Runner - Voltline
   Score: 7.90 / 8.00

2. Gym Hero - Max Pulse
   Score: 6.26 / 8.00

3. Iron Cathedral - Black Meridian
   Score: 5.36 / 8.00

4. Velocity Lines - Phase Circuit
   Score: 5.30 / 8.00

5. Neon Fever - The Mirrorballs
   Score: 5.03 / 8.00
```

### Conflicting Preferences Results

```text
Conflicting Preferences
=======================
1. Storm Runner - Voltline
   Score: 6.48 / 8.00

2. Iron Cathedral - Black Meridian
   Score: 5.54 / 8.00

3. Gym Hero - Max Pulse
   Score: 5.00 / 8.00

4. Velocity Lines - Phase Circuit
   Score: 4.96 / 8.00

5. Neon Fever - The Mirrorballs
   Score: 4.53 / 8.00
```

### Experiment 2: Weight-Shift Experiment

I also tested how changing the scoring weights affected the recommendations.

The original scoring system used:

- Genre: 2 points
- Mood: 1 point
- Energy: 2 points
- Valence: 1 point
- Tempo: 1 point
- Maximum: 7 points

For the experiment, I changed the weights to:

- Genre: 1 point
- Mood: 1 point
- Energy: 4 points
- Valence: 1 point
- Tempo: 1 point
- Maximum: 8 points

The goal was to reduce the importance of genre and make energy similarity more influential.

The results showed that Storm Runner entered the top five for High-Energy Pop, replacing Sol de Verano. For Chill Lofi, Spacewalk Thoughts moved from fourth place to third, passing Focus Flow. However, the rankings for Deep Intense Rock and Conflicting Preferences remained unchanged.

This experiment showed that numerical similarities can become more influential than genre matches when their weights are increased. It also demonstrated that changing weights does not necessarily change every recommendation list.

### Comparing the Two Scoring Systems

| Profile | Original Top Recommendation | Experimental Top Recommendation |
|---|---|---|
| High-Energy Pop | Sunrise City | Sunrise City |
| Chill Lofi | Library Rain | Library Rain |
| Deep Intense Rock | Storm Runner | Storm Runner |
| Conflicting Preferences | Storm Runner | Storm Runner |

The top recommendation stayed the same for all four profiles, but some lower-ranked songs changed positions. This shows that scoring weights can influence the ranking without necessarily changing the overall winner.

### What I Learned From the Experiments

Testing different user profiles showed that the recommender changes its results depending on the user's preferences. High-Energy Pop recommended Sunrise City, while Chill Lofi recommended Library Rain. Deep Intense Rock and Conflicting Preferences both recommended Storm Runner first, although the conflicting profile received a lower score because its mood preference did not match.

One interesting result was that Gym Hero appeared in multiple recommendation lists because of its strong energy and numerical similarities. This shows that the system considers more than just genre when making recommendations.

---

## Limitations and Risks

Some limitations of the recommender include:

- It only works with a relatively small song catalog of 18 songs.
- It does not understand lyrics or language.
- It may favor certain genres or moods over others.
- Numerical features cannot fully represent someone's musical taste.
- Recommendations depend on the accuracy of the song data and user preferences.
- Danceability and acousticness are included in the dataset but are not currently used in the scoring system.
- Exact genre and mood matching does not recognize similarities between related categories.

The weight-shift experiment also showed that increasing energy's importance can cause songs from different genres to rank higher, even when they do not match the user's preferred genre.

---

## Reflection

Through this project, I learned how recommendation systems use data and scoring rules to predict what users might enjoy. I learned that even a simple change in scoring weights can affect the order of recommendations. Testing different profiles helped me understand how genre, mood, energy, valence, and tempo work together to represent someone's musical preferences.

I also learned that recommendation systems can have biases when they rely too heavily on certain features or use a limited dataset. For example, a song can receive a high score even when it does not match the user's preferred genre because its numerical features are similar. Overall, this project helped me understand how recommendation algorithms work and why testing different users and preferences is important.

---

## Model Card

Read and complete `model_card.md` for additional information about the system's algorithm, evaluation, limitations, and potential biases.