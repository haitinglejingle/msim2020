import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="msimmusic", # Replace with your own username
    version="0.0.1",
    author="Haiting Chan",
    author_email="haitingchan@gmail.com",
    description="Make Your MIDI Instrument. From the Tufts MSIM RPi Music Project",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/homorhythm/msim2020",
    packages=['msimmusic',],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
