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

One limitation of my recommender is that the dataset only contains 18 songs, so some genres have more representation than others. For example, lofi appears three times while pop appears twice, which can make it easier for the system to find lofi matches. Another limitation is that energy is worth 4 out of the 8 possible points in the experimental scoring system, so it can have more influence than genre and mood combined. The system also does not subtract points when a song has the wrong mood or genre, which can allow songs with mismatched preferences to receive relatively high scores. Finally, danceability and acousticness are included in the dataset but are not currently used in the scoring calculations.

## Evaluation

### User Profiles Tested

I tested my recommender using four different user profiles:

1. **High-Energy Pop:** Pop, happy mood, high energy, positive valence, and fast tempo.
2. **Chill Lofi:** Lofi, chill mood, low energy, moderate valence, and slow tempo.
3. **Deep Intense Rock:** Rock, intense mood, high energy, moderate valence, and fast tempo.
4. **Conflicting Preferences:** Rock, relaxed mood, high energy, low valence, and fast tempo.

Each profile was tested against the same dataset of 18 songs.

### Original Recommendation Results

- High-Energy Pop: Sunrise City (6.40/7)
- Chill Lofi: Library Rain (6.60/7)
- Deep Intense Rock: Storm Runner (6.92/7)
- Conflicting Preferences: Storm Runner (5.56/7)

### Comparing User Profiles

**High-Energy Pop vs. Chill Lofi:**

High-Energy Pop recommended Sunrise City, while Chill Lofi recommended Library Rain. This makes sense because the first profile prefers upbeat pop music, while the second prefers slower and calmer lofi music.

**High-Energy Pop vs. Deep Intense Rock:**

High-Energy Pop recommended Sunrise City, while Deep Intense Rock recommended Storm Runner. Both profiles prefer high energy, but their different genre and mood preferences caused different songs to rank first.

**High-Energy Pop vs. Conflicting Preferences:**

Sunrise City ranked first for High-Energy Pop, while Storm Runner ranked first for Conflicting Preferences. The conflicting profile preferred rock and high energy, which helped Storm Runner score well even though its mood did not match.

**Chill Lofi vs. Deep Intense Rock:**

Library Rain ranked first for Chill Lofi, while Storm Runner ranked first for Deep Intense Rock. Their different energy and tempo preferences caused the system to recommend very different songs.

**Chill Lofi vs. Conflicting Preferences:**

Library Rain ranked first for Chill Lofi, while Storm Runner ranked first for Conflicting Preferences. The chill profile preferred low energy and slower music, while the conflicting profile preferred high energy and fast tempo.

**Deep Intense Rock vs. Conflicting Preferences:**

Both profiles recommended Storm Runner first. However, Deep Intense Rock gave it a score of 6.92, compared to 5.56 for Conflicting Preferences. The difference came from the conflicting profile's mood mismatch and lower valence similarity.

### Weight-Shift Experiment

I also tested how changing the scoring weights affected the recommendations.

The original system used:

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

This experiment showed that increasing the importance of energy can make songs from different genres rank higher when their numerical characteristics are similar. It also showed that changing scoring weights does not always change the top recommendation.

### Overall Evaluation

Overall, the recommender successfully produced different recommendations based on different user preferences. The experiments showed that genre, mood, energy, valence, and tempo all influence the final rankings. I also learned that changing the scoring weights can affect recommendations and that a song can still rank highly even when it does not match every user preference. Testing different profiles helped me understand the strengths and weaknesses of my recommendation system.

---

## 7. Evaluation

A basic check is to try different user profiles and confirm that exact genre and mood matches earn their points, songs closer to the numerical targets score higher, and the final list is sorted by score. The number of results should also match the requested `k` value. These checks show whether the scoring and ranking behave as intended, but they do not prove that every recommendation will fit a person's taste.

---

## 8. Future Work

The system could use a larger and more varied song catalog, include more song or user preference features, and add tests for scores and rankings. It could also explain scores more clearly and offer more variety in the final recommendations.

---

## 9. Personal Reflection

This project shows how a recommender turns song details and user preferences into scores and a ranked list. Changing the weights can change which songs appear first. It also shows that a simple scoring rule can be easy to explain while still reflecting the limits and biases of its data.
