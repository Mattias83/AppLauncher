import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app_launcher.application import Application


def create_keyboard_actions(app: "Application") -> None:
    # skapa action för att stänga av appen med escape
    quit_action = Gio.SimpleAction.new("quit_app", None)
    quit_action.connect("activate", on_escape_action, app)
    app.add_action(quit_action)
    app.set_accels_for_action("app.quit_app", ["Escape"])

    # skapa action för enter tangenten
    enter_action = Gio.SimpleAction.new("enter_pressed", None)
    enter_action.connect("activate", on_enter_action, app)
    app.add_action(enter_action)
    app.set_accels_for_action("app.enter_pressed", ["Return"])


def on_escape_action(action, param, app: "Application") -> None:
    app.quit()


def on_enter_action(action, param, app):
    # TODO
    app.window.widgets.selection_model.get_selected_item().execute()
