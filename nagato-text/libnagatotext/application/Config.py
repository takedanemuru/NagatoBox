

class ShamisenConfig(object):

    def _yuki_n_config(self, user_data):
        self._config.set_data(user_data)

    def _yuki_n_set_recent_path(self, path=None):
        if path is not None:
            self._config.set_recent_path(path)

    def _yuki_n_clear_recent_paths(self):
        self._config.clear_recent_paths()

    def _inform_recent_paths(self):
        return self._config.get_recent_paths()

    def _inform_config(self, user_data):
        yuki_group, yuki_key = user_data
        return self._config[yuki_group][yuki_key]
