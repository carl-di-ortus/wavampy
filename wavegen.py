#! /usr/bin/python3

"""A structure that wraps a wave file,
    generates audio data and saves it to a file."""

# Scripted by Carl di Ortus | reklamukibiras@gmail.com
# Available in MIT license (see LICENCE)

import chunk
import math
import struct


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

        if (type == EXAMPLESINEWAVE):
            numSamples = self.formate.dwSamplesPerSec * self.formate.wChannels

            self.data.shortArray.append(0)
            self.data.shortArray = self.data.shortArray*numSamples
            amplitude = 32760   # max amplitude for 16-bit audio

            # "angle" used in function. Value = period of the wave.
            t = (math.pi * 2 * freq) / \
                (self.formate.dwSamplesPerSec * self.formate.wChannels)

            for i in range(self.formate.dwSamplesPerSec):
                for channel in range(self.formate.wChannels):
                    self.data.shortArray[i*2 + channel] = int(amplitude *
                                                              math.sin(t * i))
        return

    def save(self, filePath):
        """Saves the current wave data to the specified file.
        File is always overwritten if already exists."""
        # TODO: check byte packing, check file integrity

        handle = open(filePath, 'wb')

        handle.write(self.header.sGroupID.encode('ASCII'))
        handle.write(struct.pack('<i', self.header.dwFileLength))
        handle.write(self.header.sRiffType.encode('ASCII'))

        handle.write(self.formate.sChunkID.encode('ASCII'))
        handle.write(struct.pack('<i', self.formate.dwChunkSize))
        handle.write(struct.pack('<h', self.formate.wFormatTag))
        handle.write(struct.pack('<h', self.formate.wChannels))
        handle.write(struct.pack('<i', self.formate.dwSamplesPerSec))
        handle.write(struct.pack('<i', self.formate.dwAvgBytesPerSec))
        handle.write(struct.pack('<h', self.formate.wBlockAlign))
        handle.write(struct.pack('<h', self.formate.wBitsPerSample))

        handle.write(self.data.sChunkID.encode('ASCII'))
        handle.write(struct.pack('<i', self.data.dwChunkSize))
        for i in range(len(self.data.shortArray)):
            handle.write(struct.pack('<i', i))

        handle.seek(0, 2)
        filesize = handle.tell()
        handle.seek(4)
        handle.write(struct.pack('<i', filesize - 8))

        handle.close()
        return
