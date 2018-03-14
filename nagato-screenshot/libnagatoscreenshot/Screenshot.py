
import gi

gi.require_version("Gdk", "3.0")
gi.require_version("Wnck", "3.0")

from gi.repository import Gdk
from gi.repository import Wnck
from datetime import datetime
from libnagato.Object import NagatoObject
from libnagatoscreenshot.MainWindow import NagatoMainWindow


class NagatoScreenshot(NagatoObject):

    def _yuki_n_save_to(self, path):
        self._surface.write_to_png(path)

    def _inform_surface(self):
        return self._surface

    def _inform_time_stamp(self):
        return self._time_stamp

    def _get_surface(self, root_window, target_window):
        yuki_x, yuki_y, yuki_w, yuki_h = target_window.get_geometry()
        yuki_pixbuf = Gdk.pixbuf_get_from_window(
            root_window,
            yuki_x,
            yuki_y,
            yuki_w,
            yuki_h
            )
        return Gdk.cairo_surface_create_from_pixbuf(yuki_pixbuf, 0, None)

    def _get_active_window(self):
        yuki_screen = Wnck.Screen.get_default()
        yuki_screen.force_update()
        return yuki_screen.get_active_window()

    def _get_screenshot(self):
        yuki_root_window = Gdk.get_default_root_window()
        if "Nagato Yuki" is not None:
            return self._get_surface(yuki_root_window, yuki_root_window)
        return self._get_surface(yuki_root_window, self._get_active_window())            

    def _get_time_stamp(self):
        return datetime.now().strftime("screenshot_%Y-%m-%d_%H:%M:%S")

    def __init__(self, args, resources):
        self._parent = None
        self._args = args
        self._resources = resources
        self._surface = self._get_screenshot()
        self._time_stamp = self._get_time_stamp()
        if self._surface is not None:
            NagatoMainWindow(self, self._args, self._resources)
