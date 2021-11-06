from yt_utils import Audio, Video, close_app, check_for_stop

print("""
 ________________________________________________________
|             Welcome to YouTube Downloader             |
|                                                       |
| Please only submit the character in square braces.    |
| Example: [A]udio   =>   A                             |
| Type 'STOP' or 'S' to exit at any time.               |
| These inputs will NOT be case-sensitive.              |
|                                                       |
| You can create a settings.txt file                    |
| with each setting on a new line                       |
| to avoid retyping them every time                     |
| Examples:    n      a     o   360p                    |
|            Names  Audio  One  360p                    |
|                                                       |
|                                                       |
|                                   Copyright Stil 2021 |
|_______________________________________________________|\n\n
""")

# Check for settings file
try:
    with open('settings.txt', 'r+') as f:
        file_content = f.read()

    settings = file_content.split('\n')
    name_or_url = settings[0][0]
    audio_or_video = settings[1][0]
    one_or_multiple = settings[2][0]
    try:
        resolution = settings[3]
    except IndexError:  # Resolution not set, default to 360p
        settings.append('360p')
        resolution = settings[3]

    print('Current settings:\n%s\n' % settings)

# Settings file not found
except FileNotFoundError:
    name_or_url = input('Would you like to download using a [N]ame or [U]rl\n').lower()
    check_for_stop(name_or_url)
    if name_or_url == '':
        name_or_url = 'n'
        print(name_or_url)

    audio_or_video = input('Would you like to download [A]udio or [V]ideo\n').lower()
    check_for_stop(audio_or_video)
    if audio_or_video == '':
        audio_or_video = 'a'
        print(audio_or_video)

    one_or_multiple = input("Would you like to download [O]ne or [M]ultiple files\n").lower()
    check_for_stop(one_or_multiple)
    if one_or_multiple == '':
        one_or_multiple = 'o'
        print(one_or_multiple)

    resolution = "360p"


while True:
    user_input = input('> ')

    # Exit app on "Stop" input
    check_for_stop(user_input)

    # Only one file
    if one_or_multiple == 'o':
        # Names
        if name_or_url == 'n' and audio_or_video == 'a':  # Name, Audio
            song_name = user_input
            Audio.download_from_name(song_name)
        if name_or_url == 'n' and audio_or_video == 'v':  # Name, Video
            song_name = user_input
            Video.download_from_name(song_name, resolution=resolution)

        # URLs
        if name_or_url == 'u' and audio_or_video == 'a':  # URL, Audio
            song_url = user_input
            Audio.download_from_url(song_url)
        if name_or_url == 'u' and audio_or_video == 'v':  # URL, Video
            video_url = user_input
            Video.download_from_url(video_url, resolution=resolution)

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
            Video.download_all(videos, resolution=resolution)

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
                Video.download_playlist(playlist_url, resolution=resolution)

            elif playlist_or_file == 'f' or playlist_or_file == '':
                with open(user_input, 'r+') as f:
                    playlist = f.readlines()
                for song_url in playlist:
                    Video.download_from_url(song_url, resolution=resolution)
