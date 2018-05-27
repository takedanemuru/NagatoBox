
from libnagatoimageviewer.toolbaritem.Button import NagatoButton

ICON_NAMES = [
    "zoom-fit-best",
    "zoom-in",
    "zoom-out",
    "zoom-original",
    "object-rotate-left",
    "object-rotate-right",
    "object-flip-vertical",
    "object-flip-horizontal"
    ]


class AsakuraViewButtons(object):

    def __init__(self, parent):
        for yuki_icon_name in ICON_NAMES:
            NagatoButton(parent, yuki_icon_name, "YUKI.N > view", True)
