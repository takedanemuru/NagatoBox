
from gi.repository import Gtk


class NagatoAddress(Gtk.Dialog):

    @classmethod
    def call(cls, uri):
        yuki_uri = ""
        yuki_dialog = NagatoAddress(uri)
        if Gtk.ResponseType.OK == yuki_dialog.run():
            yuki_uri = yuki_dialog.get_uri()
        yuki_dialog.destroy()
        return yuki_uri

    def _on_activate(self, widget, user_data=None):
        # This is GTK+ callback, all args are unused.
        self._go_button.clicked()

    def _set_buttons(self):
        self.add_button("Cancel", Gtk.ResponseType.CANCEL)
        self._go_button = self.add_button("Go", Gtk.ResponseType.OK)

    def _initialize_content_area(self, uri):
        yuki_content_area = self.get_content_area()
        yuki_content_area.set_spacing(16)
        yuki_content_area.set_border_width(16)
        self._entry = Gtk.Entry()
        self._entry.connect("activate", self._on_activate)
        self._entry.set_text(uri)
        yuki_content_area.add(self._entry)

    def get_uri(self):
        return self._entry.get_text()

    def __init__(self, user_data=None):
        Gtk.Dialog.__init__(
            self,
            "dialog: url",
            Gtk.Window(title="url"),
            Gtk.ResponseType.CANCEL,
            None
            )
        self.set_default_size(600, -1)
        self._initialize_content_area(user_data)
        self._set_buttons()
        self.show_all()
