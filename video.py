import urllib.request
import eyed3
import os

from eyed3.id3.frames import ImageFrame
from moviepy.editor import *




class Video:
  def __init__(self, stream, title, author, thumbnail_url, output_path = None, filename = None, filename_prefix = None, skip_existing = True):
    # all fields as defined in PyTube
    self.stream = stream
    self.title = title
    self.author = author
    self.thumbnail_url = thumbnail_url
    self.output_path = output_path
    self.filename = filename
    self.filename_prefix = filename_prefix
    self.skip_existing = skip_existing
  
  def download(self):
    """
    Downloads a video from the Video Object using the stream to the path specified
    in *video.output_path* and calls it *video.filename*

    :return: NONE
    """


    # downloads the mp4 file from youtube
    self.stream.download(output_path = self.output_path, filename = self.filename, filename_prefix = self.filename_prefix, skip_existing = self.skip_existing)    
    
    # create file paths for mp4 and mp3 file
    mp4filepath = self.output_path + '/' + self.title + '.mp4'
    mp3filepath = self.output_path + '/' + self.title + '.mp3'

    # write mp4 data into mp3 file
    video = VideoFileClip(mp4filepath)
    video.audio.write_audiofile(mp3filepath)

    # load mp3 file to add data to it
    audiofile = eyed3.load(mp3filepath)

    if (audiofile.tag == None):
      audiofile.initTag()
    
    audiofile.tag.title = self.title
    audiofile.tag.author = self.author

    ### THUMBNAIL ###
    # NOTE: gets image directly from url - DEPRECATED
    response = urllib.request.urlopen(self.thumbnail_url)
    imagedata = response.read()
    audiofile.tag.images.set(ImageFrame.FRONT_COVER, imagedata, 'image/jpeg')

    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)

    video.close()
    
    # delete the mp4 file
    # TODO: In future may want to add support for only mp4 files
    os.remove(mp4filepath)
    
