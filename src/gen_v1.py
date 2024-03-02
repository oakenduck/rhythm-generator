# Copyright (c) 2024, oakenduck
# All rights reserved.
#
# This software is dedicated to the public domain under the Creative Commons Zero v1.0 Universal license.
# You can find the full text of the license in the LICENSE file
# or at https://creativecommons.org/publicdomain/zero/1.0/


from typing import Tuple, List
from random import choice, randint

from note import Note


def find_rhythms(notes: List[Note], time_sig: float = 4/4, limit: int = 100, verbose=False) -> List[List[Note]]:
    idx = 0
    measures = []

    while idx < limit:
        measure, measure_length = generate_measure(notes, time_sig)

        if measure_length != time_sig:
            continue  # current notes are more/less than 1 measure in time_sig

        if measure in measures:
            continue  # current rhythm has already been found

        measures.append(measure)
        idx += 1
        if verbose:
            print(f"\rmeasures generated: {idx}", end="")

    if verbose:
        print()

    return measures


def generate_measure(notes: List[Note], time_sig: float = 4/4) -> List[Note]:
    m_length = 0
    measure = []

    while m_length <= time_sig:
        # get all note lengths that are less/equal to remaining length
        notes = [note for note in notes if note.length <= time_sig - m_length]

        if len(notes) == 0:
            break  # there are no valid options

        note = choice(notes)
        measure.append(note)
        m_length += note.length

    return measure
