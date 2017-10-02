
from gi.repository import Gtk
from libnagatoterminal.CoreObject import NagatoObject
from libnagatoterminal import GdkPixbufIcon
from libnagatoterminal.Dialog import NagatoDialog
from libnagatoterminal.Grid import NagatoGrid
from libnagatoterminal.AboutDialog2 import NagatoAboutDialog2
from libnagatoterminal.Settings import NagatoSettings


class NagatoWindow(Gtk.Window, NagatoObject):

    def _can_close(self):
        if self._grid.can_close_all_chilren:
            return True
        else:
            yuki_dialog = NagatoDialog(self)
            yuki_response = yuki_dialog.run()
            yuki_dialog.destroy()
            return (yuki_response == Gtk.ResponseType.OK)

    def _try_quit_application(self):
        if self._can_close():
            Gtk.main_quit()
            print("YUKI.N > また図書館に…")
            yuki_w, yuki_h = self.get_size()
            yuki_x, yuki_y = self.get_position()
            self._settings.save_window_rect(
                yuki_x,
                yuki_y,
                yuki_w,
                yuki_h
                )
            return False
        return True

    def _on_close_window(self, widget, event, user_data=None):
        return self._try_quit_application()

    def _yuki_n_quit(self):
        self._try_quit_application()

    def _yuki_n_about(self):
        yuki_dialog = NagatoAboutDialog2()
        yuki_response = yuki_dialog.run()
        yuki_dialog.destroy()

    def _initialize_window(self):
        Gtk.Window.__init__(self)
        self.set_title("YUKI.N > ...")
        self.set_icon(GdkPixbufIcon.get_application_icon())
        self.connect("delete-event", self._on_close_window)
        yuki_rect = self._settings.load_window_rect()
        if yuki_rect is not None:
            self.move(yuki_rect.left, yuki_rect.top)
            self.set_default_size(yuki_rect.width, yuki_rect.height)

    def __init__(self):
        self._parent = None
        self._settings = NagatoSettings()
        self._initialize_window()
        self._grid = NagatoGrid(self)
        self.add(self._grid)
        self.show_all()
        Gtk.main()
