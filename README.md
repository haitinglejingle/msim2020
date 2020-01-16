# MSIM2020 – Music
A Python package for making your own instrument that will play to a MIDI track. For the Tufts MSIM Raspberry Pi Music project in year 2020.

## Prerequisites


1. You will need to install python-sonic, a simple Python interface for Sonic Pi.
`python3 -m pip install python-sonic`

2. Download [python3-midi](https://github.com/louisabraham/python3-midi) by following their instructions. They're a bit tricky, so feel free to ask me for help.

3. [Sonic Pi](https://sonic-pi.net/) needs to be open on the same computer for python-sonic to make sounds. So, if you plan on playing sounds from python-sonic, open Sonic Pi in the background!

**Okay, now check that you did all three steps above so it doesn't haunt you later.**

_Note: It would be great if someone (or later, I) could add an install script to make this process easier. In the meantime, please ask if you need help!_

## Installation

Enter this into your command line prompt (but please let me know right away if it doesn't work for you):

`python3 -m pip install -i https://test.pypi.org/simple/ msim2020-homorhythm`

## Examples

### A fully working example

If you copy-paste this into file to run, make sure you have a MIDI file in the same directory as that file called "funkymusic.mid". You can download the one here from this GitHub repo above.


```
import msimmusic as mm
import psonic as ps

midiFile = "funkymusic.mid"

def playSawSynth(pitch, duration):
    ps.use_synth(ps.SAW)
    ps.play(pitch, release=0.2)
    ps.sleep(duration)

def main():
    tempo = 120
    track = 0   # also try 1 and 2
    mm.midiPlayer(playSawSynth, midiFile, tempo, 0)

if __name__ == "__main__":
    main()

```

### Importing

`import msimmusic as mm`

### How to use
`midiPlayer()` is the object to provide the interface to start playing a track.

```
mm.midiPlayer(playInstrument, midiFile, tempo, track=None)
```

The three required parameters (and the optional fourth):

1. A function that midiPlayer will call
2. A string for the MIDI file name
3. An integer for the tempo of the song
4. An integer for the track number in the MIDI file (aka, which instrument) 
	* Even if there are several tracks in the MIDI file, midiPlayer will default to the first track if none are given


The function provided for #1 above must have at least these two parameters representing 1) the note pitch (aka frequency) and 2) the duration _in that order_. Example definition:

```
def playSynth(p, dur):
	if p == 69:
		ps.play(p)
		ps.sleep(dur)
	# more code below
```

**A note on units:**
You might wonder, why are we checking if the pitch is `69` in the example above? Well, `69` is actually the MIDI number for the note A at 440.00 Hz. The duration of the note is simply in seconds.
**Please pay attention to the units of pitch and duration for your needs.**


##### Converting pitch from MIDI number in Hz
If you need frequency in Hz instead of the MIDI number, use this function:

```
f = mm.midiNumToFreq(p)
```

#### Getting the name of the MIDI number
If you want to use the letter note names, python-sonic library has them as a variable named as the letter and octave. For example, `ps.B3` or `ps.C5`.

For fun, You can also refer to [this table](https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies).


### Need more control? Get the midiPlayer instance
You can also get the midiPlayer instance back by including it as an additional parameter. Then, you can access internal instance variables yourself. For example:

```
def playSynth(p, dur, player):
    ps.use_synth(ps.SAW)

    # Only play if the note is A4
    if (p == ps.A4):
        ps.play(p)
        # play the duration of half a beat instead of the duration specified in the MIDI
        ps.sleep(player.secs_per_beat / 2)
```
