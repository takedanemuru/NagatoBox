
from gi.repository import Gtk
from libnagato.Object import NagatoObject

from libnagatodevelop.box.HeaderLabel import NagatoHeaderLabel
from libnagatodevelop.box.Spacer import NagatoSpacer
from libnagatodevelop.box.SpacerExpand import NagatoSpacerExpand


class NagatoGroup(NagatoObject, Gtk.Box):

    def _yuki_n_entry_changed(self, key):
        self._action_buttons.check_sensitive()
        self._on_entry_changed(key)

    def _set_header_label(self):
        pass

    def _set_contents(self):
        pass

    def _set_action_buttons(self):
        pass

    def _set_space_end(self):
        self.pack_start(NagatoSpacerExpand(self), True, True, 0)

    def _on_entry_changed(self, key):
        pass

    def _on_initialize(self):
        self._set_header_label()
        self.pack_start(NagatoHeaderLabel(self, self._label), False, False, 0)
        self.pack_start(NagatoSpacer(self), False, False, 0)
        self._set_contents()
        self._set_space_end()
        self._set_action_buttons()
        self.pack_start(self._action_buttons, False, False, 0)

    def __init__(self, parent):
        self._parent = parent
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)
        self._on_initialize()
