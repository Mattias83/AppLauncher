import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk, Gio, GLib

from app_launcher.windows.main_window import MainWindow
from app_launcher.actions.keyboard_inputs import create_keyboard_actions


class Application(Gtk.Application):
    def __init__(self, **kwargs) -> None:
        super().__init__(
            application_id="se.mattias83.applauncher",
            **kwargs,
        )
        self.load_css()
        create_keyboard_actions(self)

    def load_css(self) -> None:
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("styles.css")
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
        )

    def do_activate(self) -> None:
        self.window = MainWindow(self)
        self.window.present()
