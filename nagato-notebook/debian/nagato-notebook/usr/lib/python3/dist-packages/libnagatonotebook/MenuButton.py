
from gi.repository import Gtk
from libnagatonotebook.CoreObject import NagatoObject


class NagatoMenuButton(Gtk.Button, NagatoObject):

    def _on_activate(self, button):
        self._raise(self._message)

    def _get_image(self):
        yuki_image = Gtk.Image.new_from_icon_name(
            self._icon_name,
            Gtk.IconSize.MENU
            )
        yuki_image.set_opacity(0.7)
        return yuki_image

    def _initialize_variants(self):
        self._icon_name = ""
        self._tooltip_text = ""
        self._message = ""

    def _set_attributes(self):
        self.set_border_width(0)
        self.set_image(self._get_image())
        self.set_always_show_image(True)
        self.set_tooltip_text(self._tooltip_text)

    def __init__(self, parent):
        self._parent = parent
        self._initialize_variants()
        Gtk.Button.__init__(self)
        self.set_opacity(0.7)
        self._set_attributes()
        self.connect("clicked", self._on_activate)
        self._parent.pack_start(self, False, False, 0)
