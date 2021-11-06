# YouTube-Downloader
#### Download youtube playlists or lists of songs/videos using `pytube`

## Classes `Audio` and `Video` have the same methods

Use `download_all` to download from your own list of items using the pytube **Search** function
```py
file_name = 'songs.txt'

with open(file_name, 'r+') as f:
   songs = f.readlines()

Audio.download_all(songs)
```
  
Use `download_playlist` to download a playlist passing in your own playlist object

Use `download_from_url` to download a file using its URL

Use `download_from_name` to download a file by searching for it through pytube

`playlist/songs: list[str] / pytube.Playlist`
  Your own playlist/songs object


`file_extension: String`
  File extension to use
  >Default: ".mp3"
  
  
`file_prefix: Bool`
  If you want a file prefix
  >Default: True
  
  
`resolution: String`
  Resolution you want the vid/song to be in
  >Default: "360p"


`new_folder: String`
  If you'd like to make a new folder, type it here in a raw string
  >Default: ""
  ```
  Example: r"\new_folder"
  ```


`prefix: Int`
  Prefix for the downloaded file
  >Default: 1
   ```
   Example: 1. Frank Sinatra - Thats Life
            2. Bobby Vinton - Sealed With a Kiss
   ```  
  
`sleep_time: Int`
  Delay between each download in seconds
  >Default: 2
