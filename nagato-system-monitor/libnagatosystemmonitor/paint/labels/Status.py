
from gi.repository import Pango
from libnagatosystemmonitor.paint.labels.Labels import NagatoLabels

MARKUP = "{:.2%}\n{:.2%}\n{:.2%}\n{}\n{}°C"


class NagatoStatus(NagatoLabels):

    def _get_align(self):
        return Pango.Alignment.RIGHT

    def _get_markup(self):
        yuki_data = self._enquiry("YUKI.N > status")
        if yuki_data is None:
            return ""
        return MARKUP.format(
            yuki_data["cpu"],
            yuki_data["memory"],
            yuki_data["swap"],
            yuki_data["count"],
            yuki_data["temperature"]
            )
