
from gi.repository import Gtk


class NagatoDialogSaveFile(object):

    _default_window = None

    @classmethod
    def set_default_window(cls, window):
        NagatoDialogSaveFile._default_window = window

    def _get_buttons_for_save(self):
        yuki_buttons = (
            "Cancel", Gtk.ResponseType.CANCEL,
            "Save", Gtk.ResponseType.APPLY
            )
        return yuki_buttons

    def _get_buttons_for_open(self):
        yuki_buttons = (
            "Cancel", Gtk.ResponseType.CANCEL,
            "Open", Gtk.ResponseType.APPLY
            )
        return yuki_buttons

    def save_file(self):
        yuki_dialog = Gtk.FileChooserDialog(
            "Save your text file",
            NagatoDialogSaveFile._default_window,
            Gtk.FileChooserAction.SAVE,
            self._get_buttons_for_save()
            )
        yuki_response = yuki_dialog.run()
        yuki_file_name = Gtk.FileChooser.get_filename(yuki_dialog)
        yuki_dialog.destroy()
        return yuki_file_name

    def open_file(self):
        yuki_dialog = Gtk.FileChooserDialog(
            "Select File to Open",
            NagatoDialogSaveFile._default_window,
            Gtk.FileChooserAction.OPEN,
            self._get_buttons_for_open()
            )
        yuki_response = yuki_dialog.run()
        yuki_file_name = Gtk.FileChooser.get_filename(yuki_dialog)
        yuki_dialog.destroy()
        return yuki_file_name, yuki_response

    def __init__(self):
        pass
