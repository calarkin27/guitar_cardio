"""
Library of different scale constructions (including different modes and arpeggiation) and associated fretboard pattern options to choose from.
Based off of the the great Jamey Aebersold Jazz Handbook PDF!

For scale construction, integers represent steps (Whole = 2, Half = 1, Minor 3/pentatonic = 3) and go to octave.  Scale TO THE OCTAVE is driver behind fret counts in "frets".
Eventually MAKE ARPEGGIOS (eg [4,3,4,1])
"""

#Major
ionian = {
    'scale_name' : 'Ionian (Major)',
    'scale_construction' : [2, 2, 1, 2, 2, 2, 1],
    'frets': [
        {'E': 2, 'A': 3,'D': 3},
        {'A': 2,'D': 3,'G': 3},
        {'D': 2,'G': 3,'B': 3},
        {'G': 2,'B': 3,'E1': 3},
        {'E': 1,'A': 3,'D': 3,'G': 1},
        {'A': 1,'D': 3,'G': 3,'B': 1},
        {'D': 1,'G': 3,'B': 3,'E1': 1},
        {'E': 2,'A': 3,'D': 3,'G': 3,'B': 2,'E1': 2},
        {'E': 3,'A': 3,'D': 3,'G': 3,'B': 3},
        {'E': 1,'A': 3,'D': 3,'G': 2,'B': 3,'E1': 3},
        ]
}
lydian = {
    'scale_name' : 'Lydian',
    'scale_construction' : [2, 2, 2, 1, 2, 2, 1],
    'frets': [
        {'E': 2, 'A': 3,'D': 3},
        {'A': 2,'D': 3,'G': 3},
        {'D': 2,'G': 3,'B': 3},
        {'G': 2,'B': 3,'E1': 3},
        {'E': 1,'A': 3,'D': 3,'G': 1},
        {'A': 1,'D': 3,'G': 3,'B': 1},
        {'D': 1,'G': 3,'B': 3,'E1': 1},
        {'E': 2,'A': 3,'D': 3,'G': 2,'B': 3,'E1': 2},
        {'E': 3,'A': 3,'D': 3,'G': 3,'B': 3},
        {'E': 1,'A': 3,'D': 3,'G': 3,'B': 2,'E1': 3},
        ]
}
major_pentatonic = {
    'scale_name' : 'Major Pentatonic',
    'scale_construction' : [2, 2, 3, 2, 3],
    'frets': [
        {'E': 3,'A': 2,'D': 1},
        {'A': 3,'D': 2,'G': 1},
        {'D': 3,'G': 2,'B': 1},
        {'G': 3,'B': 2,'E1': 1},
        {'A': 1,'D': 2,'G': 2,'B': 1},
        {'A': 2,'D': 2,'G': 2},
        {'E': 2,'A': 3,'D': 3,'G': 2,'B': 3,'E1': 2},
        {'E': 2,'A': 2,'D': 2,'G': 2,'B': 2, 'E1': 1},
        {'D': 2,'G': 2,'B': 2},
        ]
}
bebop_major = {
    'scale_name' : 'Bebop Major',
    'scale_construction' : [2, 2, 1, 2, 1, 1, 2, 1],
    'frets': [
        {'E': 2, 'A': 3,'D': 4},
        {'A': 2,'D': 3,'G': 4},
        {'D': 2,'G': 3,'B': 3, 'E1': 1},
        {'G': 2,'B': 3,'E1': 4},
        {'E': 1,'A': 3,'D': 4,'G': 1},
        {'A': 1,'D': 3,'G': 4,'B': 1},
        {'D': 1,'G': 3,'B': 3,'E1': 2},
        {'E': 2,'A': 3,'D': 4,'G': 3,'B': 3,'E1': 2},
        {'E': 3,'A': 4,'D': 3,'G': 3,'B': 3, 'E1': 1},
        {'E': 1,'A': 3,'D': 4,'G': 3,'B': 3,'E1': 3},
        ]
}

#Dominant
mixolydian = {
    'scale_name' : 'Mixolydian (Dominant)',
    'scale_construction' : [2, 2, 1, 2, 2, 1, 2],
    'frets': [
        {'E': 2, 'A': 3,'D': 3},
        {'A': 2,'D': 3,'G': 3},
        {'D': 2,'G': 3,'B': 3},
        {'G': 2,'B': 3,'E1': 3},
        {'E': 1,'A': 3,'D': 3,'G': 1},
        {'A': 1,'D': 3,'G': 3,'B': 1},
        {'D': 1,'G': 3,'B': 3,'E1': 1},
        {'E': 2,'A': 3,'D': 3,'G': 3,'B': 2,'E1': 2},
        {'E': 3,'A': 3,'D': 3,'G': 3,'B': 3},
        {'E': 1,'A': 3,'D': 3,'G': 2,'B': 3,'E1': 3},
        ]
}

superlocrian = {
    'scale_name' : 'Super Locrian (Altered)',
    'scale_construction' : [1, 2, 1, 2, 2, 2, 2],
    'frets': [
        {'E': 3, 'A': 3,'D': 2},
        {'A': 3,'D': 3,'G': 2},
        {'D': 3,'G': 3,'B': 2},
        {'G': 3,'B': 3,'E1': 2},
        {'E': 2,'A': 3,'D': 3},
        {'A': 2,'D': 3,'G': 3},
        {'E': 2,'A': 3,'D': 4,'G': 3,'B': 2,'E1': 1},
        {'E': 3,'A': 3,'D': 3,'G': 3,'B': 2, 'E1': 1},
        {'E': 1,'A': 3,'D': 3,'G': 3,'B': 2,'E1': 3},
        ]
}
bebop_dominant = {
    'scale_name' : 'Bebop Dominant',
    'scale_construction' : [2, 2, 1, 2, 2, 1, 1, 1],
    'frets': [
        {'E': 2, 'A': 3,'D': 4},
        {'A': 2,'D': 3,'G': 4},
        {'D': 2,'G': 3,'B': 3, 'E1': 1},
        {'G': 2,'B': 3,'E1': 4},
        {'E': 1,'A': 3,'D': 3,'G': 2},
        {'A': 1,'D': 3,'G': 3,'B': 2},
        {'D': 1,'G': 3,'B': 2,'E1': 3},
        {'E': 2,'A': 3,'D': 3,'G': 3,'B': 2,'E1': 3},
        {'E': 3,'A': 3,'D': 4,'G': 3,'B': 3, 'E1': 1},
        {'E': 1,'A': 3,'D': 3,'G': 2,'B': 3,'E1': 4},
        ]
}
whole_tone = {
    'scale_name' : 'Bebop Dominant',
    'scale_construction' : [2, 2, 2, 2, 2, 2],
    'frets': [
        {'E': 3, 'A': 3,'D': 1},
        {'E': 2, 'A': 3,'D': 2},
        {'A': 3,'D': 3,'G': 1},
        {'A': 2,'D': 3,'G': 2},
        {'D': 3,'G': 2,'B': 2},
        {'G': 2,'B': 2,'E1': 3},
        {'E': 1,'A': 3,'D': 1,'G': 1},
        {'A': 1,'D': 2,'G': 3,'B': 1},
        {'D': 1,'G': 2,'B': 3,'E1': 1},
        {'E': 2,'A': 3,'D': 3,'G': 2,'B': 3,'E1': 1},
        {'E': 3,'A': 2,'D': 4,'G': 3,'B': 2, 'E1': 1},
        {'E': 1,'A': 3,'D': 2,'G': 3,'B': 2,'E1': 2},
        ]
}

#Minor
dorian = {
    'scale_name' : 'Dorian',
    'scale_construction' : [2, 1, 2, 2, 2, 1, 2],
    'frets': [
        {'E': 3,'A': 2,'D': 3},
        {'A': 3,'D': 2,'G': 3},
        {'D': 3,'G': 2,'B': 3},
        {'G': 3,'B': 2,'E1': 3},
        {'E': 1,'A': 3,'D': 3,'G': 1},
        {'A': 1,'D': 3,'G': 3,'B': 1},
        {'D': 1,'G': 3,'B': 3,'E1': 1},
        {'E': 3,'A': 2,'D': 3,'G': 3,'B': 3,'E1': 1},
        {'E': 3,'A': 3,'D': 3,'G': 3,'B': 2, 'E1':1},
        {'E': 1,'A': 3,'D': 3,'G': 3,'B': 2,'E1': 3}
        ]
}
phrygian = {
    'scale_name' : 'Phrygian',
    'scale_construction' : [1, 2, 2, 2, 1, 2, 2],
    'frets': [
        {'E': 3,'A': 3,'D': 2},
        {'A': 3,'D': 3,'G': 2},
        {'D': 3,'G': 3,'B': 2},
        {'G': 3,'B': 3,'E1': 2},
        {'E': 1,'A': 3,'D': 3,'G': 1},
        {'A': 1,'D': 3,'G': 3,'B': 1},
        {'D': 1,'G': 3,'B': 3,'E1': 1},
        {'E': 3,'A': 3,'D': 3,'G': 3,'B': 3,'E1': 1},
        {'E': 3,'A': 3,'D': 2,'G': 3,'B': 2, 'E1':2},
        {'E': 2,'A': 3,'D': 3,'G': 3,'B': 2,'E1': 2}
        ]
}
aeolian = {
    'scale_name' : 'Aeolian (Natural/Pure Minor)',
    'scale_construction' : [2, 1, 2, 2, 1, 2, 2],
    'frets': [
        {'E': 3,'A': 3,'D': 2},
        {'A': 3,'D': 3,'G': 2},
        {'D': 3,'G': 3,'B': 2},
        {'G': 3,'B': 3,'E1': 2},
        {'E': 1,'A': 3,'D': 3,'G': 1},
        {'A': 1,'D': 3,'G': 3,'B': 1},
        {'D': 1,'G': 3,'B': 3,'E1': 1},
        {'E': 3,'A': 3,'D': 2,'G': 3,'B': 3,'E1': 1},
        {'E': 3,'A': 3,'D': 3,'G': 3,'B': 3},
        {'E': 1,'A': 3,'D': 3,'G': 3,'B': 3,'E1': 3},
        {'E': 2,'A': 3,'D': 3,'G': 3,'B': 2,'E1': 2}
        ]
}
minor_pentatonic = {
    'scale_name' : 'Minor Pentatonic',
    'scale_construction' : [3, 2, 2, 3, 2],
    'frets': [
        {'E': 1,'A': 3,'D': 2},
        {'A': 1,'D': 3,'G': 2},
        {'D': 1,'G': 3,'B': 2},
        {'G': 1,'B': 3,'E1': 2},
        {'A': 1,'D': 2,'G': 2,'B': 1},
        {'A': 2,'D': 2,'G': 2},
        {'E': 1,'A': 2,'D': 2,'G': 2,'B': 2,'E1': 2},
        {'E': 2,'A': 2,'D': 2,'G': 2,'B': 2, 'E1': 1},
        {'D': 2,'G': 2,'B': 2},
        ]
}
melodic_minor = {
    'scale_name' : 'Melodic Minor... Awwww Yeeeaaaaaaahhhh!!!',
    'scale_construction' : [2, 1, 2, 2, 2, 2, 1],
    'frets': [
        {'E': 3,'A': 2,'D': 3},
        {'A': 3,'D': 2,'G': 3},
        {'D': 3,'G': 2,'B': 3},
        {'G': 3,'B': 2,'E1': 3},
        {'E': 1,'A': 3,'D': 3,'G': 1},
        {'A': 1,'D': 3,'G': 3,'B': 1},
        {'D': 1,'G': 3,'B': 2,'E1': 2},
        {'E': 3,'A': 2,'D': 3,'G': 3,'B': 2,'E1': 2},
        {'E': 3,'A': 3,'D': 3,'G': 3,'B': 2, 'E1': 1},
        {'E': 1,'A': 3,'D': 3,'G': 3,'B': 2,'E1': 3},
        ]
}
harmonic_minor = {
    'scale_name' : 'Harmonic Minor',
    'scale_construction' : [2, 1, 2, 2, 1, 3, 2],
    'frets': [
        {'E': 3,'A': 3,'D': 2},
        {'A': 3,'D': 3,'G': 2},
        {'D': 3,'G': 3,'B': 2},
        {'G': 3,'B': 2,'E1': 3},
        {'E': 2,'A': 3,'D': 3},
        {'D': 1,'G': 3,'B': 3,'E1': 1},
        {'E': 3,'A': 3,'D': 3,'G': 3,'B': 2,'E1': 1},
        {'E': 3,'A': 3,'D': 3,'G': 3,'B': 3}
        ]
}
blues = {
    'scale_name' : 'Blues',
    'scale_construction' : [3, 2, 1, 1, 3, 2],
    'frets': [
        {'E': 1,'A': 4,'D': 2},
        {'A': 1,'D': 4,'G': 2},
        {'D': 1,'G': 4,'B': 1, 'E1': 1},
        {'G': 1,'B': 3,'E1': 2},
        {'A': 1,'D': 3,'G': 2,'B': 1},
        {'A': 2,'D': 3,'G': 2},
        {'E': 1,'A': 3,'D': 2,'G': 2,'B': 3,'E1': 2},
        {'E': 2,'A': 3,'D': 2,'G': 2,'B': 2, 'E1': 1},
        {'D': 2,'G': 2,'B': 2},
        ]
}
bebop_minor = {
    'scale_name' : 'Bebop Minor',
    'scale_construction' : [2, 1, 2, 2, 2, 1, 1, 1],
    'frets': [
        {'E': 3,'A': 2,'D': 4},
        {'A': 3,'D': 2,'G': 4},
        {'D': 3,'G': 2,'B': 4},
        {'G': 3,'B': 2,'E1': 4},
        {'E': 1,'A': 3,'D': 3,'G': 2},
        {'A': 1,'D': 3,'G': 3,'B': 2},
        {'D': 1,'G': 3,'B': 2,'E1': 3},
        {'E': 3,'A': 2,'D': 4,'G': 3,'B': 2,'E1': 3},
        {'E': 3,'A': 3,'D': 3,'G': 3,'B': 3, 'E1':1},
        {'E': 1,'A': 3,'D': 3,'G': 4,'B': 2,'E1': 4}
        ]
}

#Half-Diminished
locrian = {
    'scale_name' : 'Locrian (Half-diminished)',
    'scale_construction' : [1, 2, 2, 1, 2, 2, 2],
    'frets': [
        {'E': 3,'A': 3,'D': 2},
        {'A': 3,'D': 3,'G': 2},
        {'D': 3,'G': 3,'B': 2},
        {'G': 3,'B': 2,'E1': 3},
        {'E': 2,'A': 3,'D': 3},
        {'A': 2,'D': 3,'G': 3},
        {'D': 2,'G': 3,'B': 2, 'E1': 1},
        {'E': 3,'A': 3,'D': 3,'G': 3,'B': 2,'E1': 1},
        {'E': 2,'A': 3,'D': 3,'G': 3,'B': 2,'E1': 2}
        ]
}
locrian2 = {
    'scale_name' : 'Locrian 2 (Half-diminished #2)',
    'scale_construction' : [2, 1, 2, 1, 2, 2, 2],
    'frets': [
        {'E': 3,'A': 3,'D': 2},
        {'A': 3,'D': 3,'G': 2},
        {'D': 3,'G': 3,'B': 2},
        {'G': 3,'B': 2,'E1': 3},
        {'E': 2,'A': 3,'D': 3},
        {'A': 2,'D': 3,'G': 3},
        {'D': 2,'G': 3,'B': 2, 'E1': 1},
        {'E': 3,'A': 3,'D': 2,'G': 3,'B': 3,'E1': 1},
        {'E': 2,'A': 3,'D': 3,'G': 3,'B': 2,'E1': 2}
        ]
}

#list all functions in this file for selection
#can make different lists/"tiers" (e.g. easy, medium, hard) and select from parent file.  This is if you want to do difficulties vice specifically pick scales.
scale_pattern_list = [ionian, dorian, phrygian, lydian, mixolydian, aeolian, locrian]
not_in_use_list = [superlocrian, major_pentatonic, minor_pentatonic, melodic_minor, harmonic_minor, blues, bebop_major, bebop_dominant, bebop_minor, whole_tone]

#not currently using.  creating categories per above comment.
major_list = [ionian, lydian]
dominant_list = [mixolydian, superlocrian]
minor_list = [aeolian, dorian, phrygian]
halfdiminished_list = [locrian]
bebop_list = [bebop_major, bebop_dominant, bebop_minor]
pentatonic_list = [major_pentatonic, minor_pentatonic]
blues_list = [blues]
other_major_list = []
other_dominant_list = [superlocrian, whole_tone]
other_minor_list = [melodic_minor, harmonic_minor]
other_halfdminishedlist = [locrian2]
