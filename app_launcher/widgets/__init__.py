import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk, Gio

from app_launcher.widgets.search_field import SearchField
from app_launcher.app_parsers import Apps
from app_launcher.app_parsers import App


class Widgets:
    def __init__(self, window: Gtk.ApplicationWindow) -> None:
        # MainWindow container box for ui elements
        window_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        # create search field
        self.search_field = SearchField()
        self.search_field.connect("changed", self.on_search_changed)
        window_box.append(self.search_field)

        # create scrollable window for apps list
        self.scrolled_window = Gtk.ScrolledWindow()
        # no horizonal scrollbars, vertical scrollbars when needed.
        self.scrolled_window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self.scrolled_window.set_vexpand(True)
        window_box.append(self.scrolled_window)

        # Create ListStore for apps
        self.list_store = Gio.ListStore.new(App)
        apps = Apps()
        for app in apps.all_apps:
            self.list_store.append(app)

        # Custom filter
        self.custom_filter = Gtk.CustomFilter.new(self.filter_func, None)
        self.filter_model = Gtk.FilterListModel.new(self.list_store, self.custom_filter)

        # Custom sorter
        self.custom_sorter = Gtk.CustomSorter.new(self.sorter_func, None)
        self.sort_model = Gtk.SortListModel.new(self.filter_model, self.custom_sorter)

        # Selection Model
        self.selection_model = Gtk.SingleSelection.new(self.sort_model)
        self.selection_model.set_can_unselect(
            False
        )  # förhindra avmarkering av alla objekt

        # ListView
        self.list_view = Gtk.ListView.new(self.selection_model, self.create_factory())
        self.list_view.set_vexpand(True)
        self.list_view.set_show_separators(False)

        self.scrolled_window.set_child(self.list_view)

        window.set_child(window_box)

    def create_factory(self):
        factory = Gtk.SignalListItemFactory()
        factory.connect("setup", self.setup_factory)
        factory.connect("bind", self.bind_factory)
        return factory

    def setup_factory(self, factory, list_item):
        # list_item.get_style_context().add_class("list-row")
        label = Gtk.Label()
        label.set_xalign(0)  # Justera texten till vänster
        list_item.set_child(label)

    def bind_factory(self, factory, list_item):
        item = list_item.get_item()
        label = list_item.get_child()
        label.set_text(item.name)

    def filter_func(self, item, filter_data):
        search_text = self.search_field.get_text().lower()
        if search_text == "":
            return True
        return search_text in item.name.lower()

    def sorter_func(self, item1, item2, user_data):
        search_text = self.search_field.get_text().lower()
        name1 = item1.name.lower()
        name2 = item2.name.lower()

        # Prioritera exakt matchning
        if name1 == search_text:
            return -1
        if name2 == search_text:
            return 1

        # Prioritera om namnet börjar med söktexten
        if name1.startswith(search_text) and not name2.startswith(search_text):
            return -1
        if not name1.startswith(search_text) and name2.startswith(search_text):
            return 1

        # Sortera alfabetiskt
        return (name1 > name2) - (name1 < name2)

    def on_search_changed(self, entry):
        self.custom_filter.changed(Gtk.FilterChange.DIFFERENT)
        self.custom_sorter.changed(Gtk.SorterChange.DIFFERENT)
