#!/usr/local/bin/python3

import midi
import psonic as ps
import time


def midiNumToFreq(note):
    a = 440
    return (a/32) * (2 ** ((note - 9) / 12))

class midiPlayer:
    def __init__(self, instrumentHandler, fi, tempo, track=None):
        '''
        input parameters:
        - instrumentHandler: a function that takes the following inputs:
          - pitch: the pitch IN MIDI NOTE, not Hz
          - duration: the length of the note in seconds
        - fi: a midi file with one or more tracks
        - tempo: the tempo in beats per minute (BPM)
        - track (optional): an integer to specify the track number in the midi file

        returns: None
        '''
        # read the midi file
        self.pattern = midi.read_midifile(fi)

        # get the parts per quarter note (aka the file's sound resolution)
        # this is used to calculate the correct note duration
        self.tempo = tempo
        self.ppq = self.pattern.resolution
        self.secs_per_beat = (60000 / (tempo * self.ppq) * self.ppq / 1000)
        self.track = self.pattern[0]
        if track is not None:
            self.track = self.pattern[track]

        self.songEnd = False

        self.startSong(instrumentHandler)

    def startSong(self, instrumentHandler):

        for line in self.track:
            if isinstance(line, midi.events.NoteOnEvent):
                    n = line.data[0] # get the midi note
                    tick = line.tick # get the note length in midi ticks

                    # convert ticks to seconds for duration
                    dur = 60000 / (self.tempo * self.ppq) * tick / 1000

                    if line.data[1] == 80:
                        # skip rests
                        ps.sleep(dur)
                    else:
                        try:
                            instrumentHandler(n, dur, player=self)
                        except:
                            instrumentHandler(n, dur)
            if isinstance(line, midi.events.EndOfTrackEvent):
                self.songEnd = True

