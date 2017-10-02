import gi
import cairo

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GdkPixbuf
from libnagatowebbrowser.CoreObject import NagatoObject


class NagatoDrawingArea(Gtk.DrawingArea, NagatoObject):

    def _draw_text(self, cairo_context, text):
        cairo_context.set_source_rgb(1, 1, 1)
        cairo_context.set_font_size(14)
        #cairo_context.text_events() returns (x, y, w, h, dx, dy)
        yuki_text = cairo_context.text_extents(text)
        cairo_context.move_to(20, 75 + yuki_text[3])
        cairo_context.show_text(text)

    def _on_draw(self, widget, cairo_context):
        #print(widget.get_allocated_width())
        #print(widget.get_allocated_height())
        #pixbuf = GdkPixbuf.Pixbuf.new_from_file("/home/takedanemuru/albedo.png")
        #Gdk.cairo_set_source_pixbuf(cairo_context, pixbuf, 0, 0)
        #cairo_context.paint()
        cairo_context.set_source_rgba(0, 2, 0, 0.5)
        #paint whole area
        #cr.paint()
        cairo_context.rectangle(20, 75, 200, 100)
        cairo_context.fill()
        self._draw_text(cairo_context, "日本語テスト")
        return False

    def _on_button_press(self, widget, event):
        #print("button pressed")
        print(event.x)
        print(event.y)

    def toggle_visible(self, unique_id):
        pass

    def __init__(self, parent):
        Gtk.DrawingArea.__init__(self)
        self.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self.connect("button-press-event", self._on_button_press)
        self.set_property("height-request", 100)
        parent.attach(self, 0, 0, 1, 1)
        self.connect("draw", self._on_draw)
