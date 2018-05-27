
TEMPLATE = {}

SHOW_VERSION = {
    "action": "store_true",
    "dest": "show_version",
    "default": False,
    "help": "show version"
}

FILE_PATH = {
    "metavar": "image file",
    "type": str,
    "nargs": "*",
    "help": "path to open"
}
