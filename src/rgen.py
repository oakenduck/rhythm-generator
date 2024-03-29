# Copyright (c) 2024, oakenduck
# All rights reserved.
#
# This software is dedicated to the public domain under the Creative Commons Zero v1.0 Universal license.
# You can find the full text of the license in the LICENSE file
# or at https://creativecommons.org/publicdomain/zero/1.0/


from gen_v1 import generate_measure
from note import distribute_notes, build_note
from parser import parser, subdivision_choices
from tools import combine_rests


if __name__ == "__main__":
    args = parser.parse_args()

    subd_idx = subdivision_choices.index(args.subdivision)

    if args.verbose:
        print(
            "do not " * (1 ^ args.rests) + "include rests\n"
            f"subdivisions: {subdivision_choices[:subd_idx + 1]}\n"
            f"tuplets to include: {args.tuplets}\n"
            f"meter: {args.meter[0]}/{args.meter[1]}\n"
        )

    notes = distribute_notes(subd_idx)
    rests = [
        build_note(s, rest=True) for s in subdivision_choices[:subd_idx + 1]
    ]

    if args.rests:
        notes += distribute_notes(subd_idx, rest=True, coeff=0.5)

    if args.dots:
        notes += distribute_notes(subd_idx - 1, dot=True, coeff=0.35)
        if args.rests:
            notes += distribute_notes(subd_idx - 1, dot=True, rest=True, coeff=0.35)

    idx = 0
    rhythms = []
    time_sig = args.meter[0]/args.meter[1]

    while idx < args.count:
        measure = generate_measure(notes, time_sig)

        if args.rests:
            measure = combine_rests(measure, rests)

        if measure in rhythms:
            continue

        rhythms.append(measure)
        idx += 1

        print(f"\rmeasures generated: {idx}", end="")

    print("\ngeneration complete.")

    if args.sorted:
        rhythms = sorted(rhythms, key=len)

    if args.output is not None:
        for measure in rhythms:
            args.output.write(" ".join(n.alias for n in measure) + "\n")

        args.output.close()
        print(f"output in {args.output.name}")
    else:
        for measure in rhythms[:1000]:
            print(" ".join(n.alias for n in measure))

        if len(rhythms) > 1000:
            print("output truncated due to size limit")
