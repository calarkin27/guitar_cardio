"""
Script containing drill functions
"""

#create output template
template = {
    'E1': ['E: '],
    'B': ['B: '],
    'G': ['G: '],
    'D': ['D: '],
    'A': ['A: '],
    'E': ['E: '],
}

#define drill functions
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

#list all functions in this file for selection
#can make different lists/"tiers" (e.g. easy, medium, hard) and select from parent file.  This is if you want to do difficulties vice specifically pick drills.
drill_list = [one_note, two_note, onetwothree]
