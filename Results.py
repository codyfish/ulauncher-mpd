from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

import os

from MpdData import Action
from MpdData import CommandData
from AlbumArtCache import AlbumArtCache

COMMANDS = {
    Action.TOGGLE_PLAY: ExtensionResultItem(icon='images/toggle.svg',
                                            name="Toggle",
                                            description="Pause/Play",
                                            on_enter=ExtensionCustomAction(
                                                data=CommandData(Action.TOGGLE_PLAY),
                                                keep_app_open=False)),
    Action.PLAY: ExtensionResultItem(icon='images/play.svg',
                                     name="Play",
                                     description="play",
                                     on_enter=ExtensionCustomAction(data=CommandData(Action.PLAY),
                                                                    keep_app_open=False)),
    Action.PAUSE: ExtensionResultItem(icon='images/pause.svg',
                                      name="Pause",
                                      description="Pause",
                                      on_enter=ExtensionCustomAction(data=CommandData(Action.PAUSE),
                                                                     keep_app_open=False)),
    Action.NEXT: ExtensionResultItem(icon='images/next.svg',
                                     name="Next",
                                     description="Next",
                                     on_enter=ExtensionCustomAction(data=CommandData(Action.NEXT),
                                                                    keep_app_open=False)),
    Action.PREVIOUS: ExtensionResultItem(icon='images/previous.svg',
                                         name="Previous",
                                         description="Previous",
                                         on_enter=ExtensionCustomAction(data=CommandData(Action.PREVIOUS),
                                                                        keep_app_open=False)),
    Action.CLEAR: ExtensionResultItem(icon='images/clear.svg',
                                      name="Clear",
                                      description="Clear queue",
                                      on_enter=ExtensionCustomAction(data=CommandData(Action.CLEAR),
                                                                     keep_app_open=False)),
    Action.ADD_SONG: ExtensionResultItem(icon='images/title.svg',
                                         name="song-add",
                                         description="Add Song",
                                         on_enter=ExtensionCustomAction(data=CommandData(Action.NONE),
                                                                        keep_app_open=True)),
    Action.ADD_ALBUM: ExtensionResultItem(icon='images/album.svg',
                                          name="album-add",
                                          description="Add Album",
                                          on_enter=ExtensionCustomAction(data=CommandData(Action.NONE),
                                                                         keep_app_open=True)),
    Action.ADD_ARTIST: ExtensionResultItem(icon='images/artist.svg',
                                           name="artist-add",
                                           description="Add Artist",
                                           on_enter=ExtensionCustomAction(data=CommandData(Action.NONE),
                                                                          keep_app_open=True)),
    Action.INSERT_SONG: ExtensionResultItem(icon='images/title.svg',
                                            name="song-insert",
                                            description="Insert Song",
                                            on_enter=ExtensionCustomAction(data=CommandData(Action.NONE),
                                                                           keep_app_open=True)),
    Action.INSERT_ALBUM: ExtensionResultItem(icon='images/album.svg',
                                             name="album-insert",
                                             description="Insert Album",
                                             on_enter=ExtensionCustomAction(data=CommandData(Action.NONE),
                                                                            keep_app_open=True)),
    Action.INSERT_ARTIST: ExtensionResultItem(icon='images/artist.svg',
                                              name="artist-insert",
                                              description="Insert Artist",
                                              on_enter=ExtensionCustomAction(data=CommandData(Action.NONE),
                                                                             keep_app_open=True)),
    Action.ADD_FOLDER: ExtensionResultItem(icon='images/folder.svg',
                                           name="folder-add",
                                           description="Add Folder",
                                           on_enter=ExtensionCustomAction(data=CommandData(Action.NONE),
                                                                          keep_app_open=True)),
    Action.INSERT_FOLDER: ExtensionResultItem(icon='images/folder.svg',
                                              name="folder-insert",
                                              description="Insert Folder",
                                              on_enter=ExtensionCustomAction(data=CommandData(Action.NONE),
                                                                             keep_app_open=True)),
    Action.ADD_PLAYLIST: ExtensionResultItem(icon='images/playlist.svg',
                                             name="playlist-add",
                                             description="Add Playlist",
                                             on_enter=ExtensionCustomAction(data=CommandData(Action.NONE),
                                                                            keep_app_open=True)),
    Action.INSERT_PLAYLIST: ExtensionResultItem(icon='images/playlist.svg',
                                                name="playlist-insert",
                                                description="Insert Playlist",
                                                on_enter=ExtensionCustomAction(data=CommandData(Action.NONE),
                                                                               keep_app_open=True)),

    Action.ADD_TO_PLAYLIST: ExtensionResultItem(icon='images/add-to-playlist.svg',
                                                name="add-to-playlist",
                                                description="Adds current song to a playlist",
                                                on_enter=ExtensionCustomAction(data=CommandData(Action.NONE),
                                                                               keep_app_open=True)),

}


def list_commands(command_suggestions=None):
    if command_suggestions is not None:
        items = [COMMANDS[action] for action in command_suggestions]
    else:
        items = [value for (key, value) in COMMANDS.items()]
    return RenderResultListAction(items)


def list_music(client, album_art_cache, command, args):
    if command is Action.ADD_SONG:
        return list_songs(client, album_art_cache, Action.ADD_SONG, args)
    elif command is Action.ADD_ALBUM:
        return list_albums(client, album_art_cache, Action.ADD_ALBUM, args)
    elif command is Action.ADD_ARTIST:
        return list_artists(client, album_art_cache, Action.ADD_ARTIST, args)
    elif command is Action.ADD_FOLDER:
        return list_folders(client, album_art_cache, Action.ADD_FOLDER, args)
    elif command is Action.ADD_PLAYLIST:
        return list_playlists(client, album_art_cache, Action.ADD_PLAYLIST, args)
    elif command is Action.INSERT_SONG:
        return list_songs(client, album_art_cache, Action.INSERT_SONG, args)
    elif command is Action.INSERT_ALBUM:
        return list_albums(client, album_art_cache, Action.INSERT_ALBUM, args)
    elif command is Action.INSERT_ARTIST:
        return list_artists(client, album_art_cache, Action.INSERT_ARTIST, args)
    elif command is Action.INSERT_FOLDER:
        return list_folders(client, album_art_cache, Action.INSERT_FOLDER, args)
    elif command is Action.INSERT_PLAYLIST:
        return list_playlists(client, album_art_cache, Action.INSERT_PLAYLIST, args)
    elif command is Action.ADD_TO_PLAYLIST:
        return list_playlists(client, album_art_cache, Action.ADD_TO_PLAYLIST, args)
    else:
        pass


def list_songs(client, album_art_cache, action, args):
    query_results = client.search('title', args)

    if len(query_results) <= 9:
        query_results += [song for song in client.search('any', args) if song not in query_results]

    query_results = query_results[:9]

    items = [ExtensionResultItem(icon=album_art_cache.get_album_art(song),
                                 name="{} - {}".format(song['artist'], song['title']) if 'artist' in song.keys()
                                 else song['title'],
                                 description="Add Song",
                                 on_enter=ExtensionCustomAction(data=CommandData(action, data=song['file']),
                                                                keep_app_open=False))
             for song in query_results]
    return RenderResultListAction(items)


def list_albums(client, album_art_cache, action, args):
    albums_results = client.list('album', "(album =~ '(?i){}.*$')".format(args))
    albums_results += [album for album in client.list('album', "(Any =~ '(?i){}.*$')".format(args)) if
                       album not in albums_results]
    albums_results = albums_results[:9]

    items = [ExtensionResultItem(icon=album_art_cache.get_album_art_album(client, album),
                                 name=album,
                                 description="Add Album",
                                 on_enter=ExtensionCustomAction(data=CommandData(action, data=album),
                                                                keep_app_open=False))
             for album in albums_results]
    return RenderResultListAction(items)


def list_artists(client, album_art_cache, action, args):
    artist_results = client.list('artist', "(artist =~ '(?i){}.*$')".format(args))
    artist_results += [artist for artist in client.list('artist', "(Any =~ '(?i){}.*$')".format(args)) if
                       artist not in artist_results]
    artist_results = artist_results[:9]

    items = [ExtensionResultItem(icon=album_art_cache.get_album_art_artist(client, artist),
                                 name=artist,
                                 description="Add Artist",
                                 on_enter=ExtensionCustomAction(data=CommandData(action, data=artist),
                                                                keep_app_open=False))
             for artist in artist_results]
    return RenderResultListAction(items)


def get_largest_path(path, args):
    args = args.lower()

    dirs = path.split('/')

    for i in range(len(dirs) - 1, 0, -1):
        if args in dirs[i].lower():
            return '/'.join(dirs[0:i + 1])

    return dirs[0]


def list_folders(client, album_art_cache, action, args):
    # prevent errors with ascii and unicode in later maps and filters
    # do not encode in python 3
    # args = args.encode('UTF-8')
    # also in the middle of the path
    folder_results = client.list('file', "(file =~ '.*(?i){}.*$')".format(args))

    # print type(folder_results[0])
    # print type(args)

    # remove file name matches
    folder_results = list(filter(lambda path: args.lower() in os.path.dirname(path).lower(), folder_results))
    # make dir names
    folder_results = list(map(lambda path: os.path.dirname(path), folder_results))
    # unify names
    folder_results = set(folder_results)
    # remove tailing paths
    folder_results = list(set(map(lambda path: get_largest_path(path, args), folder_results)))
    # sort by length / deepness
    folder_results.sort(key=len)
    # max elements afterwards
    folder_results = folder_results[:9]

    items = [ExtensionResultItem(icon=album_art_cache.get_album_art_folder(client, folder),
                                 name=folder,
                                 description="Add Folder",
                                 on_enter=ExtensionCustomAction(data=CommandData(action, data=folder),
                                                                keep_app_open=False))
             for folder in folder_results]
    return RenderResultListAction(items)


def list_playlists(client, album_art_cache, action, args):
    args = args.lower()

    playlist_results = client.listplaylists()
    # filter lists
    playlist_results = list(filter(lambda p: p['playlist'].lower().startswith(args), playlist_results))

    items = [ExtensionResultItem(icon=album_art_cache.get_album_art_playlist(client, playlist['playlist']),
                                 name=playlist['playlist'],
                                 description="Add Playlist",
                                 on_enter=ExtensionCustomAction(data=CommandData(action, data=playlist['playlist']),
                                                                keep_app_open=False))
             for playlist in playlist_results]
    return RenderResultListAction(items)
