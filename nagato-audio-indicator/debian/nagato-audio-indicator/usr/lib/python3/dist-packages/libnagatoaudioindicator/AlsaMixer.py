
import subprocess
from libnagato.Object import NagatoObject

COMMAND_LINE_CHANNEL = "amixer get {} | egrep -o '[0-9]+%'"
COMMAND_LINE_SET = "amixer sset {} {}%"


class NagatoAlsaMixer(NagatoObject):

    def _run(self, command_line):
        yuki_process = subprocess.Popen(
            command_line,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )
        yuki_stdout, yuki_stderr = yuki_process.communicate()
        return yuki_stdout.decode("utf-8")

    def _get_alsa_volume(self, channel):
        yuki_output = self._run(COMMAND_LINE_CHANNEL.format(channel))
        return yuki_output.split("\n")

    def _set_channel(self):
        if self._get_alsa_volume("Master") != [""]:
            self._channel = "Master"
        else:
            self._channel = "PCM"

    def set_volume(self, volume):
        self._run(COMMAND_LINE_SET.format(self._channel, volume))

    def __init__(self, parent):
        self._parent =parent
        self._set_channel()

    @property
    def volume(self):
        return self._get_alsa_volume(self._channel)[0]
