
from gi.repository import Gdk
from gi.repository import Gtk


SCRIPT = "document.title = window.getSelection().getRangeAt(0).toString()"
API =  "https://duckduckgo.com/?q={}+{}"


class NagatoSelection(object):

    def _yuki_n_search_selection(self, search_on):
        self._settings.enable_javascript()
        self.run_javascript(
            SCRIPT,
            None,
            self._on_get_selection_to_search,
            search_on
            )

    def _on_get_selection_to_search(self, webview, result, search_on):
        if self.run_javascript_finish(result) is not None:
            yuki_selection = self.get_property("title")
            yuki_query = API.format(search_on, yuki_selection)
            self._raise("YUKI.N > create", yuki_query)
        self._settings.disable_javascript()

    def _yuki_n_copy_selection(self):
        self._settings.enable_javascript()
        self.run_javascript(
            SCRIPT,
            None,
            self._on_get_selection_to_copy,
            None
            )

    def _on_get_selection_to_copy(self, webview, result, user_data=None):
        if self.run_javascript_finish(result) is not None:
            yuki_selection = self.get_property("title")
            yuki_display = Gdk.Display.get_default()
            yuki_clipboard = Gtk.Clipboard.get_default(yuki_display)
            # -1 means whole length of utf-8 string
            yuki_clipboard.set_text(yuki_selection, -1)
        self._settings.disable_javascript()
