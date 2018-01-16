
import os
import urllib.request
from gi.repository import Gtk


def _get_buttons():
    # Gtk.STOCK_ enums don't mean icon but translated text.
    return (
        Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
        Gtk.STOCK_SAVE, Gtk.ResponseType.ACCEPT,
        )

def _run(dialog_title, default_directory, default_name):
    yuki_path = ""
    yuki_dialog = Gtk.FileChooserDialog(
        dialog_title,
        Gtk.Window(title=dialog_title),
        Gtk.FileChooserAction.SAVE,
        _get_buttons()
        )
    yuki_dialog.set_current_folder(default_directory)
    yuki_dialog.set_current_name(default_name)
    yuki_dialog.set_default_response(Gtk.ResponseType.CANCEL)
    yuki_dialog.set_do_overwrite_confirmation(True)
    if Gtk.ResponseType.ACCEPT == yuki_dialog.run():
        yuki_path = yuki_dialog.get_filename()
    yuki_dialog.destroy()
    return yuki_path

def save_image_from_cairo_surface(cairo_surface):
    yuki_path = _run("Save Snapshot", os.environ["HOME"], "screenshot.png")
    if yuki_path != "":
        cairo_surface.write_to_png(yuki_path)

def save_image_from_uri(uri):
    yuki_path = _run("Save Image", os.environ["HOME"], "web_image.png")
    if yuki_path != "":
        urllib.request.urlretrieve(uri, yuki_path)
