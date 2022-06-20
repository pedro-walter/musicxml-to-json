import json
from random import randint

music = json.load(open('gymnopdie.json'))

pitch_numbers = {}
beat_array = []
pitch_array = []
for note in music:
    beat_array.append(note['beat'])
    if not note['pitch'] in pitch_numbers:
        pitch_numbers[note['pitch']] = randint(1, 16)
    pitch_array.append(pitch_numbers[note['pitch']])

output = {
    "c2array": True,
    "size": [
        2,
        len(music),
        1
    ],
    "data": [beat_array, pitch_array]
}

json.dump(output, open('gymnopdie-transformed.json', 'w'))