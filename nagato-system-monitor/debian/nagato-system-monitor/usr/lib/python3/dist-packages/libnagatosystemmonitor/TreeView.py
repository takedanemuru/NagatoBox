
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagatosystemmonitor.Kill import NagatoKill
from libnagatosystemmonitor.EnterLock import NagatoEnterLock
from libnagatosystemmonitor.menu.context.ForTreeView import NagatoContextMenu


class NagatoTreeView(NagatoObject, Gtk.TreeView):

    def _set_column(self, title, xalign, text_index, sort_index):
        yuki_column = Gtk.TreeViewColumn(
            title=title,
            cell_renderer=Gtk.CellRendererText(xalign=xalign),
            text=text_index
            )
        yuki_column.set_sort_column_id(sort_index)
        yuki_column.set_expand(True)
        self.append_column(yuki_column)

    def _yuki_n_kill_process(self, process_id=None):
        if process_id is not None:
            self._kill.kill(process_id)

    def _set_columns(self):
        self._set_column("PID", 0, 0, 0)
        self._set_column("Name", 0, 1, 1)
        self._set_column("CPU usage", 1, 2, 3)
        self._set_column("vsize (MiB)", 1, 4, 5)
        self._set_column("rss (MiB)", 1, 6, 7)

    def __init__(self, parent, model):
        self._parent = parent
        Gtk.TreeView.__init__(self)
        self.set_model(model)
        self._set_columns()
        NagatoContextMenu(self)
        NagatoEnterLock(self)
        self._kill = NagatoKill()
        self._parent.add(self)
