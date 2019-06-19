from mpd import MPDClient


def get_playlist_length(client):
    return int(client.status()['playlistlength'])


def get_pos(client):
    if get_playlist_length(client) is 0:
        return 0
    else:
        return int(client.status()['song'])


def insert_song_files_at(client, pos, files):
    for song in files:
        client.addid(song, pos)
        pos = pos + 1


def insert_song_files(client, files):
    pos = get_pos(client)
    if pos is not get_playlist_length(client):
        pos = pos + 1

    insert_song_files_at(client, pos, files)


def insert_songs(client, songs):
    song_files = list(map(lambda song: song['file'], songs))
    insert_song_files(client, song_files)


def insert_song(client, song_file):
    pos = get_pos(client)
    if pos is not get_playlist_length(client):
        pos = pos + 1

    client.addid(song_file, pos)


def insert_album(client, album):
    songs = client.find('album', album)
    insert_songs(client, songs)


def insert_artist(client, artist):
    songs = client.find('artist', artist)
    insert_songs(client, songs)


def insert_folder(client, folder):
    # no song matches only a directory -> search instead of find
    songs = client.search('file', folder)
    # remove matches in the middle
    songs = list(filter(lambda path: path['file'].startswith(folder), songs))
    insert_songs(client, songs)


def insert_playlist(client, playlist):
    song_files = client.listplaylist(playlist)
    insert_song_files(client, song_files)
