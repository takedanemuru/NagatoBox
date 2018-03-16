
import gi

gi.require_version("Gdk", "3.0")
gi.require_version("Wnck", "3.0")

from gi.repository import Gdk
from gi.repository import Wnck


class NagatoWindowSurface(object):

    def _get_pixbuf(self, root_window, target_window):
        yuki_x, yuki_y, yuki_w, yuki_h = target_window.get_geometry()
        yuki_pixbuf = Gdk.pixbuf_get_from_window(
            root_window,
            yuki_x,
            yuki_y,
            yuki_w,
            yuki_h
            )
        return yuki_pixbuf

    def _set_surface(self, root_window, target_window):
        self._surface= Gdk.cairo_surface_create_from_pixbuf(
            self._get_pixbuf(root_window, target_window),
            0,
            None
            )

    def _get_active_window(self):
        yuki_screen = Wnck.Screen.get_default()
        yuki_screen.force_update()
        return yuki_screen.get_active_window()

    def save_to(self, path):
        self._surface.write_to_png(path)

    def get_surface(self):
        return self._surface

    def __init__(self, focused_only):
        yuki_root = Gdk.get_default_root_window()
        self._surface = None
        yuki_target = self._get_active_window() if focused_only else yuki_root
        if yuki_target is not None:
            self._set_surface(yuki_root, yuki_target)
