import urllib.request
import eyed3
import os
from moviepy.editor import *
from eyed3.id3.frames import ImageFrame


class Video:
  def __init__(self, stream, title, author, thumbnail_url, output_path = None, filename = None, filename_prefix = None, skip_existing = True):
    self.stream = stream
    self.title = title
    self.author = author
    self.thumbnail_url = thumbnail_url
    self.output_path = output_path
    self.filename = filename
    self.filename_prefix = filename_prefix
    self.skip_existing = skip_existing
  
  def download(self):
    self.stream.download(output_path = self.output_path, filename = self.filename, filename_prefix = self.filename_prefix, skip_existing = self.skip_existing)    
    
    # following code from https://stackoverflow.com/questions/65668113/how-to-set-thumbnail-for-mp3-using-eyed3-python-module
    
    urllib.request.urlretrieve(self.thumbnail_url, "tmp.jpg")
    
    mp4filepath = self.output_path + '/' + self.filename
    mp3filepath = self.output_path + '/' + self.title + '.mp3'

    video = VideoFileClip(mp4filepath)
    video.audio.write_audiofile(mp3filepath)


    audiofile = eyed3.load(mp3filepath)

    if (audiofile.tag == None):
      print('init tag')
      audiofile.initTag()
    
    audiofile.tag.title = self.title
    audiofile.tag.author = self.author

    audiofile.tag.images.set(ImageFrame.FRONT_COVER, open("tmp.jpg", 'rb').read(), 'image/jpeg')

    audiofile.tag.save(version=eyed3.id3.ID3_V2_3)

    video.close()
    
    os.remove('tmp.jpg')
    os.remove(mp4filepath)
    
