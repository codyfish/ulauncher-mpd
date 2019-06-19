# ulauncher-mpd
ulauncher-mpd is an extension for ulauncher that allows you to control mpd.

It enables the user to toggle playback, skip tracks and append or insert
songs, albums, interprets, folders and playlists to the current queue.
It displays and caches album arts while selecting what to play. 

## Installation

Currently, there is only a version for python 2 (ulauncher extension API 1/ulauncher v4) available.
Install this extension using ulaunchers extension menu.

### Dependencies

* python-mpd2
* enum
* mutagen

Install these python packages using e.g. `pip2 install`

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



