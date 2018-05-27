
from gi.repository import Pango
from gi.repository import PangoCairo
from libnagato.Object import NagatoObject

FONT = "Ubuntu Mono 15"
OFFSET = 10
SPACING = 5


class NagatoLabels(NagatoObject):

    def _get_align(self):
        return Pango.Alignment.CENTER

    def _get_markup(self):
        return ""

    def _get_pango_layout(self, cairo_context):
        yuki_layout = PangoCairo.create_layout(cairo_context)
        yuki_layout.set_spacing(Pango.SCALE*SPACING)
        yuki_layout.set_alignment(self._get_align())
        yuki_layout.set_markup(self._get_markup(), -1)
        yuki_font_description = Pango.font_description_from_string(FONT)
        yuki_layout.set_font_description(yuki_font_description)
        return yuki_layout

    def _get_layout_positions(self, layout):
        yuki_rectangle_ink, yuki_rectangle_logical = layout.get_extents()
        yuki_w, yuki_h = self._enquiry("YUKI.N > drawing area size")
        yuki_layout_height = yuki_rectangle_logical.height/Pango.SCALE
        self._layout_height = yuki_layout_height
        layout.set_height(Pango.SCALE*(yuki_h-OFFSET*2))
        layout.set_width(Pango.SCALE*(yuki_w-OFFSET*2))
        return OFFSET, (yuki_h-OFFSET-yuki_layout_height)

    def paint(self, cairo_context):
        cairo_context.set_source_rgb(0.5, 0.5, 0.5)
        yuki_layout = self._get_pango_layout(cairo_context)
        yuki_positions = self._get_layout_positions(yuki_layout)
        cairo_context.move_to(*yuki_positions)
        PangoCairo.update_layout(cairo_context, yuki_layout)
        PangoCairo.show_layout(cairo_context, yuki_layout)
        return self._layout_height

    def __init__(self, parent):
        self._parent = parent
