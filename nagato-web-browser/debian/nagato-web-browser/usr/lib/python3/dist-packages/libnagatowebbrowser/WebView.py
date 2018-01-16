
import gi

gi.require_version('WebKit2','4.0')

from gi.repository import WebKit2
from libnagatowebbrowser.WebViewCore import NagatoWebViewCore
from libnagatowebbrowser.webview.Selection import NagatoSelection
from libnagatowebbrowser.webview.Snapshot import NagatoSnapshot
from libnagatowebbrowser.WebKit2Settings import NagatoWebKit2Settings
from libnagatowebbrowser.TabLabel import NagatoTabLabel
from libnagatowebbrowser.menu.context.ForWebView import NagatoForWebView
from libnagatowebbrowser.keyboard.Binds import NagatoBinds


class NagatoWebView(NagatoWebViewCore, NagatoSelection, NagatoSnapshot):

    def _yuki_n_close_current_tab(self):
        self._parent.detach_tab(self)
        self._tab_label.destroy()
        self.destroy()

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

    def _setup_tab(self):
        self._tab_label = NagatoTabLabel(self)
        yuki_page = self._parent.get_current_page()
        self._parent.insert_page(self, self._tab_label, yuki_page+1)
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
