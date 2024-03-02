# Copyright (c) 2024, oakenduck
# All rights reserved.
#
# This software is dedicated to the public domain under the Creative Commons Zero v1.0 Universal license.
# You can find the full text of the license in the LICENSE file
# or at https://creativecommons.org/publicdomain/zero/1.0/


import argparse


subdivision_choices = [1, 2, 4, 8, 16, 32, 64]
tuplet_choices = [2, 3, 5, 6, 7, 9]

parser = argparse.ArgumentParser(description="Generate musical rhythms in LilyPond syntax.")

parser.add_argument(
    "-s",
    "--subdivision",
    metavar="N",
    type=int,
    default=16,
    choices=subdivision_choices,
    help="smallest subdivision to generate"
)

parser.add_argument(
    "-t",
    "--tuplets",
    metavar="N",
    choices=tuplet_choices,
    nargs="+",
    type=int,
    help="tuplet types to include"
)

parser.add_argument(
    "-m",
    "--meter",
    metavar=("N", "D"),
    nargs=2,
    type=int,
    default=[4, 4],
    help="time signature"
)

parser.add_argument(
    "-c",
    "--count",
    metavar="N",
    type=int,
    default=1,
    help="how many measures to generate"
)

parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="verbose output"
)

parser.add_argument(
    "-r",
    "--rests",
    action="store_true",
    help="include rests"
)

parser.add_argument(
    "-o",
    "--output",
    metavar="f",
    type=argparse.FileType('w'),
    help="optional output destination"
)
