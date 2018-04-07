
import os
from libnagato.Object import NagatoObject
from libnagatodevelop.Prototype import NagatoPrototype

DATA = {
    "user-name": "",
    "user-email": "",
    "user-uri": "",
    "user-id": "",
    "app-directory": "",
    "app-name": "",
    "app-icon": "",
    "app-id": "",
    "app-uri": "",
    "app-short-description": "",
    "app-long-description": "",
    "lib-name": ""
}


class NagatoApplicationModel(NagatoObject):

    def _set_author_value(self, key, config_key, env_key=None):
        yuki_value = self._config["author"][config_key]
        if yuki_value == "" and env_key is not None:
            yuki_value = os.getenv(env_key, "")
        DATA[key] = yuki_value

    def _set_default_directory(self):
        yuki_directory = self._config["develop"]["last-directory"]
        if yuki_directory == "":
            yuki_directory = os.getenv("HOME")
        DATA["app-directory"] = yuki_directory

    def _save_configs(self):
        self._config.set_value("author", "name", DATA["user-name"])
        self._config.set_value("author", "email", DATA["user-email"])
        self._config.set_value("author", "id-header", DATA["user-id"])
        self._config.set_value("author", "uri", DATA["user-uri"])
        self._config.set_value(
            "develop",
            "last-directory",
            os.path.dirname(DATA["app-directory"])
            )
        self._config.save_to_file()

    def create(self):
        yuki_prototype = NagatoPrototype(self)
        yuki_prototype.create(DATA)
        self._save_configs()

    def change_data(self, key, value):
        DATA[key] = value

    def __getitem__(self, key):
        return DATA[key]

    def __setitem__(self, key, value):
        DATA[key] = value
        if key == "app-name":
            yuki_safename = DATA["app-name"].replace("-", "")
            DATA["lib-name"] = "lib{}".format(yuki_safename)

    def __init__(self, parent, config):
        self._parent = parent
        self._config = config
        self._set_author_value("user-name", "name", "USER")
        self._set_author_value("user-email", "email", "EMAIL")
        self._set_author_value("user-id", "id-header")
        self._set_author_value("user-uri", "uri")
        self._set_default_directory()
