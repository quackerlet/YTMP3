from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from pathlib import Path
import os

from video import Video


def download_files(streams):
    while len(streams) > 0:
      streams.pop(0).download()

def main():
    videos = []

    while True:
      url = input("Please enter the URL of the video, or d to download files:\n>>")

      if url == 'd':
        break

      try:
        yt = YouTube(url)

        # get the audio
        stream = yt.streams.filter(only_audio = True).first()
        download_location = str(os.path.join(Path.home(), 'Downloads/mp3'))

        videos.append(Video(stream, yt.title, yt.author, yt.thumbnail_url, output_path = download_location, filename = f'{stream.title}.mp3'))

      except VideoUnavailable:
        print(f'Video {url} is unavailable')

    download_files(videos)

main()


