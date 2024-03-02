# Copyright (c) 2024, oakenduck
# All rights reserved.
#
# This software is dedicated to the public domain under the Creative Commons Zero v1.0 Universal license.
# You can find the full text of the license in the LICENSE file
# or at https://creativecommons.org/publicdomain/zero/1.0/


from typing import Tuple, List
from math import log, ceil, floor
from dataclasses import dataclass


@dataclass
class Note:
    alias: str
    fraction: Tuple[int, int]

    @property
    def length(self) -> float:
        return self.fraction[0] / self.fraction[1]

    def __repr__(self) -> str:
        return self.alias


def build_note(subd: int, *, dotted: bool = False, rest: bool = False) -> Note:
    if dotted:
        ly_not  = f"c{subd}."
        duration = (3, subd * 2)
    else:
        ly_not   = f"c{subd}"
        duration = (1, subd)

    if rest:
        ly_not = ly_not.replace('c', 'r')

    return Note(ly_not, duration)


def tuplet(n: int, subdivision: int):
    base = 2**floor(log(n, 2))

    if n == 2:  # duplets are an exception
        base = 3

    notes = " ".join(f"c{subdivision}" for i in range(n))

    ly_not = f"\\tuplet {n}/{base} " + '{ ' + notes + ' }'
    return Note(ly_not, (1, subdivision))


def distribute_notes(
    expo: int, rest: bool = False,
    dot: bool = False, coeff: float = 1.0
) -> List[Note]:

    notes = []

    for i in [2**n for n in range(expo + 1)]:
        notes += [build_note(i, rest=rest, dotted=dot)] * ceil(coeff * i)

    return notes
