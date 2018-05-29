
from gi.repository import Gtk
from libnagato.Object import NagatoObject
from libnagato.dialog.message.Warning import NagatoWarning
from libnagatosystemmonitor import Messages
from libnagatosystemmonitor.Thread import NagatoThread
from libnagatosystemmonitor.ui.drawingarea.ForMiniWindow import (
    NagatoDrawingArea
    )

BUTTONS = ["Cancel", "Close"]


class NagatoMiniWindow(Gtk.Window, NagatoObject):

    def _on_close_window(self, widget, event, user_data=None):
        if NagatoWarning.call(message=Messages.QUIT, buttons=BUTTONS) == 0:
            return True
        Gtk.main_quit()

    def _inform_histories(self):
        return self._graph_data

    def _yuki_n_step_graph(self, user_data):
        self._graph_data = user_data

    def _yuki_n_step_label(self, user_data):
        self._drawing_area.queue(user_data)

    def _initialize_window(self):
        Gtk.Window.__init__(self)
        self.connect("delete-event", self._on_close_window)
        self.set_size_request(200, 300)
        self.set_position(Gtk.WindowPosition.CENTER)

    def _on_initialize(self):
        self._graph_data = None
        self._drawing_area = NagatoDrawingArea(self)
        self._thread = NagatoThread(self)
        self._thread.start()

    def __init__(self, parent):
        self._parent = parent
        self._initialize_window()
        self._on_initialize()
        self.show_all()
        Gtk.main()
