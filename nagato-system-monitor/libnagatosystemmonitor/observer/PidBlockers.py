
from libnagato.Object import NagatoObject

IGNORE_CPU = "observer", "ignore_zero_cpu_usage"
IGNORE_MEMORY = "observer", "ignore_zero_memory_usage"


class NagatoPidBlockers(NagatoObject):

    def _get_config_boolean(self, data):
        yuki_boolean_string = self._enquiry("YUKI.N > config", data)
        return yuki_boolean_string == "yes"

    def _refresh_blockers(self):
        self._blockers["usage"] = self._get_config_boolean(IGNORE_CPU)
        self._blockers["rss"] = self._get_config_boolean(IGNORE_MEMORY)

    def change_config(self):
        self._refresh_blockers()

    def __getitem__(self, key):
        return self._blockers[key]

    def __init__(self, parent):
        self._parent = parent
        self._blockers = {}
        self._refresh_blockers()
        self._raise("YUKI.N > register config object", self)
