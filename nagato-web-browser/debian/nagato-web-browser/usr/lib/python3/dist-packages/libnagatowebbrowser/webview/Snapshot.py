
from gi.repository import WebKit2
from libnagatowebbrowser.dialog import File as Dialog


class NagatoSnapshot(object):

    def _yuki_n_snapshot(self, snapshot_region):
        # Webkit2.WebView.get_snaphot() is async procedure.
        # blocks nothing, but heavy.
        self.get_snapshot(
            snapshot_region,
            WebKit2.SnapshotOptions.NONE,
            None,
            self._on_get_snapshot_finished,
            None
            )

    def _on_get_snapshot_finished(self, webview, result, user_data=None):
        yuki_cairo_surface = self.get_snapshot_finish(result)
        if yuki_cairo_surface is not None:
            Dialog.save_image_from_cairo_surface(yuki_cairo_surface)
