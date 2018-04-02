
from gi.repository import Gtk


class NagatoFileChooserSave(Gtk.FileChooserDialog):

    @classmethod
    def call(self, current_name="Untitled Document"):
        yuki_dialog = NagatoFileChooserSave()
        yuki_dialog.set_current_name(current_name)
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
            "Save",
            Gtk.ResponseType.OK
            )
        return yuki_buttons

    def __init__(self):
        Gtk.FileChooserDialog.__init__(
            self,
            "Save File",
            Gtk.Window(title="Save File"),
            Gtk.FileChooserAction.SAVE,
            self._get_buttons()
            )
        self.set_do_overwrite_confirmation(True)
