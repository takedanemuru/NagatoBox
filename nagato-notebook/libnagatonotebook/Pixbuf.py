import gi

from gi.repository import GdkPixbuf
from libnagatonotebook.util import Path


def get_application_icon():
    yuki_icon_path = Path.get_absolute("../resources/nagato-notebook.png")
    yuki_icon = GdkPixbuf.Pixbuf.new_from_file(yuki_icon_path)
    return yuki_icon
