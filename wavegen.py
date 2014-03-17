#! /usr/bin/python3

"""A structure that wraps a wave file,
    generates audio data and saves it to a file."""

# Scripted by Carl di Ortus | reklamukibiras@gmail.com
# Available in MIT license (see LICENCE)

import chunk
import math


# Possible example waves to generate
EXAMPLESINEWAVE = 0


class wavegen:
    """Wraps a WAV file struture and auto-generates some canned waveforms."""
    
    def __init__(self):
        self.header = chunk.WaveHeader
        self.formate = chunk.WaveFormatChunk
        self.data = chunk.WaveDataChunk
    
    def wavegen(self, type=EXAMPLESINEWAVE, freq=440.0):
        """Initializes the object and generates a wave by given type."""
        
        self.header = chunk.WaveHeader()
        self.formate = chunk.WaveFormatChunk()
        self.data = chunk.WaveDataChunk()
        
        if (type==EXAMPLESINEWAVE):
            numSamples = self.formate.dwSamplesPerSec * self.formate.wChannels
            
            self.data.shortArray.append(0)
            self.data.shortArray = self.data.shortArray*numSamples
            amplitude = 32760   # max amplitude for 16-bit audio
            
            # "angle" used in function, adjusted for the number of channels
            # and sample rate. This value is like the period of the wave.
            t = (math.pi * 2 * freq) / \
                (self.formate.dwSamplesPerSec * self.formate.wChannels)
            
            for i in range(self.formate.dwSamplesPerSec):
                for channel in range(self.formate.wChannels):
                    self.data.shortArray[i*2 + channel] = int(amplitude * math.sin(t * i))
        return

    def save(filePath):
        """Saves the cyrrent wave data to the specified file.
        File is always overwritten if already exists."""
        pass
