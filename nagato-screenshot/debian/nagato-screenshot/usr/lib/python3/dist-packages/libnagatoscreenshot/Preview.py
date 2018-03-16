
import cairo
from gi.repository import Gtk
from libnagato.Object import NagatoObject


class NagatoPreview(Gtk.DrawingArea, NagatoObject):

    def _get_ratio(self, surface):
        yuki_w_ratio = self.get_allocated_width()/surface.get_width()
        yuki_h_ratio = self.get_allocated_height()/surface.get_height()
        yuki_ratio = min(yuki_w_ratio, yuki_h_ratio)
        return min(yuki_ratio, 1)

    def _get_offset(self, surface, ratio):
        yuki_surface_w = surface.get_width()*ratio
        yuki_surface_h = surface.get_height()*ratio
        yuki_left = (self.get_allocated_width()-(yuki_surface_w))*0.5
        yuki_top = (self.get_allocated_height()-(yuki_surface_h))*0.5
        return yuki_left, yuki_top

    def _on_draw(self, drawing_area, cairo_context):
        cairo_context.save()
        yuki_surface = self._enquiry("YUKI.N > surface")
        yuki_ratio = self._get_ratio(yuki_surface)
        #yuki_left, yuki_top = self._get_offset(yuki_surface, yuki_ratio)
        #cairo_context.translate(yuki_left, yuki_top)
        cairo_context.scale(yuki_ratio, yuki_ratio)
        cairo_context.set_source_surface(yuki_surface, 0, 0)
        cairo_context.paint()
        cairo_context.restore()

    def __init__(self, parent):
        self._parent = parent
        Gtk.DrawingArea.__init__(self)
        self.set_vexpand(True)
        self.connect("draw", self._on_draw)
