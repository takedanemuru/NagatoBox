
from libnagatodevelop.group.Group import NagatoGroup
from libnagatodevelop.box.entry.UserName import NagatoUserName
from libnagatodevelop.box.entry.MailAddress import NagatoMailAddress
from libnagatodevelop.box.entry.Uri import NagatoUri
from libnagatodevelop.box.entry.IdHeader import NagatoIdHeader
from libnagatodevelop.box.buttons.Author import NagatoButtons


class NagatoAuthor(NagatoGroup):

    def _on_entry_changed(self, key):
        if key == "user-uri":
            yuki_model = self._enquiry("YUKI.N > model")
            yuki_model["app-uri"] = yuki_model["user-uri"]
        self._action_buttons.check_sensitive()

    def _set_header_label(self):
        self._label = "AUTHOR"

    def _set_contents(self):
        self.pack_start(NagatoUserName(self), False, False, 0)
        self.pack_start(NagatoMailAddress(self), False, False, 0)
        self.pack_start(NagatoUri(self), False, False, 0)
        self.pack_start(NagatoIdHeader(self), False, False, 0)

    def _set_action_buttons(self):
        self._action_buttons = NagatoButtons(self)
