import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app_launcher.application import Application


def create_keyboard_actions(app: "Application") -> None:
    # create global action for escape key to quit application / close appconfig
    quit_action = Gio.SimpleAction.new("quit_app", None)
    quit_action.connect("activate", on_escape_action, app)
    app.add_action(quit_action)
    app.set_accels_for_action("app.quit_app", ["Escape"])

    # create action for return key to launch application
    enter_action = Gio.SimpleAction.new("enter_pressed", None)
    enter_action.connect("activate", on_enter_action, app)
    app.add_action(enter_action)
    app.set_accels_for_action("app.enter_pressed", ["Return"])

    # navigate up with UP key
    keyboard_up_action = Gio.SimpleAction.new("keyboard_up", None)
    keyboard_up_action.connect("activate", on_keyboard_up, app)
    app.add_action(keyboard_up_action)
    app.set_accels_for_action("app.keyboard_up", ["Up"])

    # navigate down with DOWN key
    keyboard_down_action = Gio.SimpleAction.new("keyboard_down", None)
    keyboard_down_action.connect("activate", on_keyboard_down, app)
    app.add_action(keyboard_down_action)
    app.set_accels_for_action("app.keyboard_down", ["Down"])

    # Open appconfig modal with F2
    open_modal_action = Gio.SimpleAction.new("open_modal", None)
    open_modal_action.connect("activate", on_open_modal_action, app)
    app.add_action(open_modal_action)
    app.set_accels_for_action("app.open_modal", ["F2"])


def on_escape_action(action, param, app: "Application") -> None:
    app.quit()


def on_enter_action(action, param, app):
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


def on_open_modal_action(action, param, app) -> None:
    win = app.get_active_window()
    if win:
        from app_launcher.windows.app_config_modal import AppConfigModal

        modal = AppConfigModal(win, app)
        modal.present()
