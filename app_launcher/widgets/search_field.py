import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class SearchField(Gtk.SearchEntry):
    def __init__(self) -> None:
        super().__init__()
