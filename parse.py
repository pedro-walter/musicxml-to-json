import json
import xml.etree.ElementTree as ET

tree = ET.parse('gymnopdie.musicxml')
root = tree.getroot()

notes = root.findall('part/measure/note')

voice_current_beat = [0 for i in range(16)]
music = []

for note in notes:
    voice = int(note.find('voice').text)
    duration = int(note.find('duration').text)
    if note.find('pitch'):
        music.append({
            'beat': voice_current_beat[voice],
            'note': note.find('pitch/octave').text + note.find('pitch/step').text
        })
    voice_current_beat[voice] += duration

music.sort(key=lambda x: x['beat'])

json.dump(music, open('gymnopdie.json', 'w'))