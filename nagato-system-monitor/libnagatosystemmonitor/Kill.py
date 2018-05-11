
import subprocess
from libnagato.dialog.message.Warning import NagatoWarning
from libnagatosystemmonitor.Messages import KILL
from libnagatosystemmonitor import MikuruProcess


class NagatoKill(object):

    def _kill(self, process_id):
        yuki_command =["kill", str(process_id)]
        if "root" == MikuruProcess.get_ownwer(process_id):
            yuki_command.insert(0, "pkexec")
        subprocess.call(yuki_command)

    def _get_message(self, process_id):
        return KILL.format(
            process_id,
            MikuruProcess.get_ownwer(process_id),
            MikuruProcess.get_command_line(process_id),
            )

    def _get_user_response(self, process_id):
        return NagatoWarning.call(
            message=self._get_message(process_id),
            buttons=["Cancel", "Kill"]
            )

    def kill(self, process_id):
        if self._get_user_response(process_id) == 1:
            self._kill(process_id)
