
from gi.repository import Gtk


class NagatoFileChooser(Gtk.FileChooserDialog):

    @classmethod
    def call(self, current_folder=None):
        yuki_dialog = NagatoFileChooser()
        if current_folder is not None:
            yuki_dialog.set_current_folder(current_folder)
        yuki_response = yuki_dialog.run()
        yuki_path = yuki_dialog.get_filename()
        yuki_dialog.destroy()
        if yuki_response == Gtk.ResponseType.OK:
            return yuki_path
        return None

    def _get_buttons(self):
        yuki_buttons = (
            "Cancel",
            Gtk.ResponseType.CANCEL,
            "Select",
            Gtk.ResponseType.OK
            )
        return yuki_buttons

    def _get_action(self):
        # dummy
        return 0

    def _add_filetrs(self):
        self._filter = Gtk.FileFilter()
        self._filter.add_mime_type("text/*")
        self.add_filter(self._filter)

    def __init__(self):
        Gtk.FileChooserDialog.__init__(
            self,
            "Select File",
            Gtk.Window(title="Select File"),
            self._get_action(),
            self._get_buttons()
            )
        self._add_filetrs()