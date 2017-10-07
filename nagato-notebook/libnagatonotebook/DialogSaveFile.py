
from gi.repository import Gtk


class NagatoDialogSaveFile(object):

    _default_window = None

    @classmethod
    def set_default_window(cls, window):
        NagatoDialogSaveFile._default_window = window

    def _get_buttons(self):
        yuki_buttons = (
            "Cancel", Gtk.ResponseType.CANCEL,
            "Save", Gtk.ResponseType.ACCEPT
            )
        return yuki_buttons        

    def save_file(self):
        yuki_dialog = Gtk.FileChooserDialog(
            "Save your text file", 
            NagatoDialogSaveFile._default_window,
            Gtk.FileChooserAction.SAVE,
            self._get_buttons()
            )
        yuki_response = yuki_dialog.run()
        yuki_file_name = Gtk.FileChooser.get_filename(yuki_dialog)
        yuki_dialog.destroy()
        return yuki_file_name

    def __init__(self):
        pass
