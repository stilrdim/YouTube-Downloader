import datetime
import os
from time import sleep
from pytube import YouTube, Playlist, request, Search

DW_FOLDER = os.getcwd() + r"\downloads"


def download_playlist(playlist, file_extension=".mp3", file_prefix=True,
                      resolution="360p", new_folder="", prefix=1, sleep_time=2):
    """ Download all videos in a playlist """
    timestamp = str(datetime.datetime.now()).split(maxsplit=11)[1].split('.')[0]
    print(f'[{timestamp}] Downloading:\n{playlist.title}\n')  # Announce starting the downloads

    for video in playlist.videos:
        video_title = video.title
        try:
            if file_prefix is True:
                video.streams.get_by_resolution(resolution).download(
                    output_path=DW_FOLDER + new_folder,
                    filename=video_title + file_extension,
                    filename_prefix="%s. " % prefix,
                )
            elif file_prefix is False:  # Don't add prefix to songs
                video.streams.get_by_resolution(resolution).download(
                    output_path=DW_FOLDER + new_folder,
                    filename=video_title + file_extension,
                )
        except:  # Resolution not found
            if file_prefix is True:
                video.streams.first().download(
                    output_path=DW_FOLDER + new_folder,
                    filename=video_title + file_extension,
                    filename_prefix="%s. " % prefix,
                )
            elif file_prefix is False:  # Don't add prefix to songs
                video.streams.first().download(
                    output_path=DW_FOLDER + new_folder,
                    filename=video_title + file_extension,
                )
            print("WARNING!!!\tResolution not found")

        video.register_on_complete_callback(finished(video_title))  # Log in console on completion
        prefix += 1  # Increment the prefix number
        sleep(sleep_time)  # Avoid getting in trouble with YouTube


def download_all(songs, file_extension=".mp3", file_prefix=True,
                 resolution="360p", new_folder="", prefix=1, sleep_time=2):
    """ Download all songs by searching for each """
    for song in songs:
        song_name = song.replace('\n', '')
        s = Search(song_name).results[0]  # Get first result of the search

        if file_prefix is True:
            s.streams.get_by_resolution(resolution).download(
                output_path=DW_FOLDER + new_folder,
                filename=song_name + file_extension,
                filename_prefix="%s. " % prefix,
            )
        elif file_prefix is False:  # Don't add prefix to songs
            s.streams.get_by_resolution(resolution).download(
                output_path=DW_FOLDER + new_folder,
                filename=song_name + file_extension,
            )

        s.register_on_complete_callback(finished(song_name))  # Log in console on completion
        prefix += 1  # Increment the prefix number
        sleep(sleep_time)  # Avoid getting in trouble with YouTube


def finished(song_title):
    # Create timestamps for each download
    timestamp = str(datetime.datetime.now()).split(maxsplit=11)[1].split('.')[0]

    print('[%s] %s downloaded!' % (timestamp, song_title))
