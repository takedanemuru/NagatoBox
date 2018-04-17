
from gi.repository import Gtk
from libnagato.dialog.chooser.Chooser import NagatoChooser


class NagatoSave(NagatoChooser):

    @classmethod
    def call(cls, current_name="Untitled Document"):
        cls._dialog = NagatoSave()
        cls._dialog.set_current_name(current_name)
        cls._dialog.set_do_overwrite_confirmation(True)
        return cls._get_path()

    def _set_variables(self):
        self._title = "Save File"
        self._action = Gtk.FileChooserAction.SAVE
        self._ok_button_title = "Save"
