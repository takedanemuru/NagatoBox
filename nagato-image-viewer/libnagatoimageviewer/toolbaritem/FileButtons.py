
from libnagatoimageviewer.toolbaritem.Button import NagatoButton

ICON_NAMES = [
    "document-open",
    "go-previous",
    "go-next"
    ]


class AsakuraFileButtons(object):

    def __init__(self, parent):
        for yuki_icon_name in ICON_NAMES:
            NagatoButton(parent, yuki_icon_name, "YUKI.N > file", True)
