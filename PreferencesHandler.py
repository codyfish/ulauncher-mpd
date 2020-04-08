from ulauncher.api.client.EventListener import EventListener

import os


def get_music_dir(music_dir):
    if music_dir == '$XDG_MUSIC_HOME' or music_dir.strip() == "":
        if 'XDG_MUSIC_DIR' in os.environ:
            music_dir = os.environ['XDG_MUSIC_DIR']
        else:
            print("assuming music dir is ~/music. To change this, set music_path in the configuration section")
            music_dir = os.environ['HOME'] + "/music"
    return music_dir


class MpdPreferencesEvent(EventListener):
    def __init__(self, mpd_controller):
        super(MpdPreferencesEvent, self).__init__()
        self.__mpd_controller = mpd_controller

    def on_event(self, event, extension):
        music_dir = event.preferences['mpd_music_dir']

        music_dir = get_music_dir(music_dir)

        self.__mpd_controller.set_music_dir(music_dir)

        self.__mpd_controller.set_music_dir(music_dir)
        self.__mpd_controller.set_mpd_host(event.preferences['mpd_hostname'])
        self.__mpd_controller.set_mpd_port(event.preferences['mpd_port'])
        self.__mpd_controller.set_default_volume_dif(event.preferences['volume_default_dif'])


class MpdPreferencesUpdateEvent(EventListener):
    def __init__(self, mpd_controller):
        super(MpdPreferencesUpdateEvent, self).__init__()
        self.__mpd_controller = mpd_controller

    def on_event(self, event, extension):
        if event.id == 'mpd_music_dir':
            music_dir = event.new_value
            music_dir = get_music_dir(music_dir)
            self.__mpd_controller.set_music_dir(music_dir)

        elif event.id == 'mpd_hostname':
            self.__mpd_controller.set_mpd_host(event.new_value)
        elif event.id == 'mpd_port':
            self.__mpd_controller.set_mpd_port(event.new_value)
        elif event.id == 'volume_default_dif':
            self.__mpd_controller.set_default_volume_dif(event.new_value)
