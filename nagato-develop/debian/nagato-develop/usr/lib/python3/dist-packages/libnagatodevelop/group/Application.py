
import os
from libnagatodevelop.group.Group import NagatoGroup
from libnagatodevelop.box.entry.Directory import NagatoDirectory
from libnagatodevelop.box.Icon import NagatoIcon
from libnagatodevelop.eventbox.ForImage import NagatoEventBox
from libnagatodevelop.box.entry.ApplicationName import NagatoApplicationName
from libnagatodevelop.box.entry.ApplicationId import NagatoApplicationId
from libnagatodevelop.box.entry.ApplicationUri import NagatoApplicationUri
from libnagatodevelop.box.buttons.Application import NagatoButtons


class NagatoApplication(NagatoGroup):

    def _set_application_name(self):
        yuki_model = self._enquiry("YUKI.N > model")
        yuki_text = os.path.basename(yuki_model["app-directory"])
        self._application_name.set_text(yuki_text)

    def _set_application_id(self):
        yuki_model = self._enquiry("YUKI.N > model")
        yuki_id = yuki_model["user-id"]
        if yuki_id == "":
            return
        yuki_text = "{0}.{1}".format(yuki_id, yuki_model["app-name"])
        self._application_id.set_text(yuki_text)

    def _on_entry_changed(self, key):
        if key == "app-directory":
            self._set_application_name()
        if key == "app-name":
            self._set_application_id()
        self._action_buttons.check_sensitive()

    def _set_header_label(self):
        self._label = "APPLICATION"

    def _initialize_contents(self):
        self._application_name = NagatoApplicationName(self)
        self._application_id = NagatoApplicationId(self)

    def _set_contents(self):
        self._initialize_contents()
        self.pack_start(NagatoDirectory(self), False, False, 0)
        self.pack_start(NagatoEventBox(self), False, False, 0)
        self.pack_start(self._application_name, False, False, 0)
        self.pack_start(self._application_id, False, False, 0)
        self.pack_start(NagatoApplicationUri(self), False, False, 0)

    def _set_action_buttons(self):
        self._action_buttons = NagatoButtons(self)
