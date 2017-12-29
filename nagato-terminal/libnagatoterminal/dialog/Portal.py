
from gi.repository import Gtk
from libnagato.dialog.About import NagatoAboutDialog
from libnagatoterminal.Resources import NagatoResources
from libnagatoterminal.dialog.Warning import NagatoWarning


def _get_user_confirmation(running_processes=None):
    yuki_dialog = NagatoWarning()
    yuki_dialog.set_processes(running_processes)
    yuki_response = yuki_dialog.run()
    yuki_dialog.destroy()
    return (yuki_response == Gtk.ResponseType.OK)


def get_can_close_vte(running_process):
    if running_process is None:
        return True
    return _get_user_confirmation([running_process])


def get_can_close_window(running_processes):
    if len(running_processes) == 0:
        return True
    return _get_user_confirmation(running_processes)


def show_about():
    yuki_dialog = NagatoAboutDialog(NagatoResources())
    yuki_dialog.run()
    yuki_dialog.destroy()
