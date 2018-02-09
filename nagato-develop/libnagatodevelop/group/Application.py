
from libnagatodevelop.group.Group import NagatoGroup
from libnagatodevelop.box.entry.Directory import NagatoDirectory
from libnagatodevelop.box.Icon import NagatoIcon
from libnagatodevelop.eventbox.ForImage import NagatoEventBox
from libnagatodevelop.box.entry.MailAddress import NagatoMailAddress
from libnagatodevelop.box.entry.Uri import NagatoUri
from libnagatodevelop.box.entry.IdHeader import NagatoIdHeader
from libnagatodevelop.box.buttons.Application import NagatoButtons


class NagatoApplication(NagatoGroup):

    def _on_entry_changed(self, key):
        pass

    def _set_header_label(self):
        self._label = "APPLICATION"

    def _initialize_contents(self):
        pass

    def _set_contents(self):
        self._initialize_contents()
        self.pack_start(NagatoDirectory(self), False, False, 0)
        self.pack_start(NagatoEventBox(self), False, False, 0)
        self.pack_start(NagatoUri(self), False, False, 0)
        self.pack_start(NagatoIdHeader(self), False, False, 0)

    def _set_action_buttons(self):
        self._action_buttons = NagatoButtons(self)
