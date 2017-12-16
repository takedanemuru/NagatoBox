
from gi.repository import Gtk


class NagatoLabelWarning(Gtk.Label):

    def _get_single(self):
        yuki_message = \
            "<big><u>WARNING !!</u></big>\n"\
            "\n"\
            "Following process is still running.\n"\
            "Do you really want to close terminal ?\n"\
            "\n"
        return yuki_message

    def _get_multi(self):
        yuki_message = \
            "<big><u>WARNING !!</u></big>\n"\
            "\n"\
            "Following processes are still running.\n"\
            "Do you really want to close terminal ?\n"\
            "\n"
        return yuki_message

    def _get_message(self, length):
        return self._get_single() if length == 1 else self._get_multi()

    def _get_markup(self, processes):
        yuki_message = self._get_message(len(processes))
        return yuki_message + "\n".join(processes)

    def set_processes(self, processes):
        self.set_markup(self._get_markup(processes))

    def __init__(self, content_area):
        Gtk.Label.__init__(self)
        self.set_justify(Gtk.Justification.CENTER)
        self.set_vexpand(True)
        self.get_style_context().add_class("dialog-label")
        content_area.add(self)
