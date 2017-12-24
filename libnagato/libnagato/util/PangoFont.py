
from gi.repository import Pango


def get(font_description):
    yuki_font = Pango.font_description_from_string(font_description)
    return yuki_font
