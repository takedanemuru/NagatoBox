
from gi.repository import Gtk


class NagatoDirectoryChooser(Gtk.FileChooserDialog):

    @classmethod
    def call(self, current_folder=None):
        yuki_dialog = NagatoDirectoryChooser()
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

    def __init__(self):
        Gtk.FileChooserDialog.__init__(
            self,
            "Select Directory",
            Gtk.Window(title="Select Directory"),
            Gtk.FileChooserAction.SELECT_FOLDER,
            self._get_buttons()
            )

