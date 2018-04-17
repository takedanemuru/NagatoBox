
from gi.repository import Gtk

CANCEL = Gtk.ResponseType.CANCEL
OK = Gtk.ResponseType.OK


class NagatoChooser(Gtk.FileChooserDialog):

    @classmethod
    def _get_path(cls):
        yuki_response = cls._dialog.run()
        yuki_path = cls._dialog.get_filename()
        cls._dialog.destroy()
        if yuki_response == Gtk.ResponseType.OK:
            return yuki_path
        return None

    def _set_variables(self):
        self._title = "Select File"
        self._action = 0
        self._ok_button_title = "Select"

    def __init__(self):
        self._set_variables()
        Gtk.FileChooserDialog.__init__(
            self,
            self._title,
            Gtk.Window(),
            self._action,
            ("Cancel", CANCEL, self._ok_button_title, OK)
            )
