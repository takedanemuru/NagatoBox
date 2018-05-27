
from libnagato.Object import NagatoObject
from libnagato.dialog.chooser.Load import NagatoLoad
from libnagatoimageviewer.files.Paths import NagatoPaths
from libnagatoimageviewer.files.Index import NagatoIndex

CALL_DISPATCH = {
    "document-open": "_on_document_open",
    "go-previous": "_on_go_previous",
    "go-next": "_on_go_next"
}


class NagatoFiles(NagatoObject):

    def _on_document_open(self):
        yuki_path = NagatoLoad.call(self._paths.directory, "image/*")
        if yuki_path is None:
            return
        yuki_index = self._paths.reset_paths(yuki_path)
        self._index.reset(yuki_index)

    def _on_go_previous(self):
        self._index.go_previous()

    def _on_go_next(self):
        self._index.go_next()

    def _inform_max_index(self):
        return self._paths.maximum

    def __call__(self, message):
        yuki_method = getattr(self, CALL_DISPATCH[message])
        yuki_method()

    def __init__(self, parent):
        self._parent = parent
        self._index = NagatoIndex(self)
        self._paths = NagatoPaths(self)

    @property
    def path(self):
        return self._paths[self._index.index]
