
from gi.repository import Gtk
from gi.repository import Gdk
from libnagato.menu.Action import NagatoActionCore


class NagatoColor(NagatoActionCore):

    def _get_current_rgba(self):
        yuki_color_value = self._enquiry(self._message, self._query)
        yuki_gdk_rgba = Gdk.RGBA()
        yuki_gdk_rgba.parse(yuki_color_value)
        return yuki_gdk_rgba

    def _on_activate(self, widget):
        yuki_dialog = Gtk.ColorSelectionDialog.new(self._title)
        yuki_color_selection = yuki_dialog.get_color_selection()
        yuki_color_selection.set_current_rgba(self._get_current_rgba())
        if yuki_dialog.run() == Gtk.ResponseType.OK:
            yuki_rgba = yuki_color_selection.get_current_rgba()
            yuki_data = self._query + (yuki_rgba.to_string(),)
            self._raise(self._message, yuki_data)
        yuki_dialog.destroy()

    def _on_map(self, widget):
        pass

    def _initialize_variables(self):
        pass
