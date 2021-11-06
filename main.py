from yt_utils import Audio, Video, close_app

print("""
 ________________________________________________________
|             Welcome to YouTube Downloader             |
|                                                       |
| Please only submit the character in square braces.    |
| Example: [A]udio   =>   A                             |
| Type 'STOP' or 'S' to exit at any time.               |
| These inputs will NOT be case-sensitive.              |
|                                                       |
|                                   Copyright Stil 2021 |
|_______________________________________________________|\n\n
""")
name_or_url = input('Would you like to download using a [N]ame or [U]rl\n').lower()
audio_or_video = input('Would you like to download [A]udio or [V]ideo\n').lower()
one_or_multiple = input("Would you like to download [O]ne or [M]ultiple files\n").lower()

while True:
    user_input = input('> ')

    # Exit app on "Stop" input
    if user_input.lower() == 'stop' or user_input.lower() == 's':
        close_app()

    # Only one file
    if one_or_multiple == 'o' or '':
        # Names
        if name_or_url == 'n' and audio_or_video == 'a':  # Name, Audio
            song_name = user_input
            Audio.download_from_name(song_name)
        if name_or_url == 'n' and audio_or_video == 'v':  # Name, Video
            song_name = user_input
            Video.download_from_name(song_name)

        # URLs
        if name_or_url == 'u' and audio_or_video == 'a':  # URL, Audio
            song_url = user_input
            Audio.download_from_url(song_url)
        if name_or_url == 'u' and audio_or_video == 'v':  # URL, Video
            video_url = user_input
            Video.download_from_url(video_url)

    # Multiple files
    if one_or_multiple == 'm':
        # Names
        if name_or_url == 'n' and audio_or_video == 'a':  # Name, Audio
            with open(user_input, 'r+') as f:
                songs = f.readlines()
            Audio.download_all(songs)
        if name_or_url == 'n' and audio_or_video == 'v':  # Name, Video
            with open(user_input, 'r+') as f:
                videos = f.readlines()
            Video.download_all(videos)

        # URLs
        if name_or_url == 'u' and audio_or_video == 'a':  # URL, Audio
            playlist_or_file = input("Did you insert a [P]laylist or [F]ile with URLs?\n").lower()

            # Downloading from a playlist
            if playlist_or_file == 'p':
                playlist_url = user_input
                Audio.download_playlist(playlist_url)

            # Downloading from a file
            elif playlist_or_file == 'f' or playlist_or_file == '':
                with open(user_input, 'r+') as f:
                    playlist = f.readlines()
                for song_url in playlist:
                    Audio.download_from_url(song_url)

        if name_or_url == 'u' and audio_or_video == 'v':  # URL, Video
            playlist_or_file = input("Did you insert a [P]laylist or [F]ile with URLs?\n").lower()

            if playlist_or_file == 'p':
                playlist_url = user_input
                Video.download_playlist(playlist_url)

            elif playlist_or_file == 'f' or playlist_or_file == '':
                with open(user_input, 'r+') as f:
                    playlist = f.readlines()
                for song_url in playlist:
                    Video.download_from_url(song_url)
