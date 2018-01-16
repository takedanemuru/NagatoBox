
from libnagatowebbrowser.menu.separator.Hidable import NagatoHidable


class NagatoSeparator(NagatoHidable):

    def _get_visible(self):
        yuki_hit_test_result = self._enquiry(self._query)
        return yuki_hit_test_result.context_is_selection()
