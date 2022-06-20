from datetime import timedelta
import fractions
import json
from typing import Counter
import xml.etree.ElementTree as ET

import pdb

tree = ET.parse('gymnopdie.musicxml')
root = tree.getroot()

beats_per_measure = int(root.find('part/measure/attributes/time/beats').text)

music = []

seconds_per_beat = fractions.Fraction(1000,1125)

current_measure = 0
last_loop_beat = None

for measure in root.findall('part/measure'):
    voice_current_beat = Counter()
    for note in measure.findall('note'):
        voice = int(note.find('voice').text)
        duration = int(note.find('duration').text)
        if note.find('pitch'):
            is_chord = len(note.findall('chord')) > 0
            if is_chord:
                this_loop_beat = last_loop_beat
            else:
                this_loop_beat = current_measure * beats_per_measure + voice_current_beat[voice]
                last_loop_beat = this_loop_beat
                voice_current_beat[voice] += duration
            to_append = {
                'beat': this_loop_beat,
                'duration': duration,
                'voice': voice,
                'note': note.find('pitch/octave').text + note.find('pitch/step').text,
                'timestamp': timedelta(seconds=float(seconds_per_beat * this_loop_beat)).total_seconds()
            }
            print(to_append)
            music.append(to_append)
        else:
            voice_current_beat[voice] += duration
        ET.dump(note)
        print(voice_current_beat)
    current_measure += 1

music.sort(key=lambda x: x['beat'])
json.dump(music, open('gymnopdie.json', 'w'))