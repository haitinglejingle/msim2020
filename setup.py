import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="msimmusic-homorhythm", # Replace with your own username
    version="0.0.1",
    author="Haiting Chan",
    author_email="haitingchan@gmail.com",
    description="Make Your MIDI Instrument. From the Tufts MSIM RPi Music Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/homorhythm/msimmusic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
