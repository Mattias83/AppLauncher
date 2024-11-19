import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

from app_launcher.widgets.search_field import SearchField


class Widgets:
    def __init__(self, window: Gtk.ApplicationWindow) -> None:
        # MainWindow container box for ui elements
        window_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # create search field
        self.search_field = SearchField()
        window_box.append(self.search_field)

        window.set_child(window_box)
