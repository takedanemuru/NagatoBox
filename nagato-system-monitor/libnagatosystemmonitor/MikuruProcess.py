
from pathlib import Path


def get_ownwer(process_id):
    return Path("/proc/{}/environ".format(process_id)).owner()


def get_command_line(pid):
    yuki_command = Path("/proc/{}/cmdline".format(str(pid))).read_text()
    return yuki_command.replace("\0", " ")


def get_command(pid):
    yuki_command = Path("/proc/{}/comm".format(str(pid))).read_text()
    return yuki_command.replace("\n", "")
