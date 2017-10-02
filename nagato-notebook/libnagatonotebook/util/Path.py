
import os


def get_absolute(relative_path):
    yuki_base = os.path.dirname(os.path.abspath(__file__))
    yuki_name = os.path.normpath(os.path.join(yuki_base, relative_path))
    return yuki_name


def get_home():
    return os.environ["HOME"]
