
from gi.repository import Gtk
from libnagato.dialog.ui.Label import NagatoLabel


class NagatoMessage(Gtk.Dialog):

    def _set_buttons(self, buttons):
        yuki_response_id = 0
        for button_text in buttons:
            self.add_button(button_text, yuki_response_id)
            yuki_response_id += 1

    def _set_contents(self, message):
        pass

    def _initialize_content_area(self):
        self._content_area = self.get_content_area()
        self._content_area.set_spacing(8)
        self._content_area.set_border_width(8)

    def __init__(self, title, message, pixbuf, buttons):
        Gtk.Dialog.__init__(
            self,
            "dialog: {}".format(title),
            Gtk.Window(),
            0,
            None
            )
        self.set_default_size(300, 300)
        self._initialize_content_area()
        self._set_contents(message)
        self._set_buttons(buttons)
        self.show_all()
