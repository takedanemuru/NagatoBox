
import os


def _get_resource_directory():
    yuki_util_dir = os.path.dirname(os.path.abspath(__file__))
    yuki_lib_dir = os.path.dirname(yuki_util_dir)
    return os.path.join(yuki_lib_dir, "resources")


def get_resource(relative_path):
    return os.path.join(_get_resource_directory(), relative_path)


def get_home():
    return os.environ["HOME"]
