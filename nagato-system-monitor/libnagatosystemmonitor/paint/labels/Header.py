
from gi.repository import Pango
from libnagatosystemmonitor.paint.labels.Labels import NagatoLabels


class NagatoHeader(NagatoLabels):

    def _get_align(self):
        return Pango.Alignment.LEFT

    def _get_markup(self):
        return "CPU:\nMemory:\nSwap:\nProcesses:\nThermal:"
