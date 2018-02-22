
from gi.repository import Gtk


class NagatoIconChooser(Gtk.FileChooserDialog):

    @classmethod
    def call(self):
        yuki_dialog = NagatoIconChooser()
        yuki_response = yuki_dialog.run()
        yuki_path = yuki_dialog.get_filename()
        yuki_dialog.destroy()
        if yuki_response == Gtk.ResponseType.OK:
            return yuki_path
        return None

    def _get_file_filter(self):
        yuki_file_filter = Gtk.FileFilter()
        yuki_file_filter.set_name("images only")
        yuki_file_filter.add_mime_type("image/*")
        return yuki_file_filter

    def _get_buttons(self):
        yuki_buttons = (
            "Cancel",
            Gtk.ResponseType.CANCEL,
            "Select",
            Gtk.ResponseType.OK
            )
        return yuki_buttons

    def __init__(self):
        Gtk.FileChooserDialog.__init__(
            self,
            "Select Icon",
            Gtk.Window(title="Select Icon"),
            Gtk.FileChooserAction.OPEN,
            self._get_buttons()
            )
        self.add_filter(self._get_file_filter())
