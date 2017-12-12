
from gi.repository import Gtk
from libnagatoterminal.dialog import Portal
from libnagatoterminal.dialog.ui.LabelWarning import NagatoLabelWarning


class NagatoWarning(Gtk.Dialog):

    def _set_buttons(self):
        self.add_button("Cancel", Gtk.ResponseType.CANCEL)
        self.add_button("Close", Gtk.ResponseType.OK)

    def _initialize_content_area(self):
        yuki_content_area = self.get_content_area()
        yuki_content_area.set_spacing(8)
        yuki_content_area.set_border_width(8)
        self._label = NagatoLabelWarning(yuki_content_area)

    def set_processes(self, processes):
        self._label.set_processes(processes)

    def __init__(self):
        Gtk.Dialog.__init__(
            self,
            "dialog: warning",
            Portal.default_window,
            Gtk.ResponseType.CANCEL,
            None
            )
        self.set_default_size(300, 300)
        self._initialize_content_area()
        self._set_buttons()
        self.show_all()
