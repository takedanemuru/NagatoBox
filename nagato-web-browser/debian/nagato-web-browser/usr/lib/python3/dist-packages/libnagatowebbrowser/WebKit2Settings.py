
import gi

gi.require_version('WebKit2','4.0')

from gi.repository import WebKit2
from libnagatowebbrowser.CoreObject import NagatoObject

USER_AGENT_NAME = "nagato-web-browser"


class NagatoWebKit2Settings(WebKit2.Settings, NagatoObject):

    def __init__(self):
        WebKit2.Settings.__init__(self)
        self.set_enable_tabs_to_links(True)
        self.set_enable_javascript(False)
        self.set_enable_plugins(False)
        self.set_enable_plugins(False)
        self.set_user_agent(USER_AGENT_NAME)
