
from gi.repository import Gtk
from gi.repository import Gdk
from libnagato.util import CssProvider
from libnagatodevelop.box.WithLabel import NagatoWithLabel


class NagatoIcon(NagatoWithLabel):

    def _get_label_text(self):
        return "Application Icon"

    def _on_set_css(self):
        CssProvider.set_to_widget(self, "shade-half")

    def _get_buttons(self):
        yuki_buttons = (
            "Cancel",
            Gtk.ResponseType.CANCEL,
            "Select",
            Gtk.ResponseType.OK
            )
        return yuki_buttons

    def _on_button_press(self, widget, event):
        yuki_dialog = Gtk.FileChooserDialog(
            "Select Icon",
            Gtk.Window(title="Select Icon"),
            Gtk.FileChooserAction.OPEN,
            self._get_buttons()
            )
        yuki_file_filter = Gtk.FileFilter()
        yuki_file_filter.set_name("images only")
        yuki_file_filter.add_mime_type("image/*")
        yuki_dialog.add_filter(yuki_file_filter)
        yuki_response = yuki_dialog.run()
        yuki_dialog.destroy()
        print(yuki_response)

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
