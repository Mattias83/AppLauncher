import re
from configparser import ConfigParser

from app_launcher.app_parsers.app import App


class GnomeApp(App):
    """
    Parses .desktop files from Gnome
    """

    def __init__(self, path: str) -> None:
        app = ConfigParser(interpolation=None)
        app.read(path)
        section: str = "Desktop Entry"
        # remove gnome flags from exec string
        exec = re.sub(r"%.", "", app.get(section, "Exec"))
        super().__init__(
            name=app.get(section, "Name"),
            exec=exec,
            app_type=app.get(section, "Type"),
            app_provider="Gnome",
            icon=app.get(section, "Icon", fallback=""),
        )
