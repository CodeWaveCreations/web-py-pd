#GENERATE NOTES
def generate_octave_notes(base_note):

    '''
    Calculates and returns the notes of an octave based on the given base note.
    :return: A list containing all the notes of an octave starting from the given base note.
    '''

    notes = []

    for i in range(6):
        octave_notes = [base_note * (2 ** (i / 12.0)) for i in range(12)]
        notes.extend(octave_notes)
        base_note *= 2 
    return notes

c0, c_sharp0, d0, d_sharp0, e0, f0, f_sharp0, g0, g_sharp0, a0, a_sharp0, b0 = [16, 17, 18, 19, 20, 21, 23, 24, 26, 27, 29, 31]