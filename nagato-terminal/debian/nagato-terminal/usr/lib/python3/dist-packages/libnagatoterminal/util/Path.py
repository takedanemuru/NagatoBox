
import os


def _get_resource_directory():
    yuki_base = os.path.dirname(os.path.abspath(__file__))
    yuki_base = os.path.dirname(yuki_base)
    return os.path.join(yuki_base, "resources")


def get_absolute(relative_path):
    yuki_base = os.path.dirname(os.path.abspath(__file__))
    yuki_name = os.path.normpath(os.path.join(yuki_base, relative_path))
    return yuki_name


def get_resource(relative_path):
    return os.path.join(_get_resource_directory(), relative_path)


def get_home():
    return os.environ["HOME"]
