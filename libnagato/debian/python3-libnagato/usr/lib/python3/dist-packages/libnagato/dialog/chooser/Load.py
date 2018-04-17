
from gi.repository import Gtk
from gi.repository import GLib
from gi.repository.GdkPixbuf import Pixbuf
from libnagato.dialog.chooser.Chooser import NagatoChooser

MIME_TYPE = "text/*"
FOLDER = GLib.get_home_dir()
SIZE = 256


class NagatoLoad(NagatoChooser):

    @classmethod
    def call(cls, folder=FOLDER, mime_type=MIME_TYPE):
        cls._dialog = NagatoLoad()
        cls._dialog.set_current_folder(folder)
        cls._dialog.add_filters(mime_type)
        cls._dialog.add_preview_widget()
        return cls._get_path()

    def _on_update_preview(self, file_chooser):
        try:
            yuki_path = self.get_preview_filename()
            yuki_pixbuf = Pixbuf.new_from_file_at_size(yuki_path, SIZE, SIZE)
            yuki_preview_widget = file_chooser.get_preview_widget()
            yuki_preview_widget.set_from_pixbuf(yuki_pixbuf)
            self.set_preview_widget_active(True)
        except:
            self.set_preview_widget_active(False)

    def add_preview_widget(self):
        self.set_preview_widget(Gtk.Image())
        self.connect("update-preview", self._on_update_preview)

    def add_filters(self, mime_type):
        yuki_filter = Gtk.FileFilter()
        yuki_filter.add_mime_type(mime_type)
        yuki_filter.set_name("mime type : {}".format(mime_type))
        self.add_filter(yuki_filter)

    def _set_variables(self):
        self._title = "Select File"
        self._action = Gtk.FileChooserAction.OPEN
        self._ok_button_title = "Select"
