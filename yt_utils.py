import datetime
import os
import atexit
from time import sleep
from pytube import YouTube, Playlist, Search

DW_FOLDER = os.getcwd() + r"\downloads"
SETTINGS_FILE = 'settings.txt'


class Audio:
    @staticmethod
    def download_playlist(playlist_url, file_extension=".mp3", file_prefix=True,
                          resolution="360p", sub_folder="", prefix=1, delay=2):
        """ Download all songs from a playlist """
        timestamp = str(datetime.datetime.now()).split(maxsplit=11)[1].split('.')[0]
        playlist = Playlist(playlist_url)
        print(f'[{timestamp}] Downloading:\n{playlist.title}\n')  # Announce starting the downloads

        itag = choose_resolution(resolution, audio_only=True)

        for song in playlist.videos:
            try:
                if file_prefix is True:
                    song.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=song.title + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:  # Don't add prefix to songs
                    song.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=song.title + file_extension,)
            except AttributeError:  # Resolution not found
                if file_prefix is True:
                    song.streams.filter(only_audio=True).first().download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=song.title + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:
                    song.streams.filter(only_audio=True).first().download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=song.title + file_extension,)
                resolution_not_found()

            song.register_on_complete_callback(finished(song.title, prefix))  # Log in console on completion
            prefix += 1  # Increment the prefix number
            sleep(delay)  # Avoid getting in trouble with YouTube

    @staticmethod
    def download_all(songs, file_extension=".mp3", file_prefix=True,
                     resolution="360p", sub_folder="", prefix=1, delay=2):
        """ Download all songs by searching for each """
        itag = choose_resolution(resolution, audio_only=True)

        for song in songs:
            song_name = song.replace('\n', '')
            s = Search(song_name).results[0]  # Get first result of the search

            try:
                if file_prefix is True:
                    s.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=song_name + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:
                    s.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=song_name + file_extension,)
            except AttributeError:
                if file_prefix is True:
                    s.streams.filter(only_audio=True).first().download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=song_name + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:
                    s.streams.filter(only_audio=True).first().download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=song_name + file_extension,)
                resolution_not_found()

            s.register_on_complete_callback(finished(song_name, prefix))
            prefix += 1
            sleep(delay)

    @staticmethod
    def download_from_url(song_url, file_extension=".mp3", resolution="360p", sub_folder="", delay=0):
        """ Downloads a song by URL """
        itag = choose_resolution(resolution, audio_only=True)
        song = YouTube(song_url)
        try:
            song.streams.get_by_itag(itag).download(
                output_path=DW_FOLDER + sub_folder,
                filename=song.title + file_extension,)
        except AttributeError:
            song.streams.filter(only_audio=True).first().download(
                output_path=DW_FOLDER + sub_folder,
                filename=song.title + file_extension,)
        finished(song.title)
        sleep(delay)

    @staticmethod
    def download_from_name(song_name, file_extension=".mp3", resolution="360p", sub_folder="",
                           delay=0, result_iter=0):
        """ Downloads a song by searching for the name """
        itag = choose_resolution(resolution, audio_only=True)
        song = Search(song_name).results[result_iter]

        try:
            song.streams.get_by_itag(itag).download(
                output_path=DW_FOLDER + sub_folder,
                filename=song.title + file_extension,)
        except AttributeError:
            song.streams.filter(only_audio=True).first().download(
                output_path=DW_FOLDER + sub_folder,
                filename=song.title + file_extension,)
        finished(song.title)
        sleep(delay)


class Video:
    @staticmethod
    def download_playlist(playlist_url, file_extension=".mp4", file_prefix=True,
                          resolution="360p", sub_folder="", prefix=1, delay=2):
        """ Download all videos from a playlist """
        timestamp = str(datetime.datetime.now()).split(maxsplit=11)[1].split('.')[0]

        playlist = Playlist(playlist_url)
        itag = choose_resolution(resolution)

        print(f'[{timestamp}] Downloading:\n{playlist.title}\n')

        for video in playlist.videos:
            try:
                if file_prefix is True:
                    video.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=video.title + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:
                    video.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=video.title + file_extension,)
            except AttributeError:
                if file_prefix is True:
                    video.streams.filter(only_video=True).first().download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=video.title + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:
                    video.streams.filter(only_video=True).first().download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=video.title + file_extension,)
                resolution_not_found()

            video.register_on_complete_callback(finished(video.title, prefix))
            prefix += 1
            sleep(delay)

    @staticmethod
    def download_all(videos, file_extension=".mp4", file_prefix=True,
                     resolution="360p", sub_folder="", prefix=1, delay=2):
        """ Download all videos by searching for each """
        itag = choose_resolution(resolution)

        for video in videos:
            video_name = video.replace('\n', '')
            s = Search(video_name).results[0]

            try:
                if file_prefix is True:
                    s.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=video_name + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:
                    s.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=video_name + file_extension,)
            except AttributeError:
                if file_prefix is True:
                    s.streams.filter(only_video=True).first().download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=video_name + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:
                    s.streams.filter(only_video=True).first().download(
                        output_path=DW_FOLDER + sub_folder,
                        filename=video_name + file_extension,)
                resolution_not_found()

            s.register_on_complete_callback(finished(video_name, prefix))
            prefix += 1
            sleep(delay)

    @staticmethod
    def download_from_url(video_url, file_extension=".mp4", resolution="360p", sub_folder="", delay=0):
        """ Downloads a video by URL """
        itag = choose_resolution(resolution)
        video = YouTube(video_url)
        try:
            video.streams.get_by_itag(itag).download(
                output_path=DW_FOLDER + sub_folder,
                filename=video.title + file_extension,)
        except AttributeError:
            video.streams.filter(only_video=True).first().download(
                output_path=DW_FOLDER + sub_folder,
                filename=video.title + file_extension,)
            resolution_not_found()
        finished(video.title)
        sleep(delay)

    @staticmethod
    def download_from_name(video_name, file_extension=".mp4", resolution="360p", sub_folder="",
                           result_iter=0, delay=0):
        """ Downloads a video by searching for the name """
        itag = choose_resolution(resolution)
        video = Search(video_name).results[result_iter]
        try:
            video.streams.get_by_itag(itag).download(
                output_path=DW_FOLDER + sub_folder,
                filename=video.title + file_extension,)
        except AttributeError:
            video.streams.filter(only_video=True).first().download(
                output_path=DW_FOLDER + sub_folder,
                filename=video.title + file_extension,)
        finished(video.title)
        sleep(delay)


def choose_resolution(resolution, audio_only=False):
    if audio_only:
        if resolution in ["min", "144", "144p"]:
            i_tag = 249  # TODO: research i_tags for audio
        elif resolution in ["very low", "240", "240p"]:
            i_tag = 249
        elif resolution in ["low", "360", "360p"]:
            i_tag = 249
        elif resolution in ["medium", "480", "480p"]:
            i_tag = 249
        elif resolution in ["high", "720", "720p"]:
            i_tag = 250
        elif resolution in ["very high", "1080", "1080p"]:
            i_tag = 251
        elif resolution in ["ultra high", "1440", "1440p"]:
            i_tag = 251
        elif resolution in ["max", "2160", "2160p", "4k"]:
            i_tag = 251
        else:
            i_tag = 140

    elif audio_only is False:
        if resolution in ["min", "144", "144p"]:
            i_tag = 160  # 278 webm_30fps, 330 webm_60fps
        elif resolution in ["very low", "240", "240p"]:
            i_tag = 133  # 242 webm_30fps, 331 webm_60fps
        elif resolution in ["low", "360", "360p"]:
            i_tag = 134  # 243 webm_30fps, 134 mp4, 18 previous value
        elif resolution in ["medium", "480", "480p"]:
            i_tag = 135  # 244 webm_30fps, 333 webm_60fps
        elif resolution in ["high", "720", "720p"]:
            i_tag = 22  # 136 mp4_30fps, 298 mp4_60fps
        elif resolution in ["very high", "1080", "1080p"]:
            i_tag = 137  # 248 webm_30fps, 299 mp4_60fps, 303 webm_60fps, 335 webm_60fps
        elif resolution in ["ultra high", "1440", "1440p"]:
            i_tag = 271  # 308 webm_60fps, 336 webm_60fps
        elif resolution in ["max", "2160", "2160p", "4k"]:
            i_tag = 313  # 315 webm_60fps, 337 webm_60fps
        else:
            i_tag = 18
    return i_tag


def resolution_not_found():
    print("[WARNING] Resolution not found for the file below! Downloaded lower resolution instead")


def create_settings(settings_file):
    """ Handles the setup of a settings.txt file """
    settings = []
    resolutions = ["blank", "empty", "",
                   "min", "144", "144p",
                   "very low", "240", "240p",
                   "low", "360", "360p",
                   "medium", "480", "480p",
                   "high", "720", "720p",
                   "very high", "1080", "1080p",
                   "ultra high", "1440", "1440p",
                   "max", "2160", "2160p", "4k",
                   ]

    os.system('cls')
    print("\nsettings.txt will be created in the script folder.\n\n"
          "Please select one of each on the next couple of questions"
          " and type in the full word\n")

    # Get settings
    name_or_url = input("Name or URL\n").lower()
    try:
        while name_or_url[0] not in ['n', 'u']:
            print('Invalid input. Expecting: "Name" or "URL"')
            name_or_url = settings.append(input("Name or URL\n").lower())
        else:
            settings.append(name_or_url)
    except IndexError:  # Default to Name
        name_or_url = 'name'
        print(name_or_url)
        settings.append(name_or_url)

    audio_or_video = input("Audio or Video\n").lower()
    try:
        while audio_or_video[0] not in ['a', 'v']:
            print('Invalid input. Expecting: "Audio" or "Video"')
            audio_or_video = input("Audio or Video\n").lower()
        else:
            settings.append(audio_or_video)
    except IndexError:  # Default to Audio
        audio_or_video = 'audio'
        print(audio_or_video)
        settings.append(audio_or_video)

    one_or_multiple = input("One or Multiple\n").lower()
    try:
        while one_or_multiple[0] not in ['o', 'm']:
            print('Invalid input. Expecting: "One" or "Multiple"')
            one_or_multiple = input("One or Multiple\n").lower()
        else:
            settings.append(one_or_multiple)
    except IndexError:  # Default to One
        one_or_multiple = 'one'
        print(one_or_multiple)
        settings.append(one_or_multiple)

    resolution = input("360p, 480p, 720p, 1080p, 1440p, 2160p\nRecommended: 360p or 720p\n").lower()
    while resolution not in resolutions:
        print('Invalid input. Expecting: \n%s\n' % resolutions)
        resolution = input("360p, 480p, 720p, 1080p, 1440p, 2160p\nRecommended: 360p or 720p\n").lower()
    else:
        if resolution == 'blank' or resolution == '' or resolution == 'empty':  # Defaults to empty, resulting in 360p
            print('360p')
        settings.append(resolution)

    settings.append(input("Name a sub-folder:\t\t(Leave empty if not needed)\n"))  # Sub folder name

    if one_or_multiple[0] == 'm':
        delay = input("This app uses delayed requests to not overload YouTube's servers.\n"  # Delay in seconds
                      "How much of a delay in seconds would you like?\n"
                      "Default: 2\n")
        if delay == '':
            delay = 2
        settings.append(delay)

    # Write the settings down and exit the file
    with open(settings_file, 'w') as f:
        counter = 0
        for setting in settings:
            if counter != len(settings) - 1:
                f.write("%s\n" % setting)
            else:  # Don't put a newline after the last setting
                f.write(setting)
            counter += 1
    close_app("\n\nThe app will now close.\nPlease reopen it for changes to take effect.")


def check_for_stop(string_to_check: str):
    if string_to_check.lower() == 's' or string_to_check.lower() == 'stop' or string_to_check.lower() == 'exit':
        close_app("Thank you for using the app!\nHave a nice day!")


def check_for_setup(string_to_check: str):
    if string_to_check.lower() == 'setup':  # The user requested a new setup
        try:
            os.remove(SETTINGS_FILE)
            create_settings(SETTINGS_FILE)
        except FileNotFoundError:
            with open(SETTINGS_FILE, 'x') as f:
                pass
            create_settings(SETTINGS_FILE)


def close_app(message, sleep_time=3):
    print(message)
    sleep(sleep_time)
    exit(1)


def finished(video_title, iterator=1):
    """ Print information about the file that just finished downloading """
    timestamp = str(datetime.datetime.now()).split(maxsplit=11)[1].split('.')[0]
    print('[%s] %s downloaded!\t[%s]' % (timestamp, video_title, iterator))


# On app close (KeyboardInterrupt, etc...)
@atexit.register
def goodbye():
    os.system('cls')
    print("Thank you for using the app!\nHave a nice day!")
    sleep(2)
