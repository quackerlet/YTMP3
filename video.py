import urllib.request
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error


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
    # audio = MP3(self.output_path + '/' + self.filename, ID3=ID3)

    # urllib.request.urlretrieve(self.thumbnail_url, "tmp.jpg")

    # audio.tags.add(
    #   APIC(
    #     encoding=3,  # 3 is for utf-8
    #     mime="image/jpeg",  # can be image/jpeg or image/png
    #     type=3,  # 3 is for the cover image
    #     desc='Cover',
    #     data=open("tmp.jpg", mode='rb').read()
    #   )
    # )
    
