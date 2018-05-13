
from gi.repository import WebKit2
from libnagato.Object import NagatoObject

USER_AGENT_NAME = "nagato-web-browser"


class NagatoWebKit2Settings(WebKit2.Settings, NagatoObject):

    def disable_javascript(self):
        self.set_enable_javascript(False)

    def enable_javascript(self):
        self.set_enable_javascript(True)

    def toggle_javascript(self):
        yuki_toggle = not self.get_enable_javascript()
        self.set_enable_javascript(yuki_toggle)
        self._raise("YUKI.N > reload")

    def get_javascript_enabled(self):
        return self.get_enable_javascript()

    def __init__(self, parent):
        self._parent = parent
        WebKit2.Settings.__init__(self)
        self.set_enable_tabs_to_links(True)
        self.set_enable_javascript(False)
        self.set_enable_plugins(False)
        self.set_javascript_can_access_clipboard(False)
        self.set_enable_smooth_scrolling(False)
        self.set_enable_private_browsing(True)
        self.set_user_agent(USER_AGENT_NAME)
