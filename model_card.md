# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder: Music Recommender Simulation**

---

## 2. Intended Use

This recommender suggests songs from a small catalog using a user's music preferences. It is designed for classroom exploration, not as a complete music service. It assumes that the selected preferences and song details describe what the user likes.

---

## 3. How the Model Works

The system uses **content-based filtering**. It compares each song's features with a user's preferences and gives the song a score out of 7:

- Genre match: up to 2 points for an exact match.
- Mood match: up to 1 point for an exact match.
- Energy similarity: up to 2 points. Songs with energy closer to the user's target receive more points.
- Valence similarity: up to 1 point. Songs with valence closer to the user's target receive more points.
- Tempo similarity: up to 1 point. Songs closer to the user's target tempo receive more points, using a 60 BPM tolerance.

The system sorts songs from highest score to lowest and returns the top three by default. The program can request a different number with `k`; for example, the current command-line example requests five recommendations.

---

## 4. Data

The catalog contains 18 songs. Each song includes its genre, mood, energy, tempo, valence, danceability, and acousticness. The songs cover several genres and moods, but some styles have only one example. The dataset does not include information such as lyrics, language, release date, or a listener's past behavior.

---

## 5. Strengths

The scoring rule is simple to understand: exact genre and mood matches earn points, and numerical features earn more points when they are closer to the user's targets. It can still recommend a song without an exact genre or mood match if its numerical features are similar. The score makes it easier to compare and rank songs consistently.

---

## 6. Limitations and Bias

The catalog is small and may not represent many genres, moods, or musical cultures. A genre or mood with few songs has less chance to appear in the recommendations. Genre and mood matches can strongly influence the score, while numerical values cannot fully describe how a song feels. The system also does not understand lyrics, personal meaning, or how a user's tastes change over time. Recommendations depend on the accuracy of the song data and the user's selected preferences.

---

## 7. Evaluation

A basic check is to try different user profiles and confirm that exact genre and mood matches earn their points, songs closer to the numerical targets score higher, and the final list is sorted by score. The number of results should also match the requested `k` value. These checks show whether the scoring and ranking behave as intended, but they do not prove that every recommendation will fit a person's taste.

---

## 8. Future Work

The system could use a larger and more varied song catalog, include more song or user preference features, and add tests for scores and rankings. It could also explain scores more clearly and offer more variety in the final recommendations.

---

## 9. Personal Reflection

This project shows how a recommender turns song details and user preferences into scores and a ranked list. Changing the weights can change which songs appear first. It also shows that a simple scoring rule can be easy to explain while still reflecting the limits and biases of its data.
