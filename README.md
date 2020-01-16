# MSIM2020 – Music
A Python package for making your own instrument that will play to a MIDI track. For the Tufts MSIM Raspberry Pi Music project in year 2020.

## Prerequisites

You will need to install python-sonic, a simple Python interface for Sonic Pi.
`pip install python-sonic`

Download [python3-midi](https://github.com/louisabraham/python3-midi) by following their instructions. As in, download the repository in the link, then from a terminal you will navigate to the folder you downloaded, then run the following while in the folder:

```
python setup.py install
```

### Note
Sonic Pi needs to be open on the same computer for python-sonic to make sounds. So, if you plan on playing sounds from python-sonic, open Sonic Pi in the background!

## Installation

Use this command (but please let me know right away if it doesn't work for you):

`python3 -m pip install -i https://test.pypi.org/simple/ msim2020-homorhythm`

## Examples

### Importing

```import msimmusic as mm```

### How to use
`startSong()` is the primary interface to start playing the song. 

```
mm.startSong(playInstrument, midiFile, tempo, track=None)
```

The three required parameters (and the optional fourth):

1. A function that startSong will call
2. A string for the MIDI file name
3. An integer for the tempo of the song
4. An integer for the track number in the MIDI file (aka, which instrument) 
	* Even if there are several, startSong will default to the first track if none are given

	
The function provided for #1 above must have exactly two parameters representing 1) the note pitch (aka frequency) and 2) the duration _in that order_. Example definition:

```
def playSynth(p, dur):
	if p == 69:
		ps.play(p)
		ps.sleep(dur)
	# more code below
```
You might wonder, why are we checking if the pitch is `69` in the example above? Well, `69` is actually the MIDI number for the note A at 440.00 Hz. 
**Please pay attention to the units of pitch and duration for your needs.** 

The duration of the note is simply in seconds.


#### Converting pitch from MIDI number in Hz
If you need frequency in Hz instead of the MIDI number, use this function:

```
f = mm.midiNumToFreq(p)
```

#### Getting the name of the MIDI number
If you want the note names, for now please refer to a resource such as [this table](https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies).

### A fully working example

Make sure you have a MIDI file in the directory you run this example below called "funkymusic.mid" for this to work.


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
    mm.startSong(playSawSynth, midiFile, tempo, 0)

if __name__ == "__main__":
    main()

```
