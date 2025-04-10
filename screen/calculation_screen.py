from functools import partial
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.factory import Factory

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu

from utils.calculations import calculate_volume
from utils.log_table import LogTable
from utils.storage import app_data, save_data

Builder.load_file("c:/Users/38098/Desktop/progect/p1/Icode/kivy_files/calculation_screen.kv")

class CalculationScreen(Screen):
    species_value = "Дуб"
    grade_value = "A"
    price_value = "0"
    selected_method = "ISO 4480-83"

    def on_enter(self):
        if not hasattr(self, "cumulative_volume"):
            self.cumulative_volume = 0.0
        self.populate_d_buttons()
        self.ids.d_buttons_layout.bind(width=self.update_d_buttons)
        if not hasattr(self, "log_table"):
            self.log_table = LogTable()
            if "log_box" in self.ids:
                self.ids.log_box.clear_widgets()
                self.ids.log_box.add_widget(self.log_table)
        print("CalculationScreen: on_enter finished")

    def on_leave(self):
        if hasattr(self, "current_menu") and self.current_menu:
            self.current_menu.dismiss()
            self.current_menu = None
        if hasattr(self, "dialog") and self.dialog:
            self.dialog.dismiss()
            self.dialog = None

    def populate_d_buttons(self):
        d_layout = self.ids.d_buttons_layout
        d_layout.clear_widgets()
        cols = 5
        spacing = dp(1)
        available_width = d_layout.width or Window.width
        available_width -= (cols + 1) * spacing
        button_size = available_width / cols
        for value in range(4, 121, 2):
            btn = Factory.MDFlatButton(
                text=str(value),
                size_hint=(None, None),
                size=(button_size, button_size),
                on_release=self.select_d_value,
                theme_text_color="Custom",
                text_color=(0, 1, 0, 1),
                md_bg_color=(0, 0, 0, 0),
                line_color=(0, 1, 0, 1)
            )
            d_layout.add_widget(btn)

    def update_d_buttons(self, instance, width):
        cols = 5
        spacing = dp(1)
        available_width = width - (cols + 1) * spacing
        button_size = available_width / cols
        for child in instance.children:
            child.size = (button_size, button_size)

    def select_d_value(self, instance):
        self.ids.diameter_input.text = instance.text
        if self.ids.length_input.text:
            self.compute_volume()

    def open_length_menu(self):
        steps = int((13 - 0.5) / 0.1) + 1
        items = []
        for i in range(steps):
            val = 0.5 + i * 0.1
            items.append({
                "text": f"{val:.1f}",
                "viewclass": "OneLineListItem",
                "on_release": partial(self.set_length, f"{val:.1f}")
            })
        self.length_menu = MDDropdownMenu(
            caller=self.ids.length_input,
            items=items,
            width_mult=4,
            max_height=dp(120)
        )
        self.length_menu.open()

    def set_length(self, value, *args):
        self.ids.length_input.text = value
        self.length_menu.dismiss()
        self.compute_volume()

    def compute_volume(self):
        try:
            d = float(self.ids.diameter_input.text)
            l = float(self.ids.length_input.text)
            volume, unit, total = calculate_volume(d, l, method=self.selected_method)
            self.ids.volume_output.text = f"{volume:.2f}"
            self.cumulative_volume += volume
            self.ids.total_v.text = f"{self.cumulative_volume:.6f}{unit}"
            if not hasattr(self, "log_table"):
                self.log_table = LogTable()
                print("CalculationScreen: Created new LogTable")
            self.log_table.add_log_entry(
                d, l, self.selected_method, 1,
                self.species_value, self.grade_value, self.price_value, volume
            )
            if hasattr(self.log_table, "update_summary"):
                self.log_table.update_summary()
        except Exception as e:
            self.ids.volume_output.text = "Ошибка"
            print("Error in compute_volume:", e)

    # Метод, вызываемый из kv-файла для обновления объёма
    def update_volume(self):
        self.compute_volume()

    def create_dynamic_menu(self, data_key, callback):
        if hasattr(self, "current_menu") and self.current_menu:
            self.current_menu.dismiss()
            self.current_menu = None

        current = ""
        if data_key == "wood_type":
            current = self.species_value
        elif data_key == "sort":
            current = self.grade_value
        elif data_key == "price":
            current = self.price_value
        elif data_key == "quantity":
            current = self.ids.ent_total_btn.text if self.ids.ent_total_btn.text else ""
        elif data_key == "method":
            current = self.selected_method

        raw_items = [i for i in app_data.get(data_key, []) if i != "Добавить"]
        unique_items = list(dict.fromkeys(raw_items))
        menu_items = []
        for i in unique_items:
            menu_items.append({
                "text": i,
                "viewclass": "CustomOneLineItem",
                "highlight": True if i == current else False,
                "on_release": partial(self._dynamic_menu_callback, callback, i)
            })
        menu_items.append({
            "text": "Добавить",
            "viewclass": "CustomOneLineItem",
            "highlight": False,
            "on_release": lambda: self.show_add_dialog(data_key, callback)
        })
        self.current_menu = MDDropdownMenu(caller=self.ids.species_btn, items=menu_items, width_mult=4)
        return self.current_menu

    def _dynamic_menu_callback(self, callback, value, *args):
        callback(value)
        if hasattr(self, "current_menu") and self.current_menu:
            self.current_menu.dismiss()
            self.current_menu = None

    def show_add_dialog(self, data_key, callback):
        if hasattr(self, "dialog") and self.dialog:
            self.dialog.dismiss()
        self.dialog = MDDialog(
            title="Добавить элемент",
            type="custom",
            content_cls=Factory.MDTextField(hint_text="Новый элемент", font_size="12sp"),
            buttons=[
                MDFlatButton(text="Ok", on_release=lambda x: self.add_new_value(data_key, callback, self.dialog)),
                MDFlatButton(text="Отмена", on_release=lambda x: self.dialog.dismiss())
            ]
        )
        self.dialog.open()

    def add_new_value(self, data_key, callback, dialog):
        new_value = dialog.content_cls.text.strip()
        if new_value and new_value not in app_data.get(data_key, []):
            app_data[data_key].append(new_value)
            save_data(app_data)
            callback(new_value)
        dialog.dismiss()

    def show_wood_type_menu(self, caller):
        menu = self.create_dynamic_menu("wood_type", self.set_wood_type)
        menu.caller = caller
        menu.open()

    def set_wood_type(self, value):
        self.species_value = value
        self.ids.species_btn.text = value

    def show_sort_menu(self, caller):
        menu = self.create_dynamic_menu("sort", self.set_sort)
        menu.caller = caller
        menu.open()

    def set_sort(self, value):
        self.grade_value = value
        self.ids.grade_btn.text = value

    def show_price_menu(self, caller):
        menu = self.create_dynamic_menu("price", self.set_price)
        menu.caller = caller
        menu.open()

    def set_price(self, value):
        self.price_value = value
        self.ids.price_btn.text = value

    def show_quantity_menu(self, caller):
        menu = self.create_dynamic_menu("quantity", self.set_quantity_value)
        menu.caller = caller
        menu.open()

    def set_quantity_value(self, value):
        self.ids.ent_total_btn.text = value

    def show_method_menu(self, caller):
        menu = self.create_dynamic_menu("method", self.set_method)
        menu.caller = caller
        menu.open()

    def set_method(self, value):
        self.selected_method = value
        self.compute_volume()

    def open_save_menu(self):
        dialog = MDDialog(title="Сохранение", text="Функция сохранения ещё не реализована.")
        dialog.open()

    def open_export_menu(self):
        dialog = MDDialog(title="Экспорт", text="Функция экспорта ещё не реализована.")
        dialog.open()

    def confirm_clear_all(self):
        self.clear_dialog = MDDialog(
            title="Очистка",
            text="Сохранить результаты перед очисткой?",
            buttons=[
                Factory.MDFlatButton(text="Да", on_release=lambda x: self.clear_all(True)),
                Factory.MDFlatButton(text="Нет", on_release=lambda x: self.clear_all(False)),
                Factory.MDFlatButton(text="Отмена", on_release=lambda x: self.clear_dialog.dismiss())
            ]
        )
        self.clear_dialog.open()

    def clear_all(self, save):
        self.clear_dialog.dismiss()
        if save:
            self.open_save_menu()
        self.ids.diameter_input.text = ""
        self.ids.length_input.text = ""
        self.ids.volume_output.text = ""
        self.ids.total_v.text = ""
        self.cumulative_volume = 0.0
        if hasattr(self, "log_table"):
            self.log_table.clear_entries()

    def open_full_table(self):
        if hasattr(self, "log_table") and self.log_table.get_entries():
            self.manager.current = "c_s_table"
            self.manager.get_screen("c_s_table").set_table(self.log_table)
        else:
            dialog = MDDialog(title="Таблица пуста", text="Нет записей или метод не реализован.")
            dialog.open()

    def _set_method_in_field(self, field, method):
        field.text = method
        if "Метод_menu" in self.edit_fields:
            self.edit_fields["Метод_menu"].dismiss()

    def open_column_menu(self):
        pass

    def open_dialog(self):
        self.dialog.open()