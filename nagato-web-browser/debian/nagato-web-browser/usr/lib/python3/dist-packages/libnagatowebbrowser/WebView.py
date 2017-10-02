import gi

gi.require_version('WebKit2','4.0')

from gi.repository import WebKit2
from libnagatowebbrowser.CoreObject import NagatoObject
from libnagatowebbrowser.WebKit2Settings import NagatoWebKit2Settings
from libnagatowebbrowser.TabLabel import NagatoTabLabel


class NagatoWebView(WebKit2.WebView, NagatoObject):

    def _yuki_n_request_close_tab(self):
        self._parent.detach_tab(self)
        self._tab_label.destroy()
        self.destroy()
        self._parent.set_show_tabs(self._parent.get_n_pages() > 1)

    def _on_create(self, web_view, navigation_action):
        yuki_request = navigation_action.get_request()
        yuki_uri = yuki_request.get_uri()
        self._raise("YUKI.N > create", yuki_uri)

    def _on_load_finished(self):
        self._raise("YUKI.N > load finished", self._position)

    def _on_load_changed(self, web_view, load_event):
        self._tab_label.set_title(self.get_property("title"))
        if load_event == WebKit2.LoadEvent.STARTED:
            pass
        elif load_event == WebKit2.LoadEvent.REDIRECTED:
            pass
        elif load_event == WebKit2.LoadEvent.COMMITTED:
            pass
        elif load_event == WebKit2.LoadEvent.FINISHED:
            self._on_load_finished()

    def _initialize_web_view(self, uri):
        WebKit2.WebView.__init__(self)
        self._settings = NagatoWebKit2Settings()
        self.set_settings(self._settings)
        self.connect("create", self._on_create)
        self.connect("load-changed", self._on_load_changed)
        self.load_uri(uri)
        self.set_property("expand", True)

    def _setup_tab(self):
        self._tab_label = NagatoTabLabel(self)
        self._page_index = self._parent.insert_page(self, self._tab_label, -1)
        self._parent.set_tab_reorderable(self, True)
        self._parent.set_show_tabs(self._parent.get_n_pages() > 1)

    def __init__(self, parent, uri):
        self._parent = parent
        self._position = 0
        self._initialize_web_view(uri)
        self._setup_tab()

    def set_position(self, position):
        self._position = position

    @property
    def page_data(self):
        yuki_data = (
            self._position,
            self.get_property("title"), 
            self.get_uri()
        )
        return yuki_data
