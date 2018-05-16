
import os
from gi.repository import Gtk
from libnagatodevelop.box.entry.Entry import NagatoEntry
from libnagatodevelop.dialog.DirectoryChooser import NagatoDirectoryChooser

ICON_POSITION = Gtk.EntryIconPosition.SECONDARY
ICON_TOOLTIP = "Click to Open Dialog"


class NagatoDirectory(NagatoEntry):

    def _get_label_text(self):
        return "Project Directory"

    def _get_key(self):
        return "app-directory"

    def _on_press_icon(self, entry, icon_position, event):
        yuki_current_folder = self._model[self._get_key()]
        yuki_directory = NagatoDirectoryChooser.call(yuki_current_folder)
        if yuki_directory is None:
            return
        yuki_text = yuki_directory.replace(os.getenv("HOME"), "~")
        self._entry.set_text(yuki_text)
        self._model[self._get_key()] = yuki_directory

    def _addtional_setups(self):
        self._entry.set_editable(False)
        self._entry.set_icon_from_icon_name(ICON_POSITION, "folder")
        self._entry.connect("icon-press", self._on_press_icon)
        self._entry.set_icon_tooltip_text(ICON_POSITION, ICON_TOOLTIP)
