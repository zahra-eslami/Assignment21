import pysynth
import play_wav
# Define the melody for "Twinkle Twinkle Little Star"
song = [
    ('c', 4), ('c', 4), ('g', 4), ('g', 4), ('a', 4), ('a', 4), ('g', 2),
    ('f', 4), ('f', 4), ('e', 4), ('e', 4), ('d', 4), ('d', 4), ('c', 2),
    ('g', 4), ('g', 4), ('f', 4), ('f', 4), ('e', 4), ('e', 4), ('d', 2),
    ('g', 4), ('g', 4), ('f', 4), ('f', 4), ('e', 4), ('e', 4), ('d', 2),
    ('c', 4), ('c', 4), ('g', 4), ('g', 4), ('a', 4), ('a', 4), ('g', 2),
    ('f', 4), ('f', 4), ('e', 4), ('e', 4), ('d', 4), ('d', 4), ('c', 2)
]

# Create the WAV file
pysynth.make_wav(song, fn="twinkle_twinkle.wav")

print("The song has been created successfully!")

song_happy_birthday = [
    ('c', 4), ('c', 4), ('d', 8), ('c', 8), ('f', 8), ('e', 2),
    ('c', 4), ('c', 4), ('d', 8), ('c', 8), ('g', 8), ('f', 2),
    ('c', 4), ('c', 4), ('c5', 8), ('a', 8), ('f', 8), ('e', 8), ('d', 8),
    ('a#', 4), ('a#', 4), ('a', 8), ('f', 8), ('g', 8), ('f', 2)
]

# Create the WAV file for "Happy Birthday"
pysynth.make_wav(song_happy_birthday, fn="happy_birthday.wav")

print("The Happy Birthday song has been created successfully!")

# Define the melody for "Hedwig's Theme"
song_hedwigs_theme = [
    ('b', 4), ('e5', 4), ('g5', 4), ('f#5', 8), ('e5', 8),
    ('b', 4), ('e5', 4), ('g5', 4), ('f#5', 8), ('e5', 8),
    ('d5', 4), ('c#5', 4), ('b4', 4), ('a#4', 8), ('b4', 8),
    ('g4', 4), ('e4', 4), ('a4', 4), ('f#4', 8), ('g4', 8)
]

# Create the WAV file for "Hedwig's Theme"
pysynth.make_wav(song_hedwigs_theme, fn="hedwigs_theme.wav")

print("The Hedwig's Theme song has been created successfully!")


