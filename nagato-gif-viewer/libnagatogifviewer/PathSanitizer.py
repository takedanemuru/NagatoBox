
import os
import mimetypes


def _get_uri(path_name):
    if path_name.startswith("/"):
        return path_name
    return os.path.join(os.getcwd(), path_name)

def _matches(path_name, mime_type):
    yuki_mime_type = mimetypes.guess_type(path_name, strict=True)[0]
    return (yuki_mime_type == mime_type)

def get_a_path(paths, mime_type):
    for yuki_path in paths:
        yuki_uri = _get_uri(yuki_path)
        if _matches(yuki_uri, mime_type)\
        and os.path.exists(yuki_uri):
            return yuki_uri
    return None
