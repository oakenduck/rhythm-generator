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
