# YouTube-Downloader
###### Download youtube playlists or lists of songs/videos using `pytube`

### Would you like to download using a [N]ame or [U]rl?
`Inputs:`
`N` `U` `SETUP`

### Would you like to download [A]udio or [V]ideo?
`Inputs:`
`A` `V` `SETUP`

### Would you like to download [O]ne or [M]ultiple files?
`Inputs:`
`O` `M` `SETUP`

>[M] reads from a `txt file` on input if you selected `Name` on first prompt


>[M] reads from a `playlist` OR `txt file` if you selected `URL` on the first prompt

### Empty input always defaults to the first choice

##
### You can create a settings.txt file manually or use SETUP as any of the inputs
>Example settings.txt
```
name
video
one
720p
sub_folder
2
yes
```
`sub_folder` **Creates new folder inside the `downloads` folder (in this case, new folder will be called `sub_folder`)**
`2` **Delay (secs) when using the `Multiple` setting**
`yes` **Will shuffle the list of songs/videos before downloading when using the `Multiple` setting**


# YouTube-Downloader-Python (yt_utils)
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

Use `check_for_stop(user_input: String)` to check if the user input was "stop" or "s", if so, closes the file 

Use `check_for_setup(user_input: String)` to check if the user input was "setup", if so, begins creating a settings.txt

`songs/videos/playlist: list[str] / pytube.Playlist`
  Your own songs/videos/playlst object


`file_extension: String`
  File extension to use
  >Default: ".mp3"
  
  
`file_prefix: Bool`
  If you want a file prefix
  >Default: True
  
  
`resolution: String`
  Resolution you want the vid/song to be in
  >Default: "360p"


`sub_folder: String`
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
  
`delay: Int`
  Delay between each download in seconds
  >Default: 2

`shuffle_list: Bool`
  Shuffle list before download (Only available in download_all)
