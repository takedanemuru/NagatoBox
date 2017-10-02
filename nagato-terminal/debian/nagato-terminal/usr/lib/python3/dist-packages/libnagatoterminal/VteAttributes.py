
from libnagatoterminal import RgbaColor
from libnagatoterminal import PangoFont


class NagatoVteAttributes(object):

    def __init__(self, vte):
        vte.set_allow_bold(False)
        vte.set_color_background(RgbaColor.get_color(0, 0, 0, 0.9))
        vte.set_color_foreground(RgbaColor.get("#A76FDE"))
        vte.set_font(PangoFont.Get("Ubuntu Mono Regular 14"))
        vte.set_hexpand(True)
        vte.set_vexpand(True)
        vte.set_opacity(0.8)
