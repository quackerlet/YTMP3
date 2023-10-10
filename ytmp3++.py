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
      download_location = str(os.path.join(Path.home(), 'Downloads/ytmp3'))

      title = input(f'Please enter the title of the song, or press the Enter key to use the default of {yt.title}\n>>')
      title = yt.title if title == "" else title

      author = input(f'Please enter the name of the artist, or press the Enter key to use the default of {yt.author}\n>>')
      author = yt.author if author == "" else author

      thumbnail_url = f'https://img.youtube.com/vi/{yt.video_id}/maxresdefault.jpg'

      videos.append(Video(stream, title, author, thumbnail_url, output_path = download_location, filename = f'{title}.mp4'))

      print(f'{title} queued for download. {len(videos)} items in the queue.\n')

    except VideoUnavailable:
      print(f'Video {url} is unavailable\n')

  download_files(videos)
  print('Goodbye!')

main()


