import json

from app_launcher.app_parsers.app import App


class AppLauncherApp(App):
    def __init__(self, path: str) -> None:
        app = json.load(open(path, "r"))
        super().__init__(
            name=app["name"],
            exec=app["exec"],
            app_type=app["type"],
            app_provider="AppLauncher",
            icon=app["icon"],
        )
