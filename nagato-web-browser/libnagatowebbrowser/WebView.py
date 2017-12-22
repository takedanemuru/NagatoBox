
import gi

gi.require_version('WebKit2','4.0')
gi.require_version('WebKit2WebExtension', '4.0')

from gi.repository import Gtk
from gi.repository import WebKit2
from gi.repository import WebKit2WebExtension
from libnagatowebbrowser.CoreObject import NagatoObject
from libnagatowebbrowser.WebKit2Settings import NagatoWebKit2Settings
from libnagatowebbrowser.TabLabel import NagatoTabLabel
from libnagatowebbrowser.MouseBinds import NagatoMouseBinds


class NagatoWebView(WebKit2.WebView, NagatoObject):

    def _yuki_n_close_current_tab(self):
        self._parent.detach_tab(self)
        self._tab_label.destroy()
        self.destroy()

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

    def _on_create(self, web_view, navigation_action):
        yuki_request = navigation_action.get_request()
        yuki_uri = yuki_request.get_uri()
        self._raise("YUKI.N > create", yuki_uri)

    def _on_load_changed(self, web_view, load_event):
        if load_event == WebKit2.LoadEvent.FINISHED:
            self._tab_label.set_title(self.get_property("title"))
            self._raise("YUKI.N > load finished")

    def _connect_gtk_callbacks(self):
        self.connect("create", self._on_create)
        self.connect("load-changed", self._on_load_changed)

    def _initialize_web_view(self, uri):
        WebKit2.WebView.__init__(self)
        self._settings = NagatoWebKit2Settings()
        self.set_settings(self._settings)
        self._connect_gtk_callbacks()
        self.load_uri(uri)

    def _setup_tab(self):
        self._tab_label = NagatoTabLabel(self)
        self._parent.insert_page(self, self._tab_label, -1)
        self._parent.set_tab_reorderable(self, True)

    def __init__(self, parent, uri):
        self._parent = parent
        self._initialize_web_view(uri)
        self._setup_tab()
        NagatoMouseBinds(self)
        self.show()
