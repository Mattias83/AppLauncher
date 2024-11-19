import json

from app_launcher.app_parsers.app import App


class AppLauncherApp(App):

    # Create custom app shortcuts using json. Example:
    # {
    #     "name": "Visual Studio Code",
    #     "exec": "/home/username/Code/utilities/ide/vscode/VSCode-linux-x64/code",
    #     "type": "desktop",
    #     "icon": "/home/username/Code/utilities/ide/vscode/vs-code-icon.png"
    # }

    def __init__(self, path: str) -> None:
        app = json.load(open(path, "r"))
        super().__init__(
            name=app["name"],
            exec=app["exec"],
            app_type=app["type"],
            app_provider="AppLauncher",
            icon=app["icon"],
        )
