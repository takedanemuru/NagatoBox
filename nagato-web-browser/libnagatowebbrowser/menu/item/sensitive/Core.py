
from gi.repository import Gtk
from libnagatowebbrowser.CoreObject import NagatoObject


class NagatoCore(Gtk.MenuItem, NagatoObject):

    def _on_activate(self, widget):
        self._raise(self._message)

    def _on_map(self, widget):
        yuki_sensitive = self._enquiry(self._query)
        self.set_sensitive(yuki_sensitive)

    def _initialize_variables(self):
        # this is a meaningless virtual method.
        self._title = ""
        self._query = ""
        self._message = ""

    def _connect_gtk_callbacks(self):
        self.connect("activate", self._on_activate)
        self.connect("map", self._on_map)

    def __init__(self, parent, root_menu):
        self._parent = parent
        self._initialize_variables()
        Gtk.MenuItem.__init__(self, self._title)
        self._connect_gtk_callbacks()
        self.get_style_context().add_class("menu-item")
        root_menu.append(self)
