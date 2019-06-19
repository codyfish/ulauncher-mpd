from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

import MpdController


class MpdExtension(Extension):

    def __init__(self):
        super(MpdExtension, self).__init__()

        mpd_controller = MpdController.MpdController()

        self.subscribe(KeywordQueryEvent, MpdKeywordQueryListener(mpd_controller))
        self.subscribe(ItemEnterEvent, MpdItemEnterListener(mpd_controller))


class MpdKeywordQueryListener(EventListener):

    def __init__(self, mpd_controller):
        super(MpdKeywordQueryListener, self).__init__()

        self.__mpd_controller = mpd_controller

    def on_event(self, event, extension):
        return self.__mpd_controller.query(event.get_argument())


class MpdItemEnterListener(EventListener):

    def __init__(self, mpd_controller):
        super(MpdItemEnterListener, self).__init__()
        self.__mpd_controller = mpd_controller

    def on_event(self, event, extension):

        command = event.get_data()
        self.__mpd_controller.execute(command)


if __name__ == '__main__':
    MpdExtension().run()
