
import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
from libnagatonotebook.CoreObject import NagatoObject
from libnagatonotebook.Grid import NagatoGrid
from libnagatonotebook import Pixbuf
from libnagatonotebook.DialogSaveFile import NagatoDialogSaveFile
from libnagatonotebook.ContextMenuApplication import NagatoContextMenuApplication


class NagatoWindow(Gtk.Window, NagatoObject):

    def _on_button_press(self, widget, event):
        if event.button == 3:
            self._context_menu.pop_up(event)

    def _yuki_n_file_save(self):
        pass
        #self._source_view.save()

    def _on_destroy(self, widget, event, user_data=None):
        Gtk.main_quit()

    def __init__(self):
        self._parent = None
        Gtk.Window.__init__(self)
        self.set_default_size(600, 400)
        self._context_menu = NagatoContextMenuApplication(self)
        self.connect("button-press-event", self._on_button_press)
        self.connect("delete-event", self._on_destroy)
        self.set_icon(Pixbuf.get_application_icon())
        NagatoDialogSaveFile.set_default_window(self)
        self._grid = NagatoGrid(self)
        self.show_all()
        Gtk.main()
