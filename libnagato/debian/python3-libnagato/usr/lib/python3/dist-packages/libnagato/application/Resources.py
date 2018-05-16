
from libnagato.dialog.About import NagatoAboutDialog


class ShamisenResources(object):

    def _yuki_n_about(self):
        NagatoAboutDialog.call(self._resources)

    def _inform_resources(self, name):
        return self._resources.get_absolute_path(name)

    def _inform_data(self, key):
        return self._resources[key]

    def _inform_pixbuf(self, name):
        return self._resources.get_pixbuf(name)

    def show_version(self):
        print(self._resources["version"])
