
import os

APPLICATION_DATA = {
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
    "app-long-description": ""
}


class NagatoApplicationModel(object):

    def _set_author_value(self, key, config_key, env_key):
        yuki_value = self._config["author"][config_key]
        if yuki_value == "":
            yuki_value = os.getenv(env_key, "")
        APPLICATION_DATA[key] = yuki_value

    def _set_default_directory(self):
        yuki_directory = self._config["develop"]["last-directory"]
        if yuki_directory == "":
            yuki_directory = os.getenv("HOME")
        APPLICATION_DATA["app-directory"] = yuki_directory

    def create(self):
        pass

    def change_data(self, key, value):
        APPLICATION_DATA[key] = value

    def __getitem__(self, key):
        return APPLICATION_DATA[key]

    def __setitem__(self, key, value):
        APPLICATION_DATA[key] = value

    def __init__(self, config):
        self._config = config
        self._set_author_value("user-name","name", "USER")
        self._set_author_value("user-email","email", "EMAIL")
        self._set_default_directory()
