from pytubefix import *
yt = YouTube(input('Cole o link aqui:'))
print(yt.title)
print(yt.thumbnail_url)
stream = yt.streams.get_highest_resolution()
stream.download()