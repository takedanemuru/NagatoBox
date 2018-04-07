
from libnagato.Object import NagatoObject
from libnagatodevelop.create.Directories import NagatoDirectories
from libnagatodevelop.create.Files import NagatoFiles
from libnagatodevelop.create.Icons import NagatoIcons
from libnagatodevelop.create.LongDescription import NagatoLongDescription
from libnagatodevelop.dialog.Info import NagatoInfo

MARKUP = \
    "project successfully created in \n"\
    "{}"


class NagatoPrototype(NagatoObject):

    def _ensure_directories(self):
        self._directories = NagatoDirectories(self._data)

    def _ensure_files(self):
        yuki_path = self._enquiry("YUKI.N > resources").get_prototype_path()
        self._files = NagatoFiles(self._data, yuki_path)

    def create(self, application_data):
        self._data = application_data
        self._ensure_directories()
        self._ensure_files()
        NagatoIcons(self._data)
        NagatoLongDescription(self._data)
        NagatoInfo.call("info", MARKUP.format(self._data["app-directory"]))
        self._raise("YUKI.N > quit", True)

    def __init__(self, parent):
        self._parent = parent
