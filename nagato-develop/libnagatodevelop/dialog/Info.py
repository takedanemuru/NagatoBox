
from gi.repository import Gtk
from libnagatodevelop.dialog.label.ForInfo import NagatoDialogLabel


class NagatoInfo(Gtk.Dialog):

    @classmethod
    def call(cls, title, markup):
        yuki_dialog = NagatoInfo(title, markup)
        yuki_dialog.run()
        yuki_dialog.destroy()
        return True

    def _set_buttons(self):
        self.add_button("OK", Gtk.ResponseType.OK)

    def _set_contents(self, markup):
        NagatoDialogLabel(self._content_area, markup)

    def _initialize_content_area(self):
        self._content_area = self.get_content_area()
        self._content_area.set_spacing(8)
        self._content_area.set_border_width(8)

    def __init__(self, title, markup):
        Gtk.Dialog.__init__(
            self,
            "dialog: {}".format(title),
            Gtk.Window(title=title),
            Gtk.ResponseType.OK,
            None
            )
        self.set_default_size(300, 300)
        self._initialize_content_area()
        self._set_contents(markup)
        self._set_buttons()
        self.show_all()
