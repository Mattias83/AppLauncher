import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from app_launcher.widgets import Widgets

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app_launcher import Application


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, app: "Application") -> None:
        super().__init__(application=app)
        self.set_title("AppLauncher")
        self.set_modal(True)
        self.set_default_size(800, 400)
        self.set_resizable(False)
        self.widgets = Widgets(self)  # building ui
