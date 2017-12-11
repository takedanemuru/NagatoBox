
from gi.repository import Gtk
from libnagatoterminal.dialog.About import NagatoAboutDialog
from libnagatoterminal.dialog.Warning import NagatoWarning


def _get_user_confirmation(running_processes=None):
    yuki_dialog = NagatoWarning()
    yuki_response = yuki_dialog.run()
    yuki_dialog.destroy()
    return (yuki_response == Gtk.ResponseType.OK)


def set_default_window(window):
    NagatoWarning.set_default_window(window)


def get_can_close_vte(running_process):
    if running_process is None:
        return True
    return _get_user_confirmation([running_process])


def get_can_close_window(running_processes):
    if len(running_processes) == 0:
        return True
    return _get_user_confirmation(running_processes)


def show_about():
    yuki_dialog = NagatoAboutDialog()
    yuki_dialog.run()
    yuki_dialog.destroy()
