
from libnagatoterminal.util import PangoFont


class NagatoVteAttributes(object):

    def __init__(self, vte):
        vte.set_allow_bold(False)
        vte.set_font(PangoFont.get("Ubuntu Mono Regular 14"))
