
from libnagato.util import PangoFont


class NagatoAttributes(object):

    def __init__(self, vte):
        vte.set_allow_bold(False)
        vte.set_scrollback_lines(-1)
        vte.set_font(PangoFont.get("Ubuntu Mono Regular 14"))
