
import gi

gi.require_version('GSound', '1.0')

from gi.repository import GSound


class NagatoGSound(GSound.Context):

    def play(self, sound_name):
        self.play_simple({GSound.ATTR_EVENT_ID: sound_name})

    def __init__(self):
        GSound.Context.__init__(self)
        self.init()
