#! /usr/bin/python3

"""Defines classes that wrap different chunks in a WAV file."""

# Scripted by Carl di Ortus | reklamukibiras@gmail.com
# Available in MIT license (see LICENCE)


class WaveHeader:
    """Wraps the header portion of a WAVE file.
        Variables:
            sGroupID - usualy 'RIFF'
            dwFileLength - total file length minus 8, which is taken up by RIFF
            sRiffType - usualy 'WAVE'"""

    def __init__(self, sGroupID="RIFF", dwFileLength=0, sRiffType="WAVE"):
        self.sGroupID = sGroupID
        self.dwFileLength = dwFileLength
        self.sRiffType = sRiffType


class WaveFormatChunk:
    """Wraps the Format chunk of a wave file.
        Variables:
            sChunkID - must be 'fmt ', note the last space
            dwchunkSize - length of header in bytes
            wFormatTag - 1 (MS PCM)
            wChannels - number of channels (2->Stereo)
            dwSamplesPerSec - frequency of the audio in Hz, usualy 44100
            wBitsPerSample - bit depth
            wBlockAlign - sample frame size in bytes
            dwAvgBytesPerSec - used for estimating RAM allocation"""

    def __init__(self, dwChunkSize=16, wFormatTag=1, wChannels=2,
                 dwSamplesPerSec=44100, wBitsPerSample=16):
        self.sChunkID = "fmt "
        self.dwChunkSize = dwChunkSize
        self.wFormatTag = wFormatTag
        self.wChannels = wChannels
        self.dwSamplesPerSec = dwSamplesPerSec
        self.wBitsPerSample = wBitsPerSample
        self.wBlockAlign = wChannels * (wBitsPerSample // 8)
        self.dwAvgBytesPerSec = dwSamplesPerSec * self.wBlockAlign


class WaveDataChunk:
    """Wraps the Data chunk of a wave file.
        Variables:
            sChunkID - must be 'data'
            dwChunkSize - length of header in bytes
            shortArray - 8-bit audio"""

    def __init__(self, dwChunkSize=0, shortArray=[]):
        self.sChunkID = "data"
        self.dwChunkSize = dwChunkSize
        self.shortArray = shortArray
