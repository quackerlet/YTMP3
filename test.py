import urllib.request
import eyed3
import os
from eyed3.id3.frames import ImageFrame


# following code from https://stackoverflow.com/questions/65668113/how-to-set-thumbnail-for-mp3-using-eyed3-python-module
audiofile = eyed3.load('C:/Users/3nnem/Downloads/Capital Letters.mp3')
print(os.path.exists('C:/Users/3nnem/Downloads/Capital Letters.mp3'))

audiofile.tag.title = u'Hello'

audiofile.tag.images.set(ImageFrame.FRONT_COVER, open('tmp.jpg','rb').read(), 'image/jpeg')

audiofile.tag.save()