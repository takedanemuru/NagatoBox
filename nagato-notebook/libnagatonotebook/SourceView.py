
import gi

gi.require_version("GtkSource", "3.0")

from gi.repository import GtkSource


class NagatoSourceView(GtkSource.View):

    def __init__(self, parent):
        self._parent = parent
        GtkSource.View.__init__(self)
        self.set_opacity(0.9)
        self._parent.add(self)
