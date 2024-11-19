import xml.etree.ElementTree as ET

from app_launcher.app_parsers.app import App


class FlatpakApp(App):
    """
    Parses Flatpak xml files and converting to AppLauncher compatible App format.
    """

    def __init__(self, path: str) -> None:
        tree = ET.parse(path).getroot()
        app_type = tree.get("type")
        name = tree.findtext("name")
        exec = tree.findtext("id")
        if app_type and name and exec:
            super().__init__(
                name=name,
                exec=exec,
                app_type=app_type,
                app_provider="Flatpak",
                # Flatpak icons path on my arch system.
                icon="/var/lib/flatpak/appstream/flathub/x86_64/active/icons/flatpak/128x128/"
                + exec
                + ".png",
            )
