
from gi.repository import Gtk
from libnagatowebbrowser.CoreObject import NagatoObject


class NagatoItem2(Gtk.MenuItem, NagatoObject):

    def _on_activate(self, widget):
        self._raise(self._message, self._user_data)

    def _append_to_container(self, container=None):
        yuki_container = self._parent if container is None else container
        yuki_container.append(self)

    def __init__(self, parent, **kwargs):
        self._parent = parent
        Gtk.MenuItem.__init__(self, kwargs["label"])
        self.connect("activate", self._on_activate)
        self._message = kwargs["message"]
        if "user_data" in kwargs:
            self._user_data = kwargs["user_data"]
        else:
            self._user_data = None
        self._append_to_container(kwargs["container"])
