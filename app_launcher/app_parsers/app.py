import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GObject


class App(GObject.GObject):
    def __init__(
        self, name: str, exec: str, app_type: str, app_provider: str, icon: str = ""
    ) -> None:
        super().__init__()
        self.name = name
        self.exec = exec
        self.app_type = app_type
        self.app_provider = app_provider
        self.icon = icon

    def __str__(self) -> str:
        return f"Name: {self.name}, Exec: {self.exec}, AppType: {self.app_type}, AppProvider: {self.app_provider}, Icon: {self.icon}"
