from yt_utils import Audio, Video

file_name = 'songs.txt'

with open(file_name, 'r+') as f:
    songs = f.readlines()

Audio.download_all(songs=songs, new_folder=r"\test6")
