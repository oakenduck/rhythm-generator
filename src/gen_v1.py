# Copyright (c) 2024, oakenduck
# All rights reserved.
#
# This software is dedicated to the public domain under the Creative Commons Zero v1.0 Universal license.
# You can find the full text of the license in the LICENSE file
# or at https://creativecommons.org/publicdomain/zero/1.0/


from typing import Tuple, List
from dataclasses import dataclass
from random import choice, randint


@dataclass
class Note:
    alias: str
    fraction: Tuple[int, int]

    @property
    def length(self) -> float:
        return self.fraction[0] / self.fraction[1]

    def __str__(self) -> str:
        return f"{self.fraction[0]}/{self.fraction[1]}"


def filter_note_choices(notes: List[Note], remaining: float) -> List[Note]:
    return [note for note in notes if note.length <= remaining]


def find_rhythms(notes: List[Note], time_sig: float = 4/4, limit: int = 100) -> List[List[Note]]:
    idx = 0
    measures = []

    while idx < limit:
        measure = []
        options = notes
        measure_length = 0

        while measure_length <= time_sig:
            # get all note lengths that are less/equal to remaining time
            options = filter_note_choices(options, time_sig - measure_length)

            if len(options) == 0:
                break  # there are no valid choices

            note = choice(options)
            measure.append(note)
            measure_length += note.length

        if measure_length != time_sig:
            continue  # current notes are more/less than 1 measure in time_sig

        if measure in measures:
            continue  # current rhythm has already been found

        measures.append(measure)
        idx += 1
        print(f"\rmeasures generated: {idx}", end="")

    return measures


if __name__ == "__main__":
    c1  = Note('c1', (1, 1))
    c2  = Note('c2', (1, 2))
    c4  = Note('c4', (1, 4))
    c8  = Note('c8', (1, 8))
    c16 = Note('c16', (1, 16))

    notes = [c1] + [c2]*2 + [c4]*4 + [c8]*8 + [c16]*16

    rest_replace = False
    time_sig = 4/4
    limit = 5272

    rhythms = find_rhythms(notes, time_sig=time_sig, limit=limit)
    rhythms = sorted(rhythms, key=len)

    for r in rhythms:
        for note in r:
            if rest_replace and (randint(0, 100)) < 20:
                print(note.alias.replace('c', 'r'), end=" ")
            else:
                print(note.alias, end=" ")
        print()
