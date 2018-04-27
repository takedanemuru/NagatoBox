
from gi.repository.GtkSource import SearchSettings
from gi.repository.GtkSource import SearchContext
from libnagatotext.search.Window import NagatoWindow

BACKWARD = 0
FORWARD = 1


class NagatoSearchAndReplace(object):

    def _get_current_iter(self, direction):
        yuki_bounds = self._buffer.get_selection_bounds()
        if yuki_bounds:
            yuki_position = yuki_bounds[direction].get_offset()
        else:
            yuki_position = self._buffer.get_property("cursor-position")
        return self._buffer.get_iter_at_offset(yuki_position)

    def _search_forward(self, keyword):
        yuki_iter = self._get_current_iter(FORWARD)
        yuki_found = yuki_iter.forward_search(keyword, 0, None)
        if yuki_found:
            yuki_match_start, yuki_match_end = yuki_found
            self._buffer.select_range(yuki_match_start, yuki_match_end)

    def call(self):
        if "_window" not in dir(self):
            self._window = NagatoWindow(self)
        self._window.show_all()

    def __init__(self, parent_buffer):
        self._buffer = parent_buffer
        self._settings = SearchSettings()
        self._settings.set_wrap_around(True)
        self._context = SearchContext.new(parent_buffer, self._settings)
