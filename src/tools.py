# Copyright (c) 2024, oakenduck
# All rights reserved.
#
# This software is dedicated to the public domain under the Creative Commons Zero v1.0 Universal license.
# You can find the full text of the license in the LICENSE file
# or at https://creativecommons.org/publicdomain/zero/1.0/


from gen_v1 import Note, find_rhythms
from typing import List


def combine_rests(measure: List[Note], rests: List[Note]) -> List[Note]:
    groups = [[]]
    prev_was_rest = 'r' in measure[0].alias

    for note in measure:
        if ('r' in note.alias) ^ (prev_was_rest):
            groups.append([])

        prev_was_rest = 'r' in note.alias
        groups[-1].append(note)

    rest_map = { r.length: r for r in rests }

    for idx, group in enumerate(groups):
        if is_all_rests(group):
            new_group = []
            uniques = []

            while True:
                uniques = []

                for i in group:
                    if i not in uniques:
                        uniques.append(i)

                if len(group) == len(uniques):
                    break

                for rest in uniques:
                    div, mod = divmod(group.count(rest), 2)
                    for i in range(div):
                        new_group.append(rest_map[rest.length * 2])
                    for j in range(mod):
                        new_group.append(rest)

                group = new_group
                new_group = []

            groups[idx] = group

    ret_measure = []

    for group in groups:
        ret_measure += group

    return ret_measure


def is_all_rests(measure:List[Note]) -> bool:
    return not any("r" not in note.alias for note in measure)


def has_no_rests(measure: List[Note]) -> bool:
    return all("r" not in note.alias for note in measure)
