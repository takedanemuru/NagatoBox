
from gi.repository import Gtk
from gi.repository import Gdk


def set_to_widget(widget, css_class):
    widget.get_style_context().add_class(css_class)


def set_to_application(css):
    # css must be an ABSOLUTE PATH to css file
    yuki_css_provider = Gtk.CssProvider()
    yuki_css_provider.load_from_path(css)
    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        yuki_css_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
