
import gi

gi.require_version('WebKit2','4.0')

import threading
from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import WebKit2
from libnagato.Object import NagatoObject
from libnagatowebbrowser.WebKit2Settings import NagatoWebKit2Settings
from libnagatowebbrowser.TabLabel import NagatoTabLabel
from libnagatowebbrowser.menu.context.ForWebView import NagatoForWebView
from libnagatowebbrowser.keyboard.Binds import NagatoBinds


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
        else:
            self._tab_label.set_progress(self.get_estimated_load_progress())

    def _connect_gtk_callbacks(self):
        self.connect("create", self._on_create)
        self.connect("load-changed", self._on_load_changed)

    def _target_method(self):
        GLib.idle_add(self.load_uri, self._uri, priority=GLib.PRIORITY_LOW)

    def _setup_tab(self):
        self._tab_label = NagatoTabLabel(self)
        yuki_page = self._parent.get_current_page()
        self._parent.insert_page(self, self._tab_label, yuki_page+1)
        #self._parent.insert_page(self, self._tab_label, -1)
        self._parent.set_tab_reorderable(self, True)

    def _on_initialize(self):
        self._settings = NagatoWebKit2Settings()
        self.set_settings(self._settings)
        self._connect_gtk_callbacks()
        self._setup_tab()
        NagatoForWebView(self)
        NagatoBinds(self)

    def set_tab_size(self, new_tab_size):
        self._tab_label.set_tab_size(new_tab_size)

    def __init__(self, parent, uri):
        self._parent = parent
        self._uri = uri
        self._thread = threading.Thread(target=self._target_method)
        self._thread.daemon = True
        WebKit2.WebView.__init__(self)
        self._on_initialize()
        self._thread.start()
        self.show()
