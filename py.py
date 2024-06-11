from pytube import YouTube

yt =YouTube("https://www.youtube.com/shorts/9tJHO22L1co")
stream = yt.streams.get_by_itag(22)
stream.download()