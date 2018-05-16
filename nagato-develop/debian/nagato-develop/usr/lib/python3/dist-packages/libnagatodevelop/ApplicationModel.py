
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

    def _get_config(self, user_data):
        return self._enquiry("YUKI.N > config", user_data)

    def _set_config(self, group, key, value):
        self._raise("YUKI.N > config", (group, key, value))

    def _set_author_value(self, key, config_key, env_key=None):
        yuki_value = self._get_config(("author", config_key))
        if yuki_value == "" and env_key is not None:
            yuki_value = os.getenv(env_key, "")
        DATA[key] = yuki_value

    def _set_default_directory(self):
        yuki_directory = self._get_config(("develop", "last-directory"))
        if yuki_directory == "":
            yuki_directory = os.getenv("HOME")
        DATA["app-directory"] = yuki_directory

    def _save_configs(self):
        self._set_config("author", "name", DATA["user-name"])
        self._set_config("author", "email", DATA["user-email"])
        self._set_config("author", "id-header", DATA["user-id"])
        self._set_config("author", "uri", DATA["user-uri"])
        self._set_config(
            "develop",
            "last-directory",
            os.path.dirname(DATA["app-directory"])
            )

    def create(self):
        yuki_prototype = NagatoPrototype(self)
        yuki_prototype.create(DATA)
        self._save_configs()

    def __getitem__(self, key):
        return DATA[key]

    def __setitem__(self, key, value):
        DATA[key] = value
        if key == "app-name":
            yuki_safename = DATA["app-name"].replace("-", "")
            DATA["lib-name"] = "lib{}".format(yuki_safename)

    def __init__(self, parent):
        self._parent = parent
        self._set_author_value("user-name", "name", "USER")
        self._set_author_value("user-email", "email", "EMAIL")
        self._set_author_value("user-id", "id-header")
        self._set_author_value("user-uri", "uri")
        self._set_default_directory()
