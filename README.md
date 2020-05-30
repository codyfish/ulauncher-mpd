# ulauncher-mpd
ulauncher-mpd is an extension for ulauncher that allows you to control mpd.

It enables the user to toggle playback, skip tracks and append or insert
songs, albums, interprets, folders and playlists to the current queue.
It displays and caches album arts while selecting what to play. 

## Installation

There is a version for python2 (ulauncher 4 / API 1) and one for python3 (ulauncher 5 / API 2) available.

Install this extension using ulaunchers extension menu.

### Version Notes
The python 2 version will not receive any future updates. 
The python 2 version is located in the python2 branch.

With `python-mpd2-1.1.0`, there were some API changes.
As a result, some of the extensions code had to be modified.
Install `python-mpd2-1.1.0` or manually checkout out the frozen branch 
`pre-python-mpd2-1.1.0`

### Dependencies

* `python-mpd2` (also needed for python3, in this case install with `pip`, not `pip2`)
* enum (not required for python 3)
* `mutagen`

Install these python packages using e.g. `pip install` or `pip2 install` for python 2, respectively

## Usage

Invoke the plugin by starting ulauncher and typing `mpd `.

### Commands

| command | shortcut | action |
|---------|----------|--------|
| `mpd pause` | | Pause playback |
| `mpd play` | | Start playback |
| `mpd toggle` | | Toggle playback |
| `mpd next` | | Skip to the next track in the queue |
| `mpd previous` | | Go to the previous track in the queue |
| `mpd clear` | | Clear current queue|
| `mpd song-add <title>` | `mpd sa <title>` | Add title `<title>` at the end of the queue|
| `mpd song-insert <title>` | `mpd si <title>` | Insert title `<title>` after current song|
| `mpd album-add <album>` | `mpd aa <album>`| Add album `<album>` at the end of the queue|
| `mpd album-insert <album>` | `mpd ai <album>` | Insert `<album>` album after current song|
| `mpd artist-add <artist>` | `mpd ia <artist>` | Add artist `<artist>` at the end of the queue|
| `mpd artist-insert <artist>` | `mpd ii <artist>` | Insert artist `<artist>` after current song|
| `mpd folder-add <folder>` | `mpd fa <folder>` | Add folder `<folder>` at the end of the queue|
| `mpd folder-insert <folder>` | `mpd fi <folder>` | Insert folder `<folder>` after current song|
| `mpd playlist-add <playlist>` | `mpd la <playlist>` | Add playlist `<playlist>` at the end of the queue|
| `mpd playlist-insert <playlist>` | `mpd pi <playlist>` | Insert playlist `<playlist>` after current song|
| `mpd add-to-playlist <playlist>` | `mpd adt <playlist>` | Add current song at the end of  playlist `<playlist>` |
| `mpd random-on` | `mpd rn` | Set random mode on |
| `mpd random-off` | `mpd rf` | Set random mode off |
| `mpd shuffle` | | Shuffle entire playlist once. Does not change random mode |
| `mpd volume-up <int>` | `mpd vu <int>`| Increase volume by `<int>` or `volume step` when no value is given|
| `mpd volume-down <int>` | `mpd vd <int>`| Decrease volume by `<int>` or `volume step` when no value is given|

Insert actions turn random mode off
 whereas add actions do not change the random mode.

### Cache

ulauncher-mpd caches Album arts in `XDG_CACHE_HOME/mpd-album-art` or `~/.cache/mpd-album-art`.

So far it only caches album arts that actually exist permanently, therefore after restarting ulauncher caching
large libraries without any album arts might take some while which results in longer query load times.
It only caches one song per album and assumes that all songs in one album have the same album art

#### Cached filenames

Cached album arts have following filenames in ulauncher-mpds cache folder:

* Albums: `<artist>-<title>`
* Artists: `<artist>`
* Folders: `<path>_<to>_<directory>`
* Playlist: `_<playlist>`

## Preferences

In the extension menu of ulauncher u can adjust ulauncher-mpd's preferences:

* hostname: The hostname your mpd server is running on (normally `localhost`)
* port: The port your mpd server is running on (normally `6600`)
* music directory: the directory your library is stored in (needed for album arts)
* volume step: The default volume step for increase and decrease in volume





