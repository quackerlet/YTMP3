# YTMP3++
---

`YTMP3++` is a terminal based (for now) Python application that converts YouTube videos (most likely songs) into mp3 files. For everyone like me who is too cheap to get Spotify :grin:.

## Installation
---

Unfortunately, the only way to use `YTMP3++` is by either cloning the repo or downloading the code. There are also a few dependencies that can be installed with the following:

`$ pip install -r requirements.txt`

It is also required that you have `FFMPEG` installed on your system. It should be installed whenever you install `moviepy`, but it seems that it doesn't always turn out that way :slightly_frowning_face:.

If it is not automatically installed, simply install it from [here](https://ffmpeg.org/download.html) for Windows and through brew for Mac, and set your path variables appropriately.

A better method is coming soon :smiling_face_with_tear:!

## Usage
---

After cloning or downloading the repository, navigate into this directory and run 

`python3 ytmp3++.py` (For MacOS) or

`py ytmp3++.py` (For Windows)

The program will then ask you to input video or playlist links. When you are finished inputting videos, enter 'd' to download all videos queued.

