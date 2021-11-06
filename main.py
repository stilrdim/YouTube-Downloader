from yt_utils import Audio, Video, create_settings, check_for_stop, check_for_setup, SETTINGS_FILE

print("""
 ________________________________________________________
|             Welcome to YouTube Downloader             |
|                                                       |
| Please only submit the character in square braces.    |
| Example: [A]udio   =>   A                             |
| Type 'STOP' or 'S' to exit at any time.               |
| These inputs will NOT be case-sensitive.              |
|                                                       |
| [Names, Multiple] setting will require input          |
| with the name of a .txt file with songs separated     |
| by a new line                                         |
|                                                       |
| [URL, Multiple] setting will require a YT playlist    |
| or a file with URLs separated by a new line           |
|                                                       |
|                                                       |
|                                                       |
| You can create a settings.txt file                    |
| with each setting on a new line                       |
| to avoid retyping them every time                     |
| or use SETUP as first input                           |
|                                                       |
| Examples:    n      a     o   360p                    |
|            Names  Audio  One  360p                    |
|                                                       |
|                                                       |
|                                   Copyright Stil 2021 |
|_______________________________________________________|
           https://github.com/stilrdim/YouTube-Downloader\n\n
""")

# Check for settings file
try:
    with open(SETTINGS_FILE, 'r+') as f:
        file_content = f.read()

    settings = file_content.split('\n')
    name_or_url = settings[0][0]            # Setting 1
    audio_or_video = settings[1][0]         # 2
    one_or_multiple = settings[2][0]        # 3
    try:  # Resolution
        resolution = settings[3]            # 4
    except IndexError:  # Resolution not set, default to 360p
        settings.append('360p')
        resolution = settings[3]
    try:  # Sub Folder
        sub_folder = "\\" + settings[4]     # 5
    except IndexError:  # Sub folder not set, don't make one
        settings.append('')
        sub_folder = settings[4]
    # Delay in seconds
    if one_or_multiple == 'm':
        delay = int(settings[5])            # 6
    else:
        delay = 2
    print('Current settings:\n%s\n' % settings)

# Settings file not found
except FileNotFoundError:
    name_or_url = input("If it's your first time using the app, you can use SETUP to get a settings.txt file"
                        "\n\nWould you like to download using a [N]ame or [U]rl\n").lower()
    check_for_stop(name_or_url)
    if name_or_url == '':
        name_or_url = 'n'  # Default setting
        print(name_or_url)
    check_for_setup(name_or_url)  # Check if setup was requested

    audio_or_video = input('Would you like to download [A]udio or [V]ideo\n').lower()
    check_for_stop(audio_or_video)
    if audio_or_video == '':
        audio_or_video = 'a'  # Default setting
        print(audio_or_video)
    check_for_setup(audio_or_video)

    one_or_multiple = input("Would you like to download [O]ne or [M]ultiple files\n").lower()
    check_for_stop(one_or_multiple)
    if one_or_multiple == '':
        one_or_multiple = 'o'  # Default setting
        print(one_or_multiple)
    check_for_setup(one_or_multiple)

    # Default settings
    resolution = "360p"
    sub_folder = ''
    delay = 2


while True:
    user_input = input('> ')

    # Exit app on "Stop" input
    check_for_stop(user_input)

    # Exit app on "Setup" input
    check_for_setup(user_input)

    # Only one file
    if one_or_multiple == 'o':
        # Names
        if name_or_url == 'n' and audio_or_video == 'a':  # Name, Audio
            song_name = user_input
            Audio.download_from_name(song_name, sub_folder=sub_folder)
        if name_or_url == 'n' and audio_or_video == 'v':  # Name, Video
            song_name = user_input
            Video.download_from_name(song_name, sub_folder=sub_folder, resolution=resolution)

        # URLs
        if name_or_url == 'u' and audio_or_video == 'a':  # URL, Audio
            song_url = user_input
            Audio.download_from_url(song_url, sub_folder=sub_folder)
        if name_or_url == 'u' and audio_or_video == 'v':  # URL, Video
            video_url = user_input
            Video.download_from_url(video_url, sub_folder=sub_folder, resolution=resolution)

    # Multiple files
    if one_or_multiple == 'm':
        # Names
        if name_or_url == 'n' and audio_or_video == 'a':  # Name, Audio
            with open(user_input, 'r+') as f:
                songs = f.readlines()
            Audio.download_all(songs, sub_folder=sub_folder, delay=delay)
        if name_or_url == 'n' and audio_or_video == 'v':  # Name, Video
            with open(user_input, 'r+') as f:
                videos = f.readlines()
            Video.download_all(videos, sub_folder=sub_folder, delay=delay, resolution=resolution)

        # URLs
        if name_or_url == 'u' and audio_or_video == 'a':  # URL, Audio
            playlist_or_file = input("Did you insert a [P]laylist or [F]ile with URLs?\n").lower()

            # Downloading from a playlist
            if playlist_or_file == 'p':
                playlist_url = user_input
                Audio.download_playlist(playlist_url, sub_folder=sub_folder, delay=delay)

            # Downloading from a file
            elif playlist_or_file == 'f' or playlist_or_file == '':
                with open(user_input, 'r+') as f:
                    playlist = f.readlines()
                for song_url in playlist:
                    Audio.download_from_url(song_url, sub_folder=sub_folder, delay=delay)

        if name_or_url == 'u' and audio_or_video == 'v':  # URL, Video
            playlist_or_file = input("Did you insert a [P]laylist or [F]ile with URLs?\n").lower()

            if playlist_or_file == 'p':
                playlist_url = user_input
                Video.download_playlist(playlist_url, sub_folder=sub_folder, delay=delay, resolution=resolution)

            elif playlist_or_file == 'f' or playlist_or_file == '':
                with open(user_input, 'r+') as f:
                    playlist = f.readlines()
                for song_url in playlist:
                    Video.download_from_url(song_url, sub_folder=sub_folder, delay=delay, resolution=resolution)
