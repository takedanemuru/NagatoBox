
from pathlib import Path
from gi.repository import GLib

class NagatoKill(object):

    def kill(self, process_id):
        yuki_owner = Path("/proc/{}/environ".format(process_id)).owner()
        yuki_command_line = Path("/proc/{}/cmdline".format(process_id)).read_text()
        print(yuki_owner)
        print(yuki_command_line)
        return
        GLib.spawn_command_line_sync("")

    def __init__(self):
        pass
