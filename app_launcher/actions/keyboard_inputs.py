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

    # piltangt upp
    keyboard_up_action = Gio.SimpleAction.new("keyboard_up", None)
    keyboard_up_action.connect("activate", on_keyboard_up, app)
    app.add_action(keyboard_up_action)
    app.set_accels_for_action("app.keyboard_up", ["Up"])

    # piltangent ner
    keyboard_down_action = Gio.SimpleAction.new("keyboard_down", None)
    keyboard_down_action.connect("activate", on_keyboard_down, app)
    app.add_action(keyboard_down_action)
    app.set_accels_for_action("app.keyboard_down", ["Down"])


def on_escape_action(action, param, app: "Application") -> None:
    app.quit()


def on_enter_action(action, param, app):
    # TODO
    app.window.widgets.selection_model.get_selected_item().execute()
    app.quit()


def on_keyboard_up(action, param, app):
    selected_app_row_index = app.window.widgets.selection_model.get_selected()
    if selected_app_row_index > 0:
        app.window.widgets.selection_model.set_selected(selected_app_row_index - 1)
        app.window.widgets.list_view.scroll_to(
            selected_app_row_index - 1, Gtk.ListScrollFlags.NONE, None
        )
    else:
        app.window.widgets.search_field.grab_focus()


def on_keyboard_down(action, param, app) -> None:
    selected_app_row_index = app.window.widgets.selection_model.get_selected()
    total_app_rows = app.window.widgets.list_store.get_n_items()
    if selected_app_row_index < total_app_rows:
        app.window.widgets.selection_model.set_selected(selected_app_row_index + 1)
        app.window.widgets.list_view.scroll_to(
            selected_app_row_index + 1, Gtk.ListScrollFlags.NONE, None
        )
