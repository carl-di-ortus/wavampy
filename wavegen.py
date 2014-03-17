#! /usr/bin/python3

"""A structure that wraps a wave file,
    generates audio data and saves it to a file"""

# Scripted by Carl di Ortus | reklamukibiras@gmail.com
# Available in MIT license (see LICENCE)

import chunk
import math


def WaveExampleType():
    """Possible example waves to generate"""
    EXAMPLESINEWAVE = 0


class wavegen:
    """Wraps a WAV file struture and auto-generates some canned waveforms."""
    
    def __init__():
        self.header = chunk.WaveHeader
        self.format = chunk.WaveFormatChunk
        self.data = chunk.WaveDataChunk
    
    def wavegen(type=WaveExampleType(), freq=440.0):
        """Initializes the object and generates a wave by given type."""
        
        header = chunk.WaveHeader()
        format = chunk.WaveFormatChunk()
        data = chunk.WaveDataChunk()
        
        if (type==WaveExampleType.ExampleSineWave):
            numSamples = format.dwSamplesPerSec * format.wChannels
            
            data.shortArray.append(numSamples)
            amplitude = 32760   # max amplitude for 16-bit audio
            
            # "angle" used in function, adjusted for the number of channels
            # and sample rate. This value is like the period of the wave.
            t = (math.pi * 2 * freq) / \
                (format.dwSamplesPerSec * format.wChannels)
            
            for i in range(numSamples):
                for i in range(format.wChannels):
                    data.shortArray[i + channel] = int(amplitude * math.sin(t * i))

        def save(filePath):
            """Saves the cyrrent wave data to the specified file.
            File is always overwritten if already exists."""
            pass
