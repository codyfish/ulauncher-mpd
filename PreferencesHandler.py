from ulauncher.api.client.EventListener import EventListener

import os


class MpdPreferencesEvent(EventListener):
    def __init__(self, mpd_controller):
        super(MpdPreferencesEvent, self).__init__()
        self.__mpd_controller = mpd_controller

    def on_event(self, event, extension):

        music_dir = event.preferences['mpd_music_dir']
        if music_dir is '$XDG_MUSIC_HOME':
            music_dir = os.environ['XDG_MUSIC_DIR']

        self.__mpd_controller.set_music_dir(music_dir)
        self.__mpd_controller.set_mpd_host(event.preferences['mpd_hostname'])
        self.__mpd_controller.set_mpd_port(event.preferences['mpd_port'])


class MpdPreferencesUpdateEvent(EventListener):
    def __init__(self, mpd_controller):
        super(MpdPreferencesUpdateEvent, self).__init__()
        self.__mpd_controller = mpd_controller

    def on_event(self, event, extension):
        if event.id is 'mpd_music_dir':
            music_dir = event.new_value
            if music_dir is '$XDG_MUSIC_HOME':
                music_dir = os.environ['XDG_MUSIC_DIR']

            self.__mpd_controller.set_music_dir(music_dir)

        elif event.id is 'mpd_hostname':
            self.__mpd_controller.set_mpd_host(event.preferences['mpd_hostname'])
        elif event.id is 'mpd_port':
            self.__mpd_controller.set_mpd_port(event.preferences['mpd_port'])
