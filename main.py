#! /usr/bin/python3

"""Code for the main form of this app."""

# Scripted by Carl di Ortus | reklamukibiras@gmail.com
# Available in MIT license (see LICENCE)

from wavegen import *
import argparse

parser = argparse.ArgumentParser(description="""
    Generates a wave file for given frequency and type.
    Default frequency is 440 Hz (Concert A).
    Currently only sine wave type is supported.""")
parser.add_argument('filename', metavar='<filename>', type=str,
                    help='location to save the generated wave file')
parser.add_argument('-f', metavar='freq', type=float, default=440.0,
                    help='frequency of a wave sample')


args = parser.parse_args()


def generateWave(filename, type=0, freq=440.0):
        """Generates a wave and saves it to a file"""

        wave = wavegen()
        wave.wavegen(type, freq)
        wave.save(filename)
        # TODO: player.Play(filename)


# TODO: extract type to argparser, when more types added
generateWave(args.filename, type=0, freq=args.f)
