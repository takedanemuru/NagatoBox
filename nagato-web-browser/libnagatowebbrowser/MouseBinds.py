
from gi.repository import Gtk
from gi.repository import Gdk
from libnagato.Object import NagatoObject
from libnagatowebbrowser.menu.context.ForWebView import NagatoForWebView


class NagatoMouseBinds(NagatoObject):

    def _on_context_menu(self, web_view, context_menu, event, hit_test_result):
        # this method simply returns True to abort default context menu.
        return True

    def _on_mouse_target_changed(self, web_view, hit_test_result, modifiers):
        self._hit_test_result = hit_test_result

    def _on_button_press(self, widget, event):
        if event_button == 2:
            pass
        if event.button == 3:
            self._context_menu.pop_up(self._hit_test_result)

    def _inform_hit_test_result(self):
        return self._hit_test_result

    def _connect_gtk_callbacks(self, web_view):
        web_view.connect("button-press-event", self._on_button_press)
        web_view.connect("context-menu", self._on_context_menu)
        web_view.connect("mouse-target-changed", self._on_mouse_target_changed)

    def __init__(self, parent):
        self._parent = parent
        self._context_menu = NagatoForWebView(self)
        parent.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self._connect_gtk_callbacks(parent)
