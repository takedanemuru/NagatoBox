
from gi.repository import Gdk
from libnagato.util import PangoFont


class NagatoVteAttributes(object):

    def __init__(self, vte):
        vte.set_allow_bold(False)
        vte.set_scrollback_lines(-1)
        vte.set_color_foreground(Gdk.RGBA(0.6, 0.1, 1))
        vte.set_color_background(Gdk.RGBA(0, 0, 0))
        vte.set_font(PangoFont.get("Ubuntu Mono Regular 14"))
