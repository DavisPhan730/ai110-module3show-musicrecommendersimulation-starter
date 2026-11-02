# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0** — a simple music recommender.

## 2. Goal / Task

My recommender suggests songs that match a user's music preferences. It compares a user's favorite genre and mood with the features of each song. It also checks how close a song's energy, valence, and tempo are to the user's targets. The goal is to give users a ranked list of songs they might like, with explanations for the scores.

## 3. Data Used

The project uses a CSV catalog of **18 songs**, expanded from the original 10. Each song has an ID, title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The scoring system currently uses genre, mood, energy, tempo, and valence. It does not use danceability or acousticness in the score.

The catalog is small, and some genres have more examples than others. It also has no listening history, skips, likes, or feedback from real users. Because of this, the system cannot know whether someone will actually enjoy a recommendation.

## 4. Algorithm Summary

The system uses **content-based filtering**. It scores every song based on how well its features match the user's preferences.

The final scoring rules are:

- Genre match: up to **2 points**.
- Mood match: up to **1 point**.
- Energy similarity: up to **2 points**.
- Valence similarity: up to **1 point**.
- Tempo similarity: up to **1 point**.

The maximum score is **7 points**. Genre and mood earn points for exact matches. Energy and valence earn more points when the song's values are closer to the user's targets. Tempo is compared using a 60 BPM tolerance. The recommender scores all 18 songs, sorts them from highest to lowest, and returns the requested number of results. The regular demonstration recommends the top three, while my evaluation tested the top five for each profile.

The output also explains each score so a user can see why a song ranked where it did.

## 5. Observed Behavior / Biases

The system worked well for clear preferences. For example, it recommended *Sunrise City* for High-Energy Pop and *Library Rain* for Chill Lofi. But it can recommend a song even when its genre or mood does not match, because the numerical features still earn points.

The small dataset may favor genres with more songs, such as lofi, which has three examples. The system also gives no partial credit to related genres or moods. Finally, it does not understand lyrics or the personal meaning of a song. These limits mean a high score is not a guarantee that a listener will like the music.

## 6. Evaluation Process

I tested four user profiles against all 18 songs and reviewed the top five results for each one:

| Profile | First recommendation | Original score |
|---|---|---|
| High-Energy Pop | Sunrise City | 6.40 / 7 |
| Chill Lofi | Library Rain | 6.60 / 7 |
| Deep Intense Rock | Storm Runner | 6.92 / 7 |
| Conflicting Preferences | Storm Runner | 5.56 / 7 |

### Comparing the Profiles

- **High-Energy Pop vs. Chill Lofi:** Sunrise City was first for pop, while Library Rain was first for lofi. The different energy, tempo, genre, and mood preferences explain the difference.
- **High-Energy Pop vs. Deep Intense Rock:** Both profiles prefer energetic music, but different genres and moods caused Sunrise City and Storm Runner to win.
- **High-Energy Pop vs. Conflicting Preferences:** Sunrise City fits the pop/happy profile, while Storm Runner matches the conflicting profile's rock and high-energy preferences.
- **Chill Lofi vs. Deep Intense Rock:** Library Rain fits calm, slower music, while Storm Runner fits intense, fast music.
- **Chill Lofi vs. Conflicting Preferences:** The low-energy lofi profile and the fast, high-energy conflicting profile produced very different recommendations.
- **Deep Intense Rock vs. Conflicting Preferences:** Storm Runner ranked first for both, but it scored lower for Conflicting Preferences because the requested relaxed mood did not match.

### Weight-Shift Experiment

I also tested what would happen if I changed the weights. I reduced genre from **2 to 1 point** and increased energy from **2 to 4 points**, changing the maximum score from **7 to 8**. Mood, valence, and tempo stayed at 1 point each.

The first-place song stayed the same for all four profiles. However, *Storm Runner* entered the top five for High-Energy Pop, replacing *Sol de Verano*. For Chill Lofi, *Spacewalk Thoughts* moved ahead of *Focus Flow*. This showed me that changing the weights can change the rankings, even when the top song stays the same.

I restored the original **7-point system** after the experiment. The terminal output for the different profiles and the experiment is documented in `README.md`.

## 7. Intended Use and Non-Intended Use

**Intended use:** This system is a classroom project for learning how content-based recommendations work. It can show how changing user preferences and scoring weights affects song rankings. It is also useful for practicing Python, testing, and explaining program output.

**Non-intended use:** It should not be treated as a full replacement for Spotify or another music service. It should not be used to predict someone's real music taste with confidence or make important decisions about artists or listeners. It has too few songs and no real listening feedback for that.

## 8. Ideas for Improvement

1. Add more songs across a wider variety of genres and moods so the recommendations are less limited.
2. Let related genres and moods earn partial credit, and give users more control over which features matter most.
3. Use danceability, acousticness, and real user feedback to make recommendations more personal.

## 9. Personal Reflection

My biggest learning moment was seeing how much the scoring weights affected the recommendations. I thought genre would be the most important part of music recommendations, but changing the energy weight showed me that songs from different genres can still have similar vibes. I was also surprised that such a simple scoring system could produce recommendations that made sense for different users.

GitHub Copilot helped me understand the CSV loading, scoring, ranking, and testing steps. It was useful for explaining code and suggesting changes, but I still had to check the results myself. For example, I had to fix import and folder issues when running the program, and I caught an incorrect explanation about how close two song scores were. This taught me not to assume an AI explanation is right just because it sounds confident. If I kept developing the project, I would add more songs, collect user feedback, and test different scoring approaches to see which recommendations people actually enjoy.
