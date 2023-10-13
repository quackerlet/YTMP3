import os

from pytube import YouTube
from pytube import Playlist
from pytube.exceptions import VideoUnavailable
from pathlib import Path


from video import Video


def download_files(videos):
  """
  Downloads all files from a Video Object List

  :param videos: List of videos to download 
  """
  while len(videos) > 0:
    videos.pop(0).download()

def get_video_from_url(url, input_fields = True):
  """
  Given a link for a youtube video, returns a Video Object with 
  all fields populated based on the YT Video.

  :return: Video Object that was created, or None if the link was invalid
  """
  try:
    yt = YouTube(url)

    # NOTE: PyTube defaults to mp4 file types, we can't just change the 
    #       file extensions since it won't be formatted properly

    # download the mp4 file, will convert to mp3 later
    stream = yt.streams.filter(file_extension= 'mp4').first()

    # TODO: allow the user to select their own download location
    download_location = str(os.path.join(Path.home(), 'Downloads/ytmp3'))

    # Only ask the user for fields if input_fields is True
    if input_fields:
      title = input(f'Please enter the title of the song, or press the Enter key to use the default of {yt.title}\n>>')
      title = yt.title if title == "" else title

      author = input(f'Please enter the name of the artist, or press the Enter key to use the default of {yt.author}\n>>')
      author = yt.author if author == "" else author
    else:
      title = yt.title
      author = yt.author

    thumbnail_url = f'https://img.youtube.com/vi/{yt.video_id}/maxresdefault.jpg'

    print(f'{title} queued for download.')

    return Video(stream, title, author, thumbnail_url, output_path = download_location, filename = f'{title}.mp4')

  except VideoUnavailable:
    print(f'Video {url} is unavailable\n')

def get_playlist_from_url(url):
  """
  Given a link for a youtube playlist, returns a List of Video Object with 
  all of the videos that were in the playlist.

  :return: Video Object List that was created, or None if the link was invalid
  """
  pl = Playlist(url)
  res = []

  # for video_url in pl.video_urls:
  #   video = get_video_from_url(video_url, False)

  #   if video is not None: res.append(video)

  for video in pl.videos:
    stream = video.streams.filter(file_extension= 'mp4').first()

    thumbnail_url = f'https://img.youtube.com/vi/{video.video_id}/maxresdefault.jpg'

    # TODO: allow the user to select their own download location
    download_location = str(os.path.join(Path.home(), 'Downloads/ytmp3'))

    res.append(Video(stream, video.title, video.author, thumbnail_url, output_path = download_location, filename = f'{video.title}.mp4'))

    print(f'{video.title} queued for download.')
  
  return res


def main():
  # keep a list of videos to download so we can do it all at once
  videos = []

  while True:
    # keep taking YT links until the user enters 'd'
    url = input("Please enter the URL of the video or playlist, or d to download files:\n>>")

    if url == 'd':
      break

    if "youtube.com/playlist" in url:
      videos.extend(get_playlist_from_url(url))

    else:
      video = get_video_from_url(url)

      if video is not None: videos.append(video)
    
    print(f'{len(videos)} items in the Queue.')

  download_files(videos)
  print('Goodbye!')

main()


