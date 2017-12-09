
from libnagatoterminal.MenuItemSensitiveCopy import NagatoMenuItemSensitiveCopy
from libnagatoterminal.MenuItemSensitivePaste import NagatoMenuItemSensitivePaste

class AsakuraMenuGroupClipboard(object):

    def __init__(self, parent):
        NagatoMenuItemSensitiveCopy(parent)
        NagatoMenuItemSensitivePaste(parent)        
