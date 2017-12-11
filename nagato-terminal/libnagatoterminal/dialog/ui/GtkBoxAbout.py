

class NagatoGtkBoxAbout(object):

    def get_gtk_image(self, index):
        return self._gtk_box.get_children()[0]

    def __init__(self, content_area):
        self._gtk_box = content_area.get_children()[0]
        self._gtk_box.get_style_context().add_class("about-dialog-label")
        self._gtk_box.set_opacity(0.7)
        self._gtk_box.set_spacing(8)
        self._gtk_box.set_border_width(8)
