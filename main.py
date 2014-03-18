#! /usr/bin/python3

"""Code for the main form of this app."""

# Scripted by Carl di Ortus | reklamukibiras@gmail.com
# Available in MIT license (see LICENCE)

from wavegen import *


class Main:
    
    def generateWave(filename, type=0, freq=440.0):
        """Generates a wave and saves it to a file"""
        
        wave = wavegen()
        wave.wavegen(type, freq)
        wave.save(filename);
        # SoundPlayer player = new SoundPlayer(filePath);               
        # player.Play();
    
