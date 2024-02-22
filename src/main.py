# Copyright (c) 2024, oakenduck
# All rights reserved.
#
# This software is dedicated to the public domain under the Creative Commons Zero v1.0 Universal license.
# You can find the full text of the license in the LICENSE file
# or at https://creativecommons.org/publicdomain/zero/1.0/


if __name__ == "__main__":
    from random import randint
    from datetime import datetime as dt

    from gen_v1 import Note, find_rhythms
    from tools import combine_rests, is_all_rests


    c1  = Note('c1', (1, 1))
    c2  = Note('c2', (1, 2))
    c4  = Note('c4', (1, 4))
    c8  = Note('c8', (1, 8))
    c16 = Note('c16', (1, 16))

    c2d = Note('c2.', (3, 4))
    c4d = Note('c4.', (3, 8))

    r1 = Note('r1', (1, 1))
    r2 = Note('r2', (1, 2))
    r4 = Note('r4', (1, 4))
    r8 = Note('r8', (1, 8))

    rests = [r1, r2, r4, r8]
    notes = [c2, c4, c8] * 4 + rests

    time_sig = 4/4
    limit = 1000

    print(dt.now())
    rhythms = find_rhythms(notes, time_sig=time_sig, limit=limit, verbose=1)
    rhythms = sorted(rhythms, key=len)
    print(dt.now())

    with open(dt.now().strftime("./output/%y-%m-%d_%H-%M-%S-%f"), "w") as file:
        for r in rhythms:
            if not is_all_rests(r):
                file.write(
                    " ".join(n.alias for n in combine_rests(r, rests)) + "\n"
                )
        print("written to:", file.name)
