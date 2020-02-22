"""
Script containing drill functions
"""

#Create output template
template = {
    'E1': ['E: '],
    'B': ['B: '],
    'G': ['G: '],
    'D': ['D: '],
    'A': ['A: '],
    'E': ['E: '],
}

#Define drill functions

#single note drills
def one_note(drill_notes):
    drill_name = "One-Noter"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while drill_notes:
        _ = drill_notes[0][0]
        template[_].append(str(drill_notes[0][1]))
        for item in template:
            if item == _:
                template[item].append('-')
            else:
                template[item].append('-')
                template[item].append('-')
                #add extra hyphen for formatting if double-digits used
                if drill_notes[0][1] > 9:
                    template[item].append('-')
        del drill_notes[0]

    #descending
    while drill_notes_desc:
        _ = drill_notes_desc[0][0]
        template[_].append(str(drill_notes_desc[0][1]))
        for item in template:
            if item == _:
                template[item].append('-')
            else:
                template[item].append('-')
                template[item].append('-')
                #add extra hyphen for formatting if double-digits used
                if drill_notes_desc[0][1] > 9:
                    template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def two_note(drill_notes):
    drill_name = "Two-Noter"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while drill_notes:
        _ = drill_notes[0][0]
        template[_].append(str(drill_notes[0][1]))
        template[_].append('-')
        template[_].append(str(drill_notes[0][1]))
        for item in template:
            if item == _:
                template[item].append('-')
            else:
                for i in range(4):
                    template[item].append('-')
                #add extra hyphen for formatting if double-digits used
                if drill_notes[0][1] > 9:
                    template[item].append('-')
                    template[item].append('-')
        del drill_notes[0]

    #descending
    while drill_notes_desc:
        _ = drill_notes_desc[0][0]
        template[_].append(str(drill_notes_desc[0][1]))
        template[_].append('-')
        template[_].append(str(drill_notes_desc[0][1]))
        for item in template:
            if item == _:
                template[item].append('-')
            else:
                for i in range(4):
                    template[item].append('-')
                #add extra hyphen for formatting if double-digits used
                if drill_notes_desc[0][1] > 9:
                    template[item].append('-')
                    template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def three_note(drill_notes):
    drill_name = "Three-Noter"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while drill_notes:
        _ = drill_notes[0][0]
        template[_].append(str(drill_notes[0][1]))
        template[_].append('-')
        template[_].append(str(drill_notes[0][1]))
        template[_].append('-')
        template[_].append(str(drill_notes[0][1]))
        for item in template:
            if item == _:
                template[item].append('-')
            else:
                for i in range(6):
                    template[item].append('-')
                #add extra hyphen for formatting if double-digits used
                if drill_notes[0][1] > 9:
                    for i in range(3):
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while drill_notes_desc:
        _ = drill_notes_desc[0][0]
        template[_].append(str(drill_notes_desc[0][1]))
        template[_].append('-')
        template[_].append(str(drill_notes_desc[0][1]))
        template[_].append('-')
        template[_].append(str(drill_notes_desc[0][1]))
        for item in template:
            if item == _:
                template[item].append('-')
            else:
                for i in range(6):
                    template[item].append('-')
                #add extra hyphen for formatting if double-digits used
                if drill_notes_desc[0][1] > 9:
                    for i in range(3):
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name

#three note run drills
def onetwothree(drill_notes):
    drill_name = "The Ol' 123"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while len(drill_notes) >= 3:
        for note in drill_notes[:3]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) >= 3:
        for note in drill_notes_desc[:3]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def onetwothree_I(drill_notes):
    drill_name = "123 Pattern I"
    drill_notes_desc = drill_notes.copy()

    #ascending
    while len(drill_notes) >= 3:
        for note in drill_notes[:3]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) >= 3:
        for note in drill_notes_desc[-3:]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[-1]
    return template, drill_name


def onetwothree_II(drill_notes):
    drill_name = "123 Pattern II"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while len(drill_notes) >= 3:
        for note in drill_notes[2::-1]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) >= 3:
        for note in drill_notes_desc[:3]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def onetwothree_III(drill_notes):
    drill_name = "123 Pattern III"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while len(drill_notes) >= 3:
        for note in drill_notes[:3]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]
        for note in drill_notes[2::-1]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) >= 3:
        for note in drill_notes_desc[2::-1]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
        for note in drill_notes_desc[:3]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def onetwothree_IV(drill_notes):
    drill_name = "123 Pattern IV"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while len(drill_notes) >= 3:
        for note in drill_notes[2::-1]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]
        for note in drill_notes[:3]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]
    #descending
    while len(drill_notes_desc) >= 3:
        for note in drill_notes_desc[:3]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
        for note in drill_notes_desc[2::-1]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name



#four note run drills
def onetwothreefour(drill_notes):
    drill_name = "The Ol' 1234"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while len(drill_notes) >= 4:
        for note in drill_notes[:4]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) >= 4:
        for note in drill_notes_desc[:4]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def onetwothreefour_I(drill_notes):
    drill_name = "1234 Pattern I"
    drill_notes_desc = drill_notes.copy()

    #ascending
    while len(drill_notes) >= 4:
        for note in drill_notes[:4]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) >= 4:
        for note in drill_notes_desc[-4:]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[-1]
    return template, drill_name


def onetwothreefour_II(drill_notes):
    drill_name = "1234 Pattern II"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while len(drill_notes) >= 4:
        for note in drill_notes[3::-1]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) >= 4:
        for note in drill_notes_desc[:4]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def onetwothreefour_III(drill_notes):
    drill_name = "1234 Pattern III"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    for i in range(2):
        for note in drill_notes[:4]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]
        for note in drill_notes[3::-1]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    for i in range(2):
        for note in drill_notes_desc[3::-1]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
        for note in drill_notes_desc[:4]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def onetwothreefour_IV(drill_notes):
    drill_name = "1234 Pattern IV"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    for i in range(2):
        for note in drill_notes[3::-1]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]
        for note in drill_notes[:4]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    for i in range(2):
        for note in drill_notes_desc[:4]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
        for note in drill_notes_desc[3::-1]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name



#SECTION TBD
def one_note_skip(drill_notes):
    drill_name = "The Ol' One Note Skipper"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while len(drill_notes) >= 3:
        for note in drill_notes[:3:2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) >= 3:
        for note in drill_notes_desc[:3:2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def two_note_skip(drill_notes):
    drill_name = "Two Note Skip [4ths]"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while len(drill_notes) >= 4:
        for note in drill_notes[:4:3]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) >= 4:
        for note in drill_notes_desc[:4:3]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def three_note_skip(drill_notes):
    drill_name = "Three Note Skip [5ths]"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while len(drill_notes) > 4:
        for note in drill_notes[:5:4]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) > 4:
        for note in drill_notes_desc[:5:4]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def four_note_skip(drill_notes):
    drill_name = "Four Note Skip [6ths]"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while len(drill_notes) > 5:
        for note in drill_notes[:6:5]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) > 5:
        for note in drill_notes_desc[:6:5]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def diatonic_triad(drill_notes):
    drill_name = "Diatonic Triad  ***Only use with diatonic scales. Note if/when each octave root note is played, as pattern may not end on root triad.***"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while len(drill_notes) >= 5:
        for note in drill_notes[:5:2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) >= 5:
        for note in drill_notes_desc[:5:2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def diatonic_triad_II(drill_notes):
    drill_name = "Diatonic Triad II ***Only use with diatonic scales. Note if/when each octave root note is played, as pattern may not end on root triad.***"
    drill_notes_desc = drill_notes.copy()

    #ascending
    while len(drill_notes) >= 5:
        for note in drill_notes[:5:2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) >= 5:
        for note in drill_notes_desc[-5::2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[-1]
    return template, drill_name


def diatonic_triad_III(drill_notes):
    drill_name = "Diatonic Triad III ***Only use with diatonic scales. Note if/when each octave root note is played, as pattern may not end on root triad.***"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while len(drill_notes) > 5:
        for note in drill_notes[5::-2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) > 5:
        for note in drill_notes_desc[:5:2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def diatonic_triad_IV(drill_notes):
    drill_name = "Diatonic Triad IV ***Only use with diatonic scales. Note if/when each octave root note is played, as pattern may not end on root triad.***"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while len(drill_notes) >= 5:
        for note in drill_notes[:5:2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]
        if len(drill_notes) < 5:
            break
        for note in drill_notes[4::-2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) >= 5:
        for note in drill_notes_desc[4::-2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
        if len(drill_notes_desc) < 5:
            break
        for note in drill_notes_desc[:5:2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name


def diatonic_triad_V(drill_notes):
    drill_name = "Diatonic Triad V ***Only use with diatonic scales. Note if/when each octave root note is played, as pattern may not end on root triad.***"
    drill_notes_desc = drill_notes.copy()
    drill_notes_desc.reverse()

    #ascending
    while len(drill_notes) >= 5:
        for note in drill_notes[4::-2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]
        if len(drill_notes) < 5:
            break
        for note in drill_notes[:5:2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes[0]

    #descending
    while len(drill_notes_desc) >= 5:
        for note in drill_notes_desc[:5:2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
        if len(drill_notes_desc) < 5:
            break
        for note in drill_notes_desc[4::-2]:
            _ = note[0]
            template[_].append(str(note[1]))
            for item in template:
                if item == _:
                    template[item].append('-')
                else:
                    template[item].append('-')
                    template[item].append('-')
                    #add extra hyphen for formatting if double-digits used
                    if note[1] > 9:
                        template[item].append('-')
        del drill_notes_desc[0]
    return template, drill_name




#list of all functions in this file available for selection
drill_list = [one_note, two_note, three_note, onetwothree, onetwothree_I, onetwothree_II, onetwothree_III, onetwothree_IV, onetwothreefour, onetwothreefour_I,
                onetwothreefour_II, onetwothreefour_III, one_note_skip, two_note_skip, three_note_skip, four_note_skip, diatonic_triad, diatonic_triad_II,
                diatonic_triad_III, diatonic_triad_IV, diatonic_triad_V]
