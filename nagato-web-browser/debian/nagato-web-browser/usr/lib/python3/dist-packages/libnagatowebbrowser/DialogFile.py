
import urllib.request
from libnagatowebbrowser.util import Path
from gi.repository import Gtk


def _get_buttons():
    return (
        Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
        Gtk.STOCK_SAVE, Gtk.ResponseType.ACCEPT,
        )

def save_image_from_uri(uri):
    yuki_dialog = Gtk.FileChooserDialog(
        "Save File",
        Gtk.Window(title="Save File"),
        Gtk.FileChooserAction.SAVE,
        _get_buttons()
        )
    yuki_dialog.set_current_folder(Path.get_home())
    yuki_dialog.set_current_name("web_image.png")
    yuki_dialog.set_default_response(Gtk.ResponseType.CANCEL)
    yuki_dialog.set_do_overwrite_confirmation(True)
    if Gtk.ResponseType.ACCEPT == yuki_dialog.run():
        urllib.request.urlretrieve(uri, yuki_dialog.get_filename())
    yuki_dialog.destroy()
