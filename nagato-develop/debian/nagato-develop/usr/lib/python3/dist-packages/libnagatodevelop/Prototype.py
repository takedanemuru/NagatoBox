
from libnagato.Object import NagatoObject
from libnagatodevelop.create.Directories import NagatoDirectories
from libnagatodevelop.create.Files import NagatoFiles
from libnagatodevelop.create.Icons import NagatoIcons
from libnagatodevelop.create.LongDescription import NagatoLongDescription
from libnagato.dialog.message.Info import NagatoInfo

MARKUP = \
    "project successfully created in \n"\
    "{}"


class NagatoPrototype(NagatoObject):

    def _ensure_files(self):
        yuki_path = self._enquiry("YUKI.N > resources", "PROTOTYPE")
        self._files = NagatoFiles(self._data, yuki_path)

    def create(self, application_data):
        self._data = application_data
        NagatoDirectories(self._data)
        self._ensure_files()
        NagatoIcons(self._data)
        NagatoLongDescription(self._data)
        NagatoInfo.call(message=MARKUP.format(self._data["app-directory"]))
        self._raise("YUKI.N > force quit")

    def __init__(self, parent):
        self._parent = parent
