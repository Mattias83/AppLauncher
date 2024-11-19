import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk, Gio, GLib


class Application(Gtk.Application):
    def __init__(self, **kwargs) -> None:
        super().__init__(
            application_id="se.mattias83.applauncher",
            **kwargs,
        )

    def do_activate(self) -> None:
        win = Gtk.ApplicationWindow(application=self)
        win.set_modal(True)
        win.set_default_size(800, 800)
        win.set_resizable(False)
        win.present()
