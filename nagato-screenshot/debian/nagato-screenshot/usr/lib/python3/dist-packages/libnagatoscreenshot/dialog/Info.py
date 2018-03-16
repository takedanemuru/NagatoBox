
from gi.repository import Gtk


class NagatoInfo(Gtk.Dialog):

    def _get_title(self):
        return ""

    def _set_buttons(self):
        pass

    def _set_contents(self):
        pass

    def _set_user_data(self, user_data):
        pass

    def _initialize_content_area(self):
        self._content_area = self.get_content_area()
        self._content_area.set_spacing(8)
        self._content_area.set_border_width(8)

    def __init__(self, user_data=None):
        Gtk.Dialog.__init__(
            self,
            "dialog: {}".format(self._get_title()),
            Gtk.Window(title=self._get_title()),
            Gtk.ResponseType.OK,
            None
            )
        self.set_default_size(300, 300)
        self._user_data = user_data
        self._initialize_content_area()
        self._set_contents()
        self._set_buttons()
        self.show_all()
