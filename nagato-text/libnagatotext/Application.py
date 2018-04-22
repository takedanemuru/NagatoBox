
from libnagatotext.application.Application import NagatoApplication as TFEI
from libnagatotext.MainWindow import NagatoMainWindow


class NagatoApplication(TFEI):

    def run(self):
        NagatoMainWindow(self)
