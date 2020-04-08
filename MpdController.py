from mpd import MPDClient
from mpd import MPDError

import os

import QueryParser
from MpdData import Action
from MpdData import CommandData
import AlbumArtCache
import Results
import MpdHelper


class MpdController:

    def __init__(self):
        self.__client = MPDClient()

        self.__hostname = "localhost"
        self.__port = 6600
        self.__default_volume_dif = 10

        # c music_dir = os.environ['XDG_MUSIC_DIR']

        # print("initial music dir: " + music_dir)
        # self.__album_art_cache = AlbumArtCache.init_default_cache(music_dir)
        # connect later anyways
        # self.__client.connect("localhost", 6600)

    def get_mpd_version(self):
        return self.__client.mpd_version

    def set_mpd_host(self, hostname):
        self.__hostname = hostname

    def set_mpd_port(self, port):
        self.__port = int(port)

    def set_music_dir(self, music_dir):
        print("music dir: " + music_dir)
        self.__album_art_cache = AlbumArtCache.init_default_cache(music_dir)

    def set_default_volume_dif(self, dif):
        try:
            self.__default_volume_dif = int(dif)
        except (TypeError, ValueError):
            print("Default volume difference must be an integer")



    def ensure_connection(self):
        # Alternative: Async thread pinging server
        try:
            self.__client.ping()
            return True
        except MPDError:
            try:
                self.__client.connect(self.__hostname, self.__port)
                return True
            except:
                return False

    def query(self, query):

        if query is None:
            return Results.list_commands()

        # print query

        query_segments = query.lower().split(" ", 1)
        command = query_segments[0]

        if len(query_segments) == 2:
            args = query_segments[1]
        else:
            args = None

        command_suggestions = QueryParser.parse_command(command)

        print(command_suggestions)

        if len(command_suggestions) == 1 and command_suggestions[0] is Action.VOLUME_UP:
            return Results.list_volume_up(args)
        elif len(command_suggestions) == 1 and command_suggestions[0] is Action.VOLUME_DOWN:
            return Results.list_volume_down(args)
        elif args is not None and len(command_suggestions) == 1:
            if not self.ensure_connection():
                return
            return Results.list_music(self.__client, self.__album_art_cache, command_suggestions[0], args)
        else:
            return Results.list_commands(command_suggestions)

    def execute(self, item_data):
        if not self.ensure_connection():
            return

        action = item_data.action
        args = item_data.data

        playlist_length = self.__client.status()['playlistlength']
        print(playlist_length)

        if action is Action.NONE:
            # Wait for user input
            pass
        elif action is Action.TOGGLE_PLAY:
            self.__client.pause()
        elif action is Action.PLAY:
            self.__client.pause(0)
        elif action is Action.PAUSE:
            self.__client.pause(1)
        elif action is Action.NEXT:
            self.__client.next()
        elif action is Action.PREVIOUS:
            self.__client.previous()
        elif action is Action.CLEAR:
            self.__client.clear()
            # return in order not to play invalid index as cleared queue has status "stop"
            return
        elif action is Action.ADD_SONG:
            self.__client.add(args)
        elif action is Action.ADD_ALBUM:
            self.__client.findadd('album', args)
        elif action is Action.ADD_ARTIST:
            self.__client.findadd('artist', args)
        elif action is Action.ADD_FOLDER:
            self.__client.add(args)
        elif action is Action.ADD_PLAYLIST:
            self.__client.load(args)
        elif action is Action.INSERT_SONG:
            MpdHelper.insert_song(self.__client, args)
        elif action is Action.INSERT_ALBUM:
            MpdHelper.insert_album(self.__client, args)
        elif action is Action.INSERT_ARTIST:
            MpdHelper.insert_artist(self.__client, args)
        elif action is Action.INSERT_FOLDER:
            MpdHelper.insert_folder(self.__client, args)
        elif action is Action.INSERT_PLAYLIST:
            MpdHelper.insert_playlist(self.__client, args)
        elif action is Action.ADD_TO_PLAYLIST:
            song = self.__client.currentsong()
            if song:
                self.__client.playlistadd(args, song['file'])
            # Avoid playing
            return
        elif action is Action.RANDOM_ON:
            self.__client.random(1)
        elif action is Action.RANDOM_OFF:
            self.__client.random(0)
        elif action is Action.SHUFFLE:
            self.__client.shuffle()

        elif action is Action.VOLUME_UP:
            MpdHelper.volume_up(self.__client, args, self.__default_volume_dif)
        elif action is Action.VOLUME_DOWN:
            MpdHelper.volume_down(self.__client, args, self.__default_volume_dif)

        # start playing if not playing
        if self.__client.status()['state'] == "stop":
            self.__client.play(playlist_length)
