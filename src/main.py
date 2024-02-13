# Copyright (c) 2024, oakenduck
# All rights reserved.
#
# This software is dedicated to the public domain under the Creative Commons Zero v1.0 Universal license.
# You can find the full text of the license in the LICENSE file
# or at https://creativecommons.org/publicdomain/zero/1.0/


from gen_ff_v1 import find_rhythms as fr


x = [1] + [1/2]*2 + [1/4]*4 + [1/8]*8 + [1/16]*16

if __name__ == "__main__":
    aliases = {
        1:      "c1",
        0.5:    "c2",
        0.25:   "c4",
        0.125:  "c8",
        0.0625: "c16"
    }  # aliases for note lengths to be used in frescobaldi

    rhythms = find_rhythms(notes, target=1, limit=5272)
    rhythms = sorted(rhythms, key=len)

    for r in rhythms:
        for note in r:
            if randint(0, 100) >= 10:
                print(f"{aliases[note]}", end=" ")
            else:
                print(f"{aliases[note].replace('c', 'r')}", end=" ")
        print()
