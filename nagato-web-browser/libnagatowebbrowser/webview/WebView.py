
import gi

gi.require_version('WebKit2','4.0')

from gi.repository import GLib
from gi.repository import WebKit2
from libnagato.Object import NagatoObject


class NagatoWebView(WebKit2.WebView, NagatoObject):

    def _yuki_n_go_back(self):
        self.go_back()

    def _yuki_n_go_forward(self):
        self.go_forward()

    def _yuki_n_reload(self):
        self.reload()

    def _yuki_n_stop_loading(self):
        self.stop_loading()

    def _inform_can_go_back(self):
        return self.can_go_back()

    def _inform_can_go_forward(self):
        return self.can_go_forward()

    def _inform_can_stop_loading(self):
        return (self.get_estimated_load_progress() != 1)

    def _on_initialize(self):
        pass

    def __init__(self, parent, uri):
        # This class do not append webview to the self._parent
        # Do something in self._on_initialize()
        self._parent = parent
        self._uri = uri
        WebKit2.WebView.__init__(self)
        GLib.idle_add(self.load_uri, self._uri)
        self._on_initialize()
        self.show()
