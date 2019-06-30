from MpdData import Action

COMMAND_NAMES = {
    "toggle": Action.TOGGLE_PLAY,
    "play": Action.PLAY,
    "pause": Action.PAUSE,
    "next": Action.NEXT,
    "previous": Action.PREVIOUS,
    "clear": Action.CLEAR,

    "song-add": Action.ADD_SONG,
    "song-insert": Action.INSERT_SONG,
    "album-add": Action.ADD_ALBUM,
    "album-insert": Action.INSERT_ALBUM,
    "artist-add": Action.ADD_ARTIST,
    "artist-insert": Action.INSERT_ARTIST,
    "folder-add": Action.ADD_FOLDER,
    "folder-insert": Action.INSERT_FOLDER,
    "playlist-add": Action.ADD_PLAYLIST,
    "playlist-insert": Action.INSERT_PLAYLIST,

    "add-to-playlist": Action.ADD_TO_PLAYLIST,

    # Shortcuts

    "sa": Action.ADD_SONG,
    "si": Action.INSERT_SONG,
    "aa": Action.ADD_ALBUM,
    "ai": Action.INSERT_ALBUM,
    "ia": Action.ADD_ARTIST,
    "ii": Action.INSERT_ARTIST,
    "fa": Action.ADD_FOLDER,
    "fi": Action.INSERT_FOLDER,
    "la": Action.ADD_PLAYLIST,
    "li": Action.INSERT_PLAYLIST,

    "atp": Action.ADD_TO_PLAYLIST,

}


def parse_command(command):
    return [value for key, value in COMMAND_NAMES.items() if key.startswith(command)]
