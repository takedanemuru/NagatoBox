
from libnagato.menu.Item import NagatoItem
from libnagato.menu.Separator import NagatoSeparator
from libnagatowebbrowser.menu.group.Navigations import AsakuraNavigations
from libnagatowebbrowser.menu.group.Image import AsakuraImage
from libnagatowebbrowser.menu.group.Link import AsakuraLink
from libnagatowebbrowser.menu.group.TabActions import AsakuraTabActions
from libnagatowebbrowser.menu.action.FullScreen import NagatoFullScreen
from libnagatowebbrowser.menu.context.ContextCore import NagatoContextCore


class NagatoForWebView(NagatoContextCore):

    def _inform_hit_test_result(self):
        return self._hit_test_result

    def _on_context_menu(self, web_view, context_menu, event, hit_test_result):
        # this method simply returns True to abort default context menu.
        return True

    def _on_target_changed(self, web_view, hit_test_result, modifiers):
        self._hit_test_result = hit_test_result

    def _add_gtk_callbacks(self):
        self._parent.connect("context-menu", self._on_context_menu)
        self._parent.connect("mouse-target-changed", self._on_target_changed)

    def _initialize_children(self):
        self._hit_test_result = None
        AsakuraNavigations(self)
        AsakuraImage(self)
        AsakuraLink(self)
        AsakuraTabActions(self)
        NagatoSeparator(self)
        NagatoFullScreen(self)
        NagatoSeparator(self)
        NagatoItem(self, "About", "YUKI.N > about")
        NagatoItem(self, "Quit", "YUKI.N > quit")
