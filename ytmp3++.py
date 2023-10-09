import os

from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from pathlib import Path


from video import Video


def download_files(videos):
  while len(videos) > 0:
    videos.pop(0).download()


def main():
  # keep a list of videos to download so we can do it all at once
  videos = []

  while True:
    # keep taking YT links until the user enters 'd'
    url = input("Please enter the URL of the video, or d to download files:\n>>")

    if url == 'd':
      break

    try:
      yt = YouTube(url)

      # NOTE: PyTube defaults to mp4 file types, we can't just change the 
      #       file extensions since it won't be formatted properly

      # download the mp4 file, will convert to mp3 later
      stream = yt.streams.filter(file_extension= 'mp4').first()

      # TODO: allow the user to select their own download location
      download_location = str(os.path.join(Path.home(), 'Downloads/mp3'))

      videos.append(Video(stream, yt.title, yt.author, yt.thumbnail_url, output_path = download_location, filename = f'{stream.title}.mp4'))

    except VideoUnavailable:
      print(f'Video {url} is unavailable')

  download_files(videos)

main()


