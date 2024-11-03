# **BAIXAR VÍDEO PELO PYTHON**

Um código em Python, onde você consegue baixar vídeos diretamente do youtube só jogando o link no terminal

Foi utilizada a biblioteca `pytubefix`, para baixar a biblioteca foi utilizado essa linha de comando no Terminal:

```
python -m pip install pytubefix
```

Depois implementei o código:

```
from pytubefix import *
yt = YouTube(input('Cole o link aqui:'))
print(yt.title)
print(yt.thumbnail_url)
stream = yt.streams.get_highest_resolution()
stream.download()

```