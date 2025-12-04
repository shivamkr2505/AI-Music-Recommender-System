import pandas as pd
import webbrowser

df = pd.read_csv("songs.csv")

def show_available_moods():
    print("\nAvailable moods:")
    moods = list(df["mood"].unique())
    for i, mood in enumerate(moods, 1):
        print(f"{i}. {mood}")
    return moods

def recommend_music(mood_input, mood_list):
    # If user typed a number, convert to mood
    if mood_input.isdigit():
        mood_index = int(mood_input)
        if 1 <= mood_index <= len(mood_list):
            mood = mood_list[mood_index - 1]
        else:
            print("\nInvalid number. Please choose from the list.")
            return
    else:
        mood = mood_input.capitalize()

    if mood not in df["mood"].unique():
        print("\nMood not found. Please choose from the list.")
        return

    print(f"\n🎵 Music Recommendations for mood: {mood}\n")
    results = df[df["mood"] == mood].sample(n=min(5, len(df[df["mood"] == mood])))

    for i, (_, row) in enumerate(results.iterrows(), 1):
        print(f"{i}. {row['song']} by {row['artist']} — Spotify: {row['spotify']}")

    choice = input("\nEnter the number of a song to open on Spotify (or press ENTER to skip): ")

    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(results):
            url = list(results["spotify"])[choice - 1]
            print("Opening Spotify...")
            webbrowser.open(url)
        else:
            print("Invalid choice.")

print("Welcome to AI Music Recommendation System 🎶")
mood_list = show_available_moods()

user_mood = input("\nEnter your mood (name or number): ")

recommend_music(user_mood, mood_list)
