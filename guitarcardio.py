"""
Guitar cardio ripoff program.  Enjoy!
"""

from random import choice
import itertools
import scale_pattern_library
import drill_library

#need to create input mechanism/pop-up box to select difficulty, modes, etc.

#define scale
chromatic_notes = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']

# scale = []
key = choice(chromatic_notes)
key_index = chromatic_notes.index(key)

#get information from scale pattern
scale_choice = choice(scale_pattern_library.scale_pattern_list)
# scale_choice = choice(scale_pattern_library.arpeggio_list)         #change this selection to test specific scale patterns vice random via line above
scale_name = scale_choice['scale_name']
scale_construction = scale_choice['scale_construction']

#build scale from notes and scale construction
scale = []
for step in scale_construction:
    scale.append(chromatic_notes[key_index])
    key_index += step
    if key_index >= 12:
        key_index -= 12

#build drill notes using fretboard notes and fret counts
fretboard_notes = {
    'E': {'E': (0,12),'F': (1, 13),'F#/Gb': (2, 14),'G': (3,15),'G#/Ab': (4, 16),'A': (5, 17),'A#/Bb': (6, 18),'B': (7, 19),'C': (8, 8),'C#/Db': (9, 9),'D': (10, 10),'D#/Eb': (11, 11)},
    'A': {'A': (0,12),'A#/Bb': (1, 13),'B': (2, 14),'C': (3,15),'C#/Db': (4, 16),'D': (5, 17),'D#/Eb': (6, 18),'E': (7, 19),'F': (8, 8),'F#/Gb': (9, 9),'G': (10, 10),'G#/Ab': (11, 11)},
    'D': {'D': (0,12),'D#/Eb': (1, 13),'E': (2, 14),'F': (3,15),'F#/Gb': (4, 16),'G': (5, 17),'G#/Ab': (6, 18),'A': (7, 19),'A#/Bb': (8, 8),'B': (9, 9),'C': (10, 10),'C#/Db': (11, 11)},
    'G': {'G': (0,12),'G#/Ab': (1, 13),'A': (2, 14),'A#/Bb': (3,15),'B': (4, 16),'C': (5, 17),'C#/Db': (6, 18),'D': (7, 19),'D#/Eb': (8, 8),'E': (9, 9),'F': (10, 10),'F#/Gb': (11, 11)},
    'B': {'B': (0,12),'C': (1, 13),'C#/Db': (2, 14),'D': (3,15),'D#/Eb': (4, 16),'E': (5, 17),'F': (6, 18),'F#/Gb': (7, 19),'G': (8, 8),'G#/Ab': (9, 9),'A': (10, 10),'A#/Bb': (11, 11)},
    'E1': {'E': (0,12),'F': (1, 13),'F#/Gb': (2, 14),'G': (3,15),'G#/Ab': (4, 16),'A': (5, 17),'A#/Bb': (6, 18),'B': (7, 19),'C': (8, 8),'C#/Db': (9, 9),'D': (10, 10),'D#/Eb': (11, 11)},
    }

#select random from fret patterns in scale_pattern_library
frets = choice(scale_choice['frets'])

drill_notes = []
scale_note = itertools.cycle(scale)
octave_up = False
for string in frets:
    counter = frets[string]
    while counter > 0:
        _ = fretboard_notes[string][next(scale_note)][0]
        if len(drill_notes) >= 1:
            #scenario to account for going below 0th fret, then moving octave higher
            if (_ - drill_notes[-1][1]) > 4:
                octave_up = True
                break
            #scenario to account for above 12th fret vice 0th
            if drill_notes[-1][0] == string and drill_notes[-1][1] > _:
                _ += 12
            #scenario to account for rare scenario where scale ascends and string starts on 12th fret vice 0th
            elif drill_notes[-1][0] != string and _ in (0,1) and drill_notes[-1][1] >= 12:
                print("OH SHIIITTTTTTT")
                _ += 12
        drill_notes.append((string, _))
        counter -= 1
    if octave_up:
        break

#alternate path for moving up an octave
if octave_up:
    print('OCTAVE UP ENGAGED!!!!!!!!!!!!!!!')
    drill_notes = []
    scale_note = itertools.cycle(scale)
    for string in frets:
        counter = frets[string]
        while counter > 0:
            _ = fretboard_notes[string][next(scale_note)][1]
            drill_notes.append((string, _))
            counter -= 1
print(drill_notes)

template, drill_name = choice(drill_library.drill_list)(drill_notes)

#get drill pattern (randomly determined) and populated template from drill_library
tab = ' \n'.join(''.join(template[_]) for _ in template)

output = f'\nEnjoy your guitar cardio workout, brah!\nKey:  {key}  {scale}\nScale Name:  {scale_name}\nDrill: {drill_name}\n{tab}'
print(output)
