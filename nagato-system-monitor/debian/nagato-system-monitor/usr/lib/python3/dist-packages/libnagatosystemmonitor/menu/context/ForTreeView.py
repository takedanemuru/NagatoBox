
from gi.repository import Gtk
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Context import NagatoContextCore


class NagatoContextMenu(NagatoContextCore):

    def _get_id(self):
        yuki_selection = self._parent.get_selection()
        yuki_tree_model, yuki_tree_paths = yuki_selection.get_selected_rows()
        if len(yuki_tree_paths) == 0:
            return None
        yuki_iter = yuki_tree_model.get_iter(yuki_tree_paths[0])
        return yuki_tree_model.get_value(yuki_iter, 0)

    def _refresh_menus(self):
        for yuki_child in self.get_children():
            self.remove(yuki_child)
        self._initialize_children()
        self.show_all()

    def _on_right_click(self, user_data=None):
        self._id = self._get_id()
        self._refresh_menus()
        yuki_event_time = Gtk.get_current_event_time()
        self.popup(None, None, None, None, 0, yuki_event_time)

    def _initialize_children(self):
        if "_id" not in dir(self):
            self._id = None
        yuki_title = "Kill Process id : {}".format(self._id)
        NagatoItem(self, yuki_title, "YUKI.N > kill process", self._id)
