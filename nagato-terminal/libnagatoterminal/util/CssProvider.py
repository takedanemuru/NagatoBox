import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk
from libnagatoterminal.util import Path


def set_to_application():
    yuki_css_provider = Gtk.CssProvider()
    yuki_path = Path.get_absolute("../resources/nagato-terminal.css")
    yuki_css_provider.load_from_path(yuki_path)
    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        yuki_css_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
