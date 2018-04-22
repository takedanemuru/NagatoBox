
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoViewConfig(NagatoObject):

    def _get_config(self, key):
        yuki_data = "sourceview", key
        return self._enquiry("YUKI.N > config", yuki_data)

    def _refresh(self):
        self._parent.set_hscroll_policy(Gtk.ScrollablePolicy.NATURAL)
        self._parent.set_vscroll_policy(Gtk.ScrollablePolicy.NATURAL)
        yuki_show_line_numbers = self._get_config("show_line_numbers")
        self._parent.set_show_line_numbers(yuki_show_line_numbers == "yes")
        self._parent.set_wrap_mode(self._get_config("wrap_mode"))
        self._parent.set_show_right_margin(True)
        self._parent.set_right_margin_position(80)
        self._parent.set_auto_indent(True)
        self._parent.set_indent_width(4)
        self._parent.set_insert_spaces_instead_of_tabs(True)
        self._parent.set_smart_backspace(True)
        self._parent.set_highlight_current_line(True)

    def refresh(self):
        self._refresh()

    def __init__(self, parent):
        self._parent = parent
        self._refresh()
