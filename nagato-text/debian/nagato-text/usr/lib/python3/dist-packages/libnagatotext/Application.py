
from libnagato.Object import NagatoObject
from libnagato.dialog.About import NagatoAboutDialog
from libnagatotext.Resources import NagatoResources
from libnagatotext.MainWindow import NagatoMainWindow
from libnagatotext.Config import NagatoConfig


class NagatoApplication(NagatoObject):

    def _yuki_n_save_config(self, user_data):
        self._config.set_data(user_data)

    def _yuki_n_config(self, user_data):
        self._config.set_data(user_data)
        try:
            self._main_window.show_all()
        except:
            pass

    def _yuki_n_about(self):
        NagatoAboutDialog.call(self._resources)

    def _inform_config(self, user_data):
        yuki_group, yuki_key = user_data
        return self._config[yuki_group][yuki_key]

    def _inform_resources(self, name):
        return self._resources.get_absolute_path(name)

    def _inform_data(self, key):
        return self._resources[key]

    def _inform_pixbuf(self, name):
        return self._resources.get_pixbuf(name)

    def show_version(self):
        self._resources["version"]

    def run(self):
        self._main_window = NagatoMainWindow(self)

    def __init__(self, parent):
        self._parent = parent
        self._resources = NagatoResources()
        self._config = NagatoConfig(self)
