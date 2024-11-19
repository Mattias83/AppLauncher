from glob import glob

from app_launcher.app_parsers.app import App
from app_launcher.app_parsers.app_launcher import AppLauncherApp
from app_launcher.app_parsers.flatpak import FlatpakApp
from app_launcher.app_parsers.gnome import GnomeApp


class Apps:
    MAX_APP_ROWS: int = 12  # Specifies how many apps visible in application list
    # Standard path for gnome, flatpak and applauncher apps on my arch system.
    GNOME_APPS_PATH: str = "/usr/share/applications/*.desktop"
    FLATPAK_APPS_PATH: str = "/var/lib/flatpak/exports/share/metainfo/*.xml"
    APP_LAUNCHER_APPS_PATH: str = "/home/mattias/.local/share/applications/*.json"

    def __init__(self) -> None:
        self.gnome_apps: list[App] = [
            app
            for path in glob(self.GNOME_APPS_PATH)
            if (app := GnomeApp(path)).app_type == "Application"
        ]

        self.flatpak_apps: list[App] = [
            app
            for path in glob(self.FLATPAK_APPS_PATH)
            if (app := FlatpakApp(path)).app_type == "desktop"
        ]

        self.app_launcher_apps: list[App] = [
            app
            for path in glob(self.APP_LAUNCHER_APPS_PATH)
            if (app := AppLauncherApp(path)).app_type == "desktop"
        ]

        self.all_apps: list[App] = (
            self.gnome_apps + self.flatpak_apps + self.app_launcher_apps
        )
