
import os
import subprocess


class NagatoSound(object):

    def play(self, path):
        yuki_null = open(os.devnull, 'w')
        yuki_stdout = subprocess.Popen(
            ["play", path],
            stdout=yuki_null,
            stderr=subprocess.STDOUT
            )

    def __init__(self):
        pass
