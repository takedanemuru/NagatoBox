
from gi.repository import Pango
from gi.repository import PangoCairo
from libnagato.Object import NagatoObject

FONT = "Ubuntu Mono 15"
MARKUP = "CPU:\nMemory:\nSwap:\nProcesses:\nThermal:"
ALIGN = Pango.Alignment.LEFT


class NagatoHeaderLabels(NagatoObject):

    def _get_pango_layout(self, cairo_context):
        yuki_layout = PangoCairo.create_layout(cairo_context)
        yuki_layout.set_height(Pango.SCALE*180)
        yuki_layout.set_width(Pango.SCALE*180)
        yuki_layout.set_spacing(Pango.SCALE*5)
        yuki_layout.set_alignment(ALIGN)
        yuki_layout.set_markup(MARKUP, -1)
        yuki_font_description = Pango.font_description_from_string(FONT)
        yuki_layout.set_font_description(yuki_font_description)
        return yuki_layout

    def paint(self, cairo_context):
        cairo_context.set_source_rgb(0.5, 0.5, 0.5)
        yuki_layout = self._get_pango_layout(cairo_context)
        PangoCairo.update_layout(cairo_context, yuki_layout)
        PangoCairo.show_layout(cairo_context, yuki_layout)

    def __init__(self, parent):
        self._parent = parent
