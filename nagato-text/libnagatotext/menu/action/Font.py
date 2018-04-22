
from gi.repository import Gtk
from libnagato.menu.Action import NagatoActionCore


class NagatoFont(NagatoActionCore):

    def _on_activate(self, widget):
        yuki_dialog = Gtk.FontChooserDialog(self._title, Gtk.Window())
        yuki_dialog.set_preview_text("YUKI.N > Can you see this ?")
        yuki_current_font = self._enquiry("YUKI.N > config", ("css", "font"))
        yuki_dialog.set_font(yuki_current_font)
        if Gtk.ResponseType.OK == yuki_dialog.run():
            yuki_data = "css", "font", yuki_dialog.get_font()
            self._raise("YUKI.N > config", yuki_data)
        yuki_dialog.destroy()

    def _on_map(self, widget):
        pass

    def _initialize_variables(self):
        self._title = "Select Font"
        self._query = ""
        self._message = ""
