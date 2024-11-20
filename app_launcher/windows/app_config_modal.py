import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gdk


class AppConfigModal(Gtk.Window):
    def __init__(self, parent, app) -> None:
        super().__init__(title="App Configuration")
        self.app = app
        self.get_style_context().add_class("app-config")
        self.set_transient_for(parent)
        self.set_modal(True)
        self.set_default_size(300, 300)
        self.set_resizable(False)

        key_controller = Gtk.EventControllerKey()
        key_controller.connect("key-pressed", self.on_key_pressed)
        self.add_controller(key_controller)

        self.build_ui()

    def on_key_pressed(self, controller, keyval, keycode, state) -> bool:
        if keyval == Gdk.KEY_Escape:
            self.close()
            return True
        return False

    def build_ui(self) -> None:
        # fixa ui senare TODO
        selected_app_row = self.app.window.widgets.selection_model.get_selected_item()
        label = Gtk.Label(label=selected_app_row.name)
        self.set_child(label)
