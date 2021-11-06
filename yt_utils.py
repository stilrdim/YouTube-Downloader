import datetime
import os
from time import sleep
from pytube import YouTube, Playlist, Search

DW_FOLDER = os.getcwd() + r"\downloads"


class Audio:
    @staticmethod
    def download_playlist(playlist_url, file_extension=".mp3", file_prefix=True,
                          resolution="360p", new_folder="", prefix=1, sleep_time=2):
        """ Download all songs from a playlist """
        timestamp = str(datetime.datetime.now()).split(maxsplit=11)[1].split('.')[0]
        playlist = Playlist(playlist_url)
        print(f'[{timestamp}] Downloading:\n{playlist.title}\n')  # Announce starting the downloads

        itag = choose_resolution(resolution, audio_only=True)

        for song in playlist.videos:
            try:
                if file_prefix is True:
                    song.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + new_folder,
                        filename=song.title + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:  # Don't add prefix to songs
                    song.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + new_folder,
                        filename=song.title + file_extension,)
            except AttributeError:  # Resolution not found
                if file_prefix is True:
                    song.streams.filter(only_audio=True).first().download(
                        output_path=DW_FOLDER + new_folder,
                        filename=song.title + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:
                    song.streams.filter(only_audio=True).first().download(
                        output_path=DW_FOLDER + new_folder,
                        filename=song.title + file_extension,)
                resolution_not_found()

            song.register_on_complete_callback(finished(song.title, prefix))  # Log in console on completion
            prefix += 1  # Increment the prefix number
            sleep(sleep_time)  # Avoid getting in trouble with YouTube

    @staticmethod
    def download_all(songs, file_extension=".mp3", file_prefix=True,
                     resolution="360p", new_folder="", prefix=1, sleep_time=2):
        """ Download all songs by searching for each """
        itag = choose_resolution(resolution, audio_only=True)

        for song in songs:
            song_name = song.replace('\n', '')
            s = Search(song_name).results[0]  # Get first result of the search

            try:
                if file_prefix is True:
                    s.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + new_folder,
                        filename=song_name + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:
                    s.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + new_folder,
                        filename=song_name + file_extension,)
            except AttributeError:
                if file_prefix is True:
                    s.streams.filter(only_audio=True).first().download(
                        output_path=DW_FOLDER + new_folder,
                        filename=song_name + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:
                    s.streams.filter(only_audio=True).first().download(
                        output_path=DW_FOLDER + new_folder,
                        filename=song_name + file_extension,)
                resolution_not_found()

            s.register_on_complete_callback(finished(song_name, prefix))
            prefix += 1
            sleep(sleep_time)

    @staticmethod
    def download_from_url(song_url, file_extension=".mp3", resolution="360p", new_folder=""):
        """ Downloads a song by URL """
        itag = choose_resolution(resolution, audio_only=True)
        song = YouTube(song_url)
        try:
            song.streams.get_by_itag(itag).download(
                output_path=DW_FOLDER + new_folder,
                filename=song.title + file_extension,)
        except AttributeError:
            song.streams.filter(only_audio=True).first().download(
                output_path=DW_FOLDER + new_folder,
                filename=song.title + file_extension,)
        finished(song.title)

    @staticmethod
    def download_from_name(song_name, file_extension=".mp3", resolution="360p", new_folder="",
                           result_iter=0):
        """ Downloads a song by searching for the name """
        itag = choose_resolution(resolution, audio_only=True)
        song = Search(song_name).results[result_iter]

        try:
            song.streams.get_by_itag(itag).download(
                output_path=DW_FOLDER + new_folder,
                filename=song.title + file_extension,)
        except AttributeError:
            song.streams.filter(only_audio=True).first().download(
                output_path=DW_FOLDER + new_folder,
                filename=song.title + file_extension,)
        finished(song.title)


class Video:
    @staticmethod
    def download_playlist(playlist_url, file_extension=".mp4", file_prefix=True,
                          resolution="360p", new_folder="", prefix=1, sleep_time=2):
        """ Download all videos from a playlist """
        timestamp = str(datetime.datetime.now()).split(maxsplit=11)[1].split('.')[0]

        playlist = Playlist(playlist_url)
        itag = choose_resolution(resolution)

        print(f'[{timestamp}] Downloading:\n{playlist.title}\n')

        for video in playlist.videos:
            try:
                if file_prefix is True:
                    video.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + new_folder,
                        filename=video.title + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:
                    video.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + new_folder,
                        filename=video.title + file_extension,)
            except AttributeError:
                if file_prefix is True:
                    video.streams.filter(only_video=True).first().download(
                        output_path=DW_FOLDER + new_folder,
                        filename=video.title + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:
                    video.streams.filter(only_video=True).first().download(
                        output_path=DW_FOLDER + new_folder,
                        filename=video.title + file_extension,)
                resolution_not_found()

            video.register_on_complete_callback(finished(video.title, prefix))
            prefix += 1
            sleep(sleep_time)

    @staticmethod
    def download_all(videos, file_extension=".mp4", file_prefix=True,
                     resolution="360p", new_folder="", prefix=1, sleep_time=2):
        """ Download all videos by searching for each """
        itag = choose_resolution(resolution)

        for video in videos:
            video_name = video.replace('\n', '')
            s = Search(video_name).results[0]

            try:
                if file_prefix is True:
                    s.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + new_folder,
                        filename=video_name + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:
                    s.streams.get_by_itag(itag).download(
                        output_path=DW_FOLDER + new_folder,
                        filename=video_name + file_extension,)
            except AttributeError:
                if file_prefix is True:
                    s.streams.filter(only_video=True).first().download(
                        output_path=DW_FOLDER + new_folder,
                        filename=video_name + file_extension,
                        filename_prefix="%s. " % prefix,)
                elif file_prefix is False:
                    s.streams.filter(only_video=True).first().download(
                        output_path=DW_FOLDER + new_folder,
                        filename=video_name + file_extension,)
                resolution_not_found()

            s.register_on_complete_callback(finished(video_name, prefix))
            prefix += 1
            sleep(sleep_time)

    @staticmethod
    def download_from_url(video_url, file_extension=".mp4", resolution="360p", new_folder=""):
        """ Downloads a video by URL """
        itag = choose_resolution(resolution)
        video = YouTube(video_url)
        try:
            video.streams.get_by_itag(itag).download(
                output_path=DW_FOLDER + new_folder,
                filename=video.title + file_extension,)
        except AttributeError:
            video.streams.filter(only_video=True).first().download(
                output_path=DW_FOLDER + new_folder,
                filename=video.title + file_extension,)
            resolution_not_found()
        finished(video.title)

    @staticmethod
    def download_from_name(video_name, file_extension=".mp4", resolution="360p", new_folder="",
                           result_iter=0):
        """ Downloads a video by searching for the name """
        itag = choose_resolution(resolution)
        video = Search(video_name).results[result_iter]
        try:
            video.streams.get_by_itag(itag).download(
                output_path=DW_FOLDER + new_folder,
                filename=video.title + file_extension,)
        except AttributeError:
            video.streams.filter(only_video=True).first().download(
                output_path=DW_FOLDER + new_folder,
                filename=video.title + file_extension,)
        finished(video.title)


def choose_resolution(resolution, audio_only=False):
    resolution = resolution.lower()
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
    print("WARNING!!! Resolution not found!")


def close_app(message="Thank you for using the app!\nHave a nice day!",
              sleep_time=3):
    print(message)
    sleep(sleep_time)
    exit(1)


def check_for_stop(string_to_check: str):
    if string_to_check.lower() == 's' or string_to_check.lower() == 'stop' or string_to_check.lower() == 'exit':
        close_app()


def finished(video_title, iterator=1):
    """ Print information about the file that just finished downloading """
    timestamp = str(datetime.datetime.now()).split(maxsplit=11)[1].split('.')[0]
    print('[%s] %s downloaded!\t[%s]' % (timestamp, video_title, iterator))
