
from gi.repository import Gtk
from libnagatodevelop.group.Group import NagatoGroup
from libnagatodevelop.box.DescriptionLabel import NagatoDescriptionLabel
from libnagatodevelop.box.buttons.Description import NagatoButtons
from libnagatodevelop.box.SingleEntry import NagatoSingleEntry
from libnagatodevelop.box.Spacer import NagatoSpacer
from libnagatodevelop.group.LongDescription import NagatoLongDescription

SHORT = "Short Description : "


class NagatoDescription(NagatoGroup):

    def _set_header_label(self):
        self._label = "DESCRIPTION"

    def _on_entry_changed(self, key):
        self._action_buttons.check_sensitive()

    def _initialize_contents(self):
        self._long_description = NagatoLongDescription(self)

    def _set_contents(self):
        self._initialize_contents()
        self.pack_start(NagatoDescriptionLabel(self, SHORT), False, False, 0)
        self.pack_start(NagatoSingleEntry(self), False, False, 0)
        self.pack_start(NagatoSpacer(self), False, False, 0)
        self.pack_start(self._long_description, False, False, 0)

    def _set_action_buttons(self):
        self._action_buttons = NagatoButtons(self)
