import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk, Gio, GLib

from app_launcher.windows.main_window import MainWindow


class Application(Gtk.Application):
    def __init__(self, **kwargs) -> None:
        super().__init__(
            application_id="se.mattias83.applauncher",
            **kwargs,
        )

    def do_activate(self) -> None:
        self.window = MainWindow(self)
        self.window.present()
