#! /usr/bin/python3

"""Code for the main form of this app."""

# Scripted by Carl di Ortus | reklamukibiras@gmail.com
# Available in MIT license (see LICENCE)

import wavegen


class Main:
    
    def generateWave(type=wavegen.ExampleSineWave, freq=440.0, filename):
        """Generates a wave and saves it to a file"""
        
        wave = wavegen(wavegen.ExampleSineWave)
        wave.save(filename);
        # SoundPlayer player = new SoundPlayer(filePath);               
        # player.Play();
    
