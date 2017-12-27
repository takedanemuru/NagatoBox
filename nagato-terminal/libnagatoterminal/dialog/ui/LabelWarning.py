
from gi.repository import Gtk

TEMPLATE = \
    "<span size='large'><u>WARNING !!</u></span>\n"\
    "\n"\
    "Following {} still running.\n"\
    "Do you really want to close terminal ?\n"\
    "\n"


class NagatoLabelWarning(Gtk.Label):

    def _get_message(self, length):
        if length == 1:
            return TEMPLATE.format("process is")
        else:
            return TEMPLATE.format("processes are")

    def set_processes(self, processes):
        yuki_markup = self._get_message(len(processes))
        yuki_markup += "\n".join(processes)
        self.set_markup(yuki_markup)

    def __init__(self, content_area):
        Gtk.Label.__init__(self)
        self.set_justify(Gtk.Justification.CENTER)
        self.set_vexpand(True)
        self.get_style_context().add_class("dialog-label")
        content_area.add(self)
