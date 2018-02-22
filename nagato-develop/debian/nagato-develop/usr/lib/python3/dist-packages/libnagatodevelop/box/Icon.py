
from gi.repository import Gtk
from gi.repository import Gdk
from libnagato.util import CssProvider
from libnagatodevelop.box.WithLabel import NagatoWithLabel
from libnagatodevelop.dialog.IconChooser import NagatoIconChooser
from libnagatodevelop.IconImage import NagatoIconImage


class NagatoIcon(NagatoWithLabel):

    def _get_label_text(self):
        return "Application Icon"

    def _get_key(self):
        return "app-icon"

    def _on_set_css(self):
        CssProvider.set_to_widget(self, "shade-half")

    def _on_button_press(self, widget, event):
        yuki_path = NagatoIconChooser.call()
        if yuki_path is None:
            return
        yuki_icon = NagatoIconImage(yuki_path)
        self._image.set_from_pixbuf(yuki_icon.get_scaled(256))
        self._model[self._get_key()] = yuki_path

    def _set_button_press_event(self):
        self._parent.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self._parent.connect("button-press-event", self._on_button_press)

    def _set_content(self):
        self._set_button_press_event()
        self._image = Gtk.Image()
        self._image.set_size_request(64, 64)
        self._image.set_alignment(1, 0.5)
        yuki_resources = self._enquiry("YUKI.N > resources")
        self._image.set_from_pixbuf(yuki_resources.get_application_icon())
        self.pack_start(self._image, False, True, 8)
