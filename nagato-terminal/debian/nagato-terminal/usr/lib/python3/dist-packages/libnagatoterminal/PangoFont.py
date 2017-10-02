
from gi.repository import Pango


def Get(arg_font_description):
    yuki_font = Pango.font_description_from_string(arg_font_description)
    return yuki_font
