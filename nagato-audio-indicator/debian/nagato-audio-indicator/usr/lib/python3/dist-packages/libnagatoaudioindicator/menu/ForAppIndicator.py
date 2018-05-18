
from gi.repository import Gtk
from gi.repository import Gdk
from libnagato.Object import NagatoObject
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Separator import NagatoSeparator


class NagatoMenu(Gtk.Menu, NagatoObject):

    def _add_volume_menu_items(self):
        for yuki_range in range(100, -10, -10):
            #yuki_label = str(yuki_range)
            #yuki_label = " "*(4-len(yuki_label))+yuki_label+"%"
            #yuki_menu_item = Gtk.CheckMenuItem.new_with_label(yuki_label)
            NagatoItem(self, yuki_range, "YUKI.N > range", yuki_range)
            
    def _initialize_children(self):
        self._add_volume_menu_items()
        NagatoSeparator(self)
        NagatoItem(self, "About", "YUKI.N > about")
        NagatoItem(self, "Quit", "YUKI.N > quit")

    def __init__(self, parent):
        self._parent = parent
        Gtk.Menu.__init__(self)
        self._initialize_children()
        self.show_all()
