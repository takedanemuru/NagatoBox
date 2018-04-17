
from gi.repository import Gtk
from gi.repository import Pango
from libnagato.menu.Action import NagatoActionCore


class NagatoFont(NagatoActionCore):

    def _on_font_selected(self, font_description):
        yuki_font_family = font_description.get_family()
        yuki_font_size = font_description.get_size() / Pango.SCALE

    def _on_activate(self, widget):
        yuki_dialog = Gtk.FontChooserDialog(self._title, Gtk.Window())
        yuki_dialog.set_preview_text("YUKI.N > Can you see this ?")
        if Gtk.ResponseType.OK == yuki_dialog.run():
            self._on_font_selected(yuki_dialog.get_font_desc())
        yuki_dialog.destroy()

    def _on_map(self, widget):
        pass

    def _initialize_variables(self):
        self._title = "Select Font"
        self._query = ""
        self._message = ""
