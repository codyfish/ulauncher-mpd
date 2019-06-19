from enum import Enum


class Action(Enum):
    NONE = 0

    TOGGLE_PLAY = 1
    PLAY = 2
    PAUSE = 3

    NEXT = 4
    PREVIOUS = 5

    CLEAR = 6

    ADD_SONG = 11
    ADD_ALBUM = 12
    ADD_ARTIST = 13
    ADD_FOLDER = 14
    ADD_PLAYLIST = 15

    INSERT_SONG = 21
    INSERT_ALBUM = 22
    INSERT_ARTIST = 23
    INSERT_FOLDER = 24
    INSERT_PLAYLIST = 25

    ADD_TO_PLAYLIST = 41


class CommandData:
    def __init__(self, action, data=None):
        self.action = action
        self.data = data
