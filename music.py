import random

name = input("Enter your name: ")
mood = input("Enter your mood: ").lower()

music = {

    "happy": {
        "artist": "Bollywood Mix",
        "songs": [
            "Kala Chashma",
            "Kar Gayi Chull",
            "Gallan Goodiyaan"
        ]
    },

    "sad": {
        "artist": "Arijit Singh",
        "songs": [
            "Channa Mereya",
            "Agar Tum Saath Ho",
            "Husn"
        ]
    },

    "chill": {
        "artist": "English Chill",
        "songs": [
            "Perfect",
            "Night Changes",
            "Until I Found You"
        ]
    },

    "motivated": {
        "artist": "Imagine Dragons",
        "songs": [
            "Believer",
            "Hall of Fame",
            "Unstoppable"
        ]
    }

}

if mood == "happy":
    print("😊")

elif mood == "sad":
    print("😢")

elif mood == "chill":
    print("😌")

elif mood == "motivated":
    print("🔥")

if mood in music:

    artist = music[mood]["artist"]

    songs = music[mood]["songs"]

    print("\nHello", name)
    print("Your Mood:", mood)
    print("Recommended Artist:", artist)

    print("\nRecommended Songs:")

    for i in range(2):
        print("-", random.choice(songs))

else:
    print("Sorry, mood not found")