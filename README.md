# YouTube-Downloader
Download youtube playlists or lists of songs/videos using pytube


Use download_all to download from your own list of items using the Search function
  Example:
  file_name = 'songs.txt'

  with open(file_name, 'r+') as f:
     songs = f.readlines()

  download_all(songs=songs)
  
  
Use download_playlist to download a playlist passing in your own playlist object



playlist/songs: list[str] / pytube.Playlist
  Your own playlist/songs object


file_extension: String
  File extension you'd like
  Default: ".mp3"
  
file_prefix: Bool
  If you want a file prefix
  Default: True
  
resolution: String
  Resolution you want the vid/song to be in
  Default: "360p"
  
new_folder: String
  If you'd like to make a new folder, type it here in a raw string
  Default: ""

prefix: Int
  Prefix for the downloaded file
  Default: 1
    Example: 1. Frank Sinatra - Thats Life
             2. Bobby Vinton - Sealed With a Kiss
             etc...
  
sleep_time: Int
  Delay between each download in seconds
  Default: 2
