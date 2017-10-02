
from gi.repository import Gtk
from libnagatowebbrowser.CoreObject import NagatoObject

class NagatoToolBar(Gtk.Box, NagatoObject):

    def _initialize_go_back_button(self):
        self._go_back_button = Gtk.Button.new_from_icon_name(
            "go-previous-symbolic",
            Gtk.IconSize.BUTTON
            )
        self.pack_start(self._go_back_button, False, True, 0)

    def _initialize_uri_box(self):
        self._uri_box = Gtk.Entry()
        self._uri_box.set_hexpand(True)
        self._uri_box.set_has_frame(False)
        self._uri_box.set_icon_from_icon_name(
            Gtk.EntryIconPosition.SECONDARY,
            "view-refresh-symbolic"
            )
        self.pack_start(self._uri_box, True, True, 0)

    def set_uri(self, uri):
        self._uri_box.set_text(uri)

    def __init__(self, parent):
        self._parent = parent
        Gtk.Box.__init__(self)
        self.set_opacity(0.9)
        #self._initialize_go_back_button()
        self._initialize_uri_box()
        self._parent.attach(self, 0, 0, 1, 1)
