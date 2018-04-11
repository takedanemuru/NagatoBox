
from libnagatotext import GiVersion
from libnagato.Object import NagatoObject
from libnagato.dialog.About import NagatoAboutDialog
from libnagatotext.Args import NagatoArgs
from libnagatotext.Resources import NagatoResources
from libnagatotext.MainWindow import NagatoMainWindow


class NagatoYuki(NagatoObject):

    def _yuki_n_about(self):
        NagatoAboutDialog.call(self._resources)

    def _inform_args(self, key):
        return self._args[key]

    def _inform_resources(self, name):
        return self._resources.get_absolute_path(name)

    def _inform_data(self, key):
        return self._resources[key]

    def _inform_pixbuf(self, name):
        return self._resources.get_pixbuf(name)

    def N(self, message):
        if self._args["show-version"]:
            print(self._resources["version"])
        else:
            NagatoMainWindow(self)
            print("YUKI.N > また図書館に…")

    def __init__(self):
        GiVersion.require()
        self._parent = None
        self._args = NagatoArgs()
        self._resources = NagatoResources()
