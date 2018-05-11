
from pathlib import Path
import subprocess
from libnagato.dialog.message.Warning import NagatoWarning
from libnagatosystemmonitor.Messages import KILL

class NagatoKill(object):

    def _get_ownwer(self, process_id):
        return Path("/proc/{}/environ".format(process_id)).owner()

    def _get_command(self, process_id):
        yuki_command = Path("/proc/{}/comm".format(process_id)).read_text()
        return yuki_command.replace("\n", "")

    def _get_command_array(self, process_id):
        if "root" == self._get_ownwer(process_id):
            return ["pkexec", "kill", str(process_id)]
        else:
            return ["kill", str(process_id)]

    def _get_message(self, process_id):
        yuki_message = KILL.format(
            process_id,
            self._get_ownwer(process_id),
            self._get_command(process_id),
            )
        return yuki_message

    def kill(self, process_id):
        yuki_response = NagatoWarning.call(
            message=self._get_message(process_id),
            buttons=["Cancel", "Kill"]
            )
        if yuki_response == 1:
            subprocess.call(self._get_command_array(process_id))

    def __init__(self):
        pass
