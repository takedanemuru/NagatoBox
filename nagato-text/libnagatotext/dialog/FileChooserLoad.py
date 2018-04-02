
from gi.repository import Gtk
from libnagatotext.dialog.FileChooser import NagatoFileChooser


class NagatoFileChooserLoad(NagatoFileChooser):

    def _get_action(self):
        return Gtk.FileChooserAction.OPEN
