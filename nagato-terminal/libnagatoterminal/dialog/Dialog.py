
from gi.repository import Gtk


class NagatoDialog(Gtk.Dialog):

    _default_window = None

    @classmethod
    def set_default_window(cls, window):
        NagatoDialog._default_window = window

    def _set_buttons(self):
        self.add_button("Cancel", Gtk.ResponseType.CANCEL)
        self.add_button("Close", Gtk.ResponseType.OK)

    def _set_label(self):
        yuki_message = \
            "<big><u>WARNING !!</u></big>\n"\
            "\n"\
            "Child process is running.\n"\
            "Do you really want to close terminal ?\n"
        self._label = Gtk.Label()
        self._label.set_markup(yuki_message)
        self._label.set_justify(Gtk.Justification.CENTER)
        self._label.set_vexpand(True)
        self._label.set_opacity(0.7)
        self._label.get_style_context().add_class("dialog-label")
        self.get_content_area().add(self._label)

    def __init__(self):
        Gtk.Dialog.__init__(
            self,
            "dialog: warning",
            NagatoDialog._default_window,
            Gtk.ResponseType.CANCEL,
            None)
        self.set_default_size(300, 300)
        yuki_gtk_box = self.get_content_area()
        yuki_gtk_box.set_spacing(8)
        yuki_gtk_box.set_border_width(8)
        self._set_buttons()
        self._set_label()
        self.show_all()
