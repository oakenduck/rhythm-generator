# Copyright (c) 2024, oakenduck
# All rights reserved.
#
# This software is dedicated to the public domain under the Creative Commons Zero v1.0 Universal license.
# You can find the full text of the license in the LICENSE file
# or at https://creativecommons.org/publicdomain/zero/1.0/


from random import choice


def find_rhythms(nums, target=1, limit=100):
    idx = 0
    combos = []

    while idx < limit:
        cur_combo = []
        cur_length = 0
        options = nums

        while cur_length <= target:
            # get all note lengths that are less than the remaining length
            options = [i for i in options if (i + cur_length) <= target]

            if len(options) == 0:
                break  # if there are no valid choices

            ch = choice(options)

            cur_combo.append(ch)
            cur_length += ch

        if cur_length > target:
            continue  # current notes are longer than 1 measure

        if cur_combo in combos:
            continue  # no repeated rhythms

        combos.append(cur_combo)

        idx += 1

    return combos


if __name__ == "__main__":
    notes = [1] + [1/2]*2 + [1/4]*4 + [1/8]*8 + [1/16]*16
    randomly_replace_with_rests = False
    time_sig = 1  # literally 4/4
    limit = 5272  # appears to stop finding new measures at this point

    aliases = {
        1:      "c1",
        0.5:    "c2",
        0.25:   "c4",
        0.125:  "c8",
        0.0625: "c16"
    }  # aliases for note lengths to be used in frescobaldi

    rhythms = find_rhythms(notes, target=time_sig, limit=limit)
    rhythms = sorted(rhythms, key=len)

    if randomly_replace_with_rests:
        for r in rhythms:
            for note in r:
                if randint(0, 100) >= 10:
                    print(f"{aliases[note]}", end=" ")
                else:
                    print(f"{aliases[note].replace('c', 'r')}", end=" ")
            print()
    else:
        for r in rhythms:
            for note in r:
                print(f"{aliases[note]}", end=" ")
            print()
