from yt_utils import download_all

file_name = 'songs.txt'

with open(file_name, 'r+') as f:
    songs = f.readlines()

download_all(songs=songs, new_folder="\\test2")
