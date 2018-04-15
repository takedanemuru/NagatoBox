
from gi.repository import Gtk
from libnagatotext.dialog.FileChooser import NagatoFileChooser


class NagatoFileChooserSave(NagatoFileChooser):

    @classmethod
    def call(self, current_name="Untitled Document"):
        cls._dialog = NagatoFileChooserSave()
        cls._dialog.set_current_name(current_name)
        cls._dialog.set_do_overwrite_confirmation(True)
        return cls._get_path()

    def _set_variables(self):
        self._title = "Save File"
        self._action = Gtk.FileChooserAction.SAVE
        self._ok_button_title = "Save"
