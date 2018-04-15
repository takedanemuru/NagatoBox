
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoCheck(Gtk.CheckMenuItem, NagatoObject):

    def _on_activate(self):
        self._raise(self._message)

    def _on_toggled(self, widget):
        if not self._lock:
            self._on_activate()

    def _set_active_without_signal(self, active):
        self._lock = True
        self.set_active(active)
        self._lock = False

    def _on_map(self, widget):
        yuki_active = self._enquiry(self._query, self._data)
        self._set_active_without_signal(yuki_active)

    def _initialize_variables(self, user_data=None):
        # this is a meaningless virtual method.
        self._title = ""
        self._query = ""
        self._data = None
        self._message = ""

    def _connect_gtk_callbacks(self):
        self.connect("toggled", self._on_toggled)
        self.connect("map", self._on_map)

    def __init__(self, parent, user_data=None):
        self._parent = parent
        self._initialize_variables(user_data)
        Gtk.MenuItem.__init__(self, self._title)
        self._connect_gtk_callbacks()
        self._parent.append(self)
        self._lock = False
