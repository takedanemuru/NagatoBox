
from gi.repository import Pango
from gi.repository import PangoCairo
from libnagato.Object import NagatoObject

FONT = "Ubuntu Mono 15"
MARKUP = "{:.2%}\n{:.2%}\n{:.2%}\n{}\n°C"


class NagatoStatusLabels(NagatoObject):

    def _get_align(self):
        return Pango.Alignment.RIGHT

    def _get_markup(self):
        yuki_data = self._enquiry("YUKI.N > status")
        if yuki_data is None:
            return ""
        return MARKUP.format(
            yuki_data["cpu"],
            yuki_data["memory"],
            yuki_data["swap"],
            yuki_data["count"]
            )

    def _get_pango_layout(self, cairo_context):
        yuki_layout = PangoCairo.create_layout(cairo_context)
        yuki_layout.set_height(Pango.SCALE*180)
        yuki_layout.set_width(Pango.SCALE*180)
        yuki_layout.set_spacing(Pango.SCALE*5)
        yuki_layout.set_alignment(ALIGN)
        yuki_layout.set_markup(self._get_markup(), -1)
        yuki_font_description = Pango.font_description_from_string(FONT)
        yuki_layout.set_font_description(yuki_font_description)
        return yuki_layout

    def _get_layout_height(self, layout):
        yuki_rectangle_ink, yuki_rectangle_logical = layout.get_extents()
        return (yuki_rectangle_ink.height/Pango.SCALE)

    def paint(self, cairo_context):
        cairo_context.set_source_rgb(0.5, 0.5, 0.5)
        yuki_layout = self._get_pango_layout(cairo_context)
        yuki_height = self._get_layout_height(yuki_layout)
        cairo_context.move_to(5, 350-yuki_height)
        PangoCairo.update_layout(cairo_context, yuki_layout)
        PangoCairo.show_layout(cairo_context, yuki_layout)

    def __init__(self, parent):
        self._parent = parent

