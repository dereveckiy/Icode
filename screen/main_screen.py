from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from components.drawer import Drawer
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import OneLineListItem
from utils.calculations import calculate_volume
from utils.log_table import LogTable
from utils.storage import save_data, app_data
from utils.export import export_to_pdf, export_to_word, export_to_excel
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import MDBoxLayout
import os
import json
import time

class MainScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_method = "ISO 4480-83"  # метод по умолчанию
        # Создаем таблицу; каждая запись имеет порядок:
        # [D, L, Метод, Количество, Wood, Sort, Price, Total]
        self.log_table = LogTable()
        # Инициализация выпадающих меню и меню сохранения
        self.save_menu = None

    def on_enter(self):
        if "nav_drawer" in self.ids and not self.ids.nav_drawer.children:
            self.ids.nav_drawer.add_widget(Drawer())
        if "log_container" in self.ids:
            self.ids.log_container.clear_widgets()
            self.ids.log_container.add_widget(self.log_table)
        if "method_button" in self.ids:
            self.method_menu = self.create_menu(
                self.ids.method_button,
                ["ISO 4480-83", "Doyle Log Rule", "Scribner Log Rule", "International 1/4 Log Rule",
                 "JAS Scale", "Hoppus Log Rule", "ГОСТ 2708-75"],
                self.set_method,
            )
        if "wood_type_button" in self.ids:
            self.wood_type_menu = self.create_dynamic_menu("wood_type", self.set_wood_type)
        if "price_button" in self.ids:
            self.price_menu = self.create_dynamic_menu("price", self.set_price)
        if "sort_button" in self.ids:
            self.sort_menu = self.create_dynamic_menu("sort", self.set_sort)
        if "quantity_button" in self.ids:
            self.quantity_menu = self.create_dynamic_menu("quantity", self.set_quantity)
        self.create_save_menu()

    def create_menu(self, caller, items, callback):
        menu_items = [
            {"text": i, "viewclass": "OneLineListItem",
             "on_release": lambda x=i: callback(x)}
            for i in items
        ]
        return MDDropdownMenu(caller=caller, items=menu_items, width_mult=4)

    def create_dynamic_menu(self, data_key, callback):
        items = app_data.get(data_key, [])
        menu_items = [
            {"text": i, "viewclass": "OneLineListItem",
             "on_release": lambda x=i: callback(x)}
            for i in items
        ]
        menu_items.append({
            "text": "Добавить",
            "viewclass": "OneLineListItem",
            "on_release": lambda: self.show_add_dialog(data_key, callback)
        })
        return MDDropdownMenu(caller=None, items=menu_items, width_mult=4)

    # Выпадающее меню "Сохранить" теперь центрировано независимо от размера экрана
    def create_save_menu(self):
        caller = self.ids.get("top_app_bar")
        if not caller:
            print("Warning: 'top_app_bar' не найден в ids. Проверьте, что в kv-файле MDTopAppBar имеет id: top_app_bar.")
            return
        menu_items = [
            {"text": "Сохранить", "viewclass": "OneLineListItem",
             "on_release": lambda x="save": self._on_save_option("save")},
            {"text": "Сохранить как...", "viewclass": "OneLineListItem",
             "on_release": lambda x="save_as": self._on_save_option("save_as")},
            {"text": "Загрузить таблицу", "viewclass": "OneLineListItem",
             "on_release": lambda x="load": self._on_save_option("load")}
        ]
        self.save_menu = MDDropdownMenu(caller=caller, items=menu_items, width_mult=4)
        self.save_menu.pos_hint = {"center_x": 0.5, "center_y": 0.5}

    def open_save_menu(self):
        if not self.save_menu:
            self.create_save_menu()
        if self.save_menu:
            self.save_menu.open()
        else:
            print("save_menu не инициализирован.")

    def _on_save_option(self, option):
        self.save_menu.dismiss()
        if option == "save":
            self.save_table_data()
        elif option == "save_as":
            self.save_table_as()
        elif option == "load":
            self.load_saved_table_dialog()

    def show_add_dialog(self, data_key, callback):
        dialog = MDDialog(
            title="Добавить элемент",
            type="custom",
            content_cls=MDTextField(hint_text="Новый элемент", font_size="10sp"),
            buttons=[
                MDFlatButton(text="Ok", font_size="10sp",
                             on_release=lambda x: self.add_new_value(data_key, callback, dialog)),
                MDFlatButton(text="Отмена", font_size="10sp",
                             on_release=lambda x: dialog.dismiss())
            ],
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        dialog.open()

    def add_new_value(self, data_key, callback, dialog):
        new_value = dialog.content_cls.text.strip()
        if new_value and new_value not in app_data.get(data_key, []):
            app_data[data_key].append(new_value)
            save_data(app_data)
            callback(new_value)
        dialog.dismiss()

    def show_method_menu(self, caller):
        self.method_menu.caller = caller
        self.method_menu.open()

    def show_type_menu(self, caller):
        self.wood_type_menu.caller = caller
        self.wood_type_menu.open()

    def show_price_menu(self, caller):
        self.price_menu.caller = caller
        self.price_menu.open()

    def show_sort_menu(self, caller):
        self.sort_menu.caller = caller
        self.sort_menu.open()

    def show_quantity_menu(self, caller):
        self.quantity_menu.caller = caller
        self.quantity_menu.open()

    def set_method(self, value):
        self.ids.method_button.text = value
        self.selected_method = value
        self.update_volume()
        self.method_menu.dismiss()
        self.recalc_table_entries()

    def set_wood_type(self, value):
        self.ids.wood_type_button.text = value
        self.wood_type_menu.dismiss()

    def set_price(self, value):
        self.ids.price_button.text = value
        if "price_output" in self.ids:
            self.ids.price_output.text = value
        self.price_menu.dismiss()

    def set_sort(self, value):
        self.ids.sort_button.text = value
        self.sort_menu.dismiss()

    def set_quantity(self, value):
        self.ids.quantity_button.text = value
        if "quantity_output" in self.ids:
            self.ids.quantity_output.text = value
        self.quantity_menu.dismiss()

    def calculate_volume(self):
        try:
            diameter = float(self.ids.diameter_input.text)
            length = float(self.ids.length_input.text)
            price_text = self.ids.price_button.text.strip()
            price = float(price_text) if price_text else 0
            quantity_text = self.ids.quantity_button.text.strip()
            quantity = float(quantity_text) if quantity_text else 1
            volume, unit, total = calculate_volume(
                diameter, length, log_quantity=quantity, method=self.selected_method
            )
            self.ids.result_label.text = f"Объем: {volume:.6f}{unit} "
            species = self.ids.wood_type_button.text if "wood_type_button" in self.ids else ""
            grade = self.ids.sort_button.text if "sort_button" in self.ids else ""
            self.log_table.add_log_entry(diameter, length, self.ids.method_button.text,
                                         quantity, species, grade, price, total)
            self.update_total_v()
        except ValueError:
            self.ids.result_label.text = "Ошибка ввода"

    def update_volume(self):
        try:
            diameter = float(self.ids.diameter_input.text)
            length = float(self.ids.length_input.text)
            quantity = float(self.ids.quantity_button.text or 1)
            if self.selected_method:
                volume, unit, total = calculate_volume(
                    diameter, length, log_quantity=quantity, method=self.selected_method
                )
                self.ids.result_label.text = f"{volume:.6f}"
        except ValueError:
            self.ids.result_label.text = ""

    def recalc_table_entries(self):
        new_entries = []
        entries = self.log_table.get_entries()
        for row in entries:
            try:
                if len(row) == 7:
                    diameter = float(row[0])
                    length = float(row[1])
                    quantity = float(row[2])
                    price = float(row[5])
                    method = self.selected_method
                    wood = row[3]
                    sort = row[4]
                elif len(row) >= 8:
                    diameter = float(row[0])
                    length = float(row[1])
                    method = row[2]
                    quantity = float(row[3])
                    wood = row[4]
                    sort = row[5]
                    price = float(row[6])
                else:
                    new_entries.append(row)
                    continue
                volume, unit, total = calculate_volume(diameter, length,
                                                       log_quantity=quantity,
                                                       method=self.selected_method)
                new_row = [f"{diameter}", f"{length}", self.selected_method,
                           f"{quantity}", wood, sort, f"{price}", f"{total:.2f}"]
                new_entries.append(new_row)
            except Exception:
                new_entries.append(row)
        self.log_table.load_entries(new_entries)
        self.update_total_v()

    def update_total_v(self):
        total_vol = 0.0
        for row in self.log_table.get_entries():
            try:
                total_vol += float(row[7])
            except Exception:
                continue
        self.ids.total_v.text = f"{total_vol:.6f}"

    def save_table_data(self):
        try:
            metadata = {
                "method": self.ids.method_button.text if "method_button" in self.ids else "",
                "wood_type": self.ids.wood_type_button.text if "wood_type_button" in self.ids else "",
                "price": self.ids.price_button.text if "price_button" in self.ids else "",
                "sort": self.ids.sort_button.text if "sort_button" in self.ids else "",
                "quantity": self.ids.quantity_button.text if "quantity_button" in self.ids else ""
            }
            table_entries = self.log_table.get_entries() if hasattr(self, "log_table") else []
            from screen.history_screen import HistoryScreen
            history_screen = self.manager.get_screen('history_screen')
            history_screen.save_current_table(metadata, table_entries)
            self.ids.result_label.text = "Таблица сохранена"
        except Exception as e:
            self.ids.result_label.text = f"Ошибка сохранения: {e}"

    def save_table_as(self):
        dialog_height = Window.height * 0.5
        input_field = MDTextField(hint_text="Введите имя таблицы", font_size="10sp")
        scroll = ScrollView(size_hint=(1, None), height=dialog_height)
        scroll.add_widget(input_field)
        dialog = MDDialog(
            title="Сохранить как...",
            type="custom",
            content_cls=scroll,
            buttons=[
                MDFlatButton(text="Сохранить", font_size="10sp",
                             on_release=lambda x: self._on_save_as(dialog, input_field.text)),
                MDFlatButton(text="Отмена", font_size="10sp",
                             on_release=lambda x: dialog.dismiss())
            ],
            size_hint=(0.9, None),
            height=dialog_height,
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        dialog.open()

    def _on_save_as(self, dialog, table_name):
        dialog.dismiss()
        try:
            metadata = {
                "table_name": table_name,
                "method": self.ids.method_button.text if "method_button" in self.ids else "",
                "wood_type": self.ids.wood_type_button.text if "wood_type_button" in self.ids else "",
                "price": self.ids.price_button.text if "price_button" in self.ids else "",
                "sort": self.ids.sort_button.text if "sort_button" in self.ids else "",
                "quantity": self.ids.quantity_button.text if "quantity_button" in self.ids else ""
            }
            table_entries = self.log_table.get_entries() if hasattr(self, "log_table") else []
            from screen.history_screen import HistoryScreen
            history_screen = self.manager.get_screen('history_screen')
            history_screen.save_current_table(metadata, table_entries)
            self.ids.result_label.text = f"Таблица '{table_name}' сохранена"
        except Exception as e:
            self.ids.result_label.text = f"Ошибка сохранения: {e}"
        self.clear_log_table()

    def load_saved_table_dialog(self):
        files = [f for f in os.listdir('.') if f.startswith("table_data_") and f.endswith(".json")]
        if not files:
            dialog = MDDialog(
                title="Загрузить таблицу",
                text="Нет сохранённых таблиц",
                size_hint=(0.9, None),
                height=Window.height * 0.3,
                buttons=[MDFlatButton(text="ОК", font_size="10sp", on_release=lambda x: dialog.dismiss())],
                pos_hint={"center_x": 0.5, "center_y": 0.5}
            )
            dialog.open()
            return
        md_list = []
        for fname in files:
            item = OneLineListItem(text=fname, size_hint_y=None, height=dp(40))
            item.bind(on_release=lambda x, fn=fname: self._on_load_table(fn))
            md_list.append(item)
        scroll = self._get_scroll_for_dialog(md_list)
        dialog = MDDialog(
            title="Выберите таблицу для загрузки",
            type="custom",
            content_cls=scroll,
            size_hint=(0.9, None),
            height=Window.height * 0.6,
            buttons=[MDFlatButton(text="Отмена", font_size="10sp", on_release=lambda x: dialog.dismiss())],
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        dialog.open()

    def _get_scroll_for_dialog(self, widgets):
        from kivy.uix.scrollview import ScrollView
        from kivymd.uix.list import MDList
        scroll = ScrollView(size_hint=(1, None), height=Window.height * 0.3)
        md_list = MDList()
        for widget in widgets:
            md_list.add_widget(widget)
        scroll.add_widget(md_list)
        return scroll

    def _on_load_table(self, filename):
        from utils.storage import load_table as load_table_storage
        data = load_table_storage(filename)
        if isinstance(data, dict) and "data" in data:
            entries = data["data"]
        else:
            entries = data
        self.log_table.load_entries(entries)
        self.ids.result_label.text = f"Загружена таблица: {filename}"
        self.update_total_v()

    def add_custom_method(self, new_method):
        if new_method and new_method not in getattr(self, "methods", []):
            if not hasattr(self, "methods"):
                self.methods = []
            self.methods.append(new_method)
            self.save_methods()

    def open_export_menu(self):
        menu_items = [
            {"text": "PDF", "viewclass": "OneLineListItem",
             "on_release": lambda x="PDF": self.show_export_dialog(x)},
            {"text": "Word", "viewclass": "OneLineListItem",
             "on_release": lambda x="Word": self.show_export_dialog(x)},
            {"text": "Excel", "viewclass": "OneLineListItem",
             "on_release": lambda x="Excel": self.show_export_dialog(x)},
        ]
        self.export_menu = MDDropdownMenu(caller=self.ids.top_app_bar, items=menu_items, width_mult=4)
        self.export_menu.open()

    def show_export_dialog(self, export_format):
        self.export_menu.dismiss()
        content = MDBoxLayout(orientation="vertical", spacing="10dp", size_hint_y=None)
        content.height = "400dp"
        self.export_options = {}
        for option in ["Метод", "Порода древесины", "Сорт", "Цена"]:
            row = MDBoxLayout(orientation="horizontal", size_hint_y=None, height="30dp")
            checkbox = MDCheckbox(active=True)
            label = MDFlatButton(text=option, disabled=True, font_size="10sp")
            row.add_widget(checkbox)
            row.add_widget(label)
            content.add_widget(row)
            self.export_options[option] = checkbox
        self.header_nom = MDTextField(hint_text="Номер накладной", font_size="10sp")
        self.header_supplier = MDTextField(hint_text="Поставщик", font_size="10sp")
        self.header_contractor = MDTextField(hint_text="Контрагент", font_size="10sp")
        content.add_widget(self.header_nom)
        content.add_widget(self.header_supplier)
        content.add_widget(self.header_contractor)
        self.export_dialog = MDDialog(
            title=f"Экспорт в {export_format}",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(text="Отмена", font_size="10sp",
                             on_release=lambda x: self.export_dialog.dismiss()),
                MDFlatButton(text="Экспорт", font_size="10sp",
                             on_release=lambda x: self.do_export(export_format))
            ],
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.export_dialog.open()

    def do_export(self, export_format):
        self.export_dialog.dismiss()
        selected_columns = [key for key, chk in self.export_options.items() if chk.active]
        header_info = {
            "Номер накладной": self.header_nom.text,
            "Поставщик": self.header_supplier.text,
            "Контрагент": self.header_contractor.text,
            "Метод": self.ids.method_button.text if "method_button" in self.ids else ""
        }
        data = self.log_table.get_entries()
        filename = f"export_{int(time.time())})"
        if export_format == "PDF":
            filename += ".pdf"
            export_to_pdf(data, filename, header_info, selected_columns)
        elif export_format == "Word":
            filename += ".docx"
            export_to_word(data, filename, header_info, selected_columns)
        elif export_format == "Excel":
            filename += ".xlsx"
            export_to_excel(data, filename, header_info, selected_columns)
        self.ids.result_label.text = f"Экспорт завершен: {filename}"

    def confirm_clear_log(self):
        dialog = MDDialog(
            title="Очистка таблицы",
            text="Сохранить результат перед очисткой?",
            buttons=[
                MDFlatButton(text="Да", font_size="10sp",
                             on_release=lambda x: self.prompt_save_before_clear(dialog)),
                MDFlatButton(text="Нет", font_size="10sp",
                             on_release=lambda x: self.clear_log_table()),
                MDFlatButton(text="Отмена", font_size="10sp",
                             on_release=lambda x: dialog.dismiss())
            ],
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        dialog.open()

    def prompt_save_before_clear(self, parent_dialog):
        parent_dialog.dismiss()
        input_field = MDTextField(hint_text="Введите имя файла", text="table_data", font_size="10sp")
        dialog = MDDialog(
            title="Сохранить таблицу",
            type="custom",
            content_cls=input_field,
            buttons=[
                MDFlatButton(text="Сохранить", font_size="10sp",
                             on_release=lambda x: self._on_save_before_clear(dialog, input_field.text.strip())),
                MDFlatButton(text="Отмена", font_size="10sp",
                             on_release=lambda x: dialog.dismiss())
            ],
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        dialog.open()

    def _on_save_before_clear(self, dialog, table_name):
        dialog.dismiss()
        try:
            metadata = {
                "table_name": table_name,  # Имя, заданное пользователем
                "method": self.ids.method_button.text if "method_button" in self.ids else "",
                "wood_type": self.ids.wood_type_button.text if "wood_type_button" in self.ids else "",
                "price": self.ids.price_button.text if "price_button" in self.ids else "",
                "sort": self.ids.sort_button.text if "sort_button" in self.ids else "",
                "quantity": self.ids.quantity_button.text if "quantity_button" in self.ids else ""
            }
            table_entries = self.log_table.get_entries() if hasattr(self, "log_table") else []
            from screen.history_screen import HistoryScreen
            history_screen = self.manager.get_screen('history_screen')
            history_screen.save_current_table(metadata, table_entries)
            self.ids.result_label.text = f"Таблица '{table_name}' сохранена"
        except Exception as e:
            self.ids.result_label.text = f"Ошибка сохранения: {e}"
        self.clear_log_table()

    def clear_log_table(self):
        self.log_table.load_entries([])
        if "total_v" in self.ids:
            self.ids.total_v.text = "0.000000"

    # Диалог редактирования строки: содержимое (ScrollView с полями)
    # и контейнер с иконками объединяются в один BoxLayout.
    # Используются две иконки – зелёная галочка для подтверждения и красный крест для удаления.
    def show_edit_dialog(self, row_index, row_data):
        from kivy.uix.boxlayout import BoxLayout
        # Контейнер для полей редактирования
        content = BoxLayout(orientation="vertical", spacing="10dp", size_hint_y=None)
        for text, hint in zip(row_data,
                              ["Диаметр", "Длина", "Метод", "Количество", "Порода", "Сорт", "Цена", "V(m3)"]):
            field = MDTextField(text=text, hint_text=hint, font_size="10sp",
                                size_hint_y=None, height=dp(40))
            content.add_widget(field)
        # Функция для пересчета объёма при изменении полей
        def recalc_row(*args):
            try:
                d = float(content.children[7].text)
                l = float(content.children[6].text)
                q = float(content.children[5].text)
                m = content.children[4].text
                volume, unit, total = calculate_volume(d, l, q, method=m)
                content.children[0].text = f"{volume:.6f}{unit}"
            except Exception:
                content.children[0].text = "Ошибка ввода"
        for i in [7,6,5,4]:
            content.children[i].bind(text=lambda inst, val: recalc_row())
        scroll = ScrollView(size_hint=(1, None), height=min(content.height, Window.height * 0.8))
        scroll.add_widget(content)
        # Контейнер для иконок: зелёная галочка (ОК) и красный крест (удалить)
        icon_container = BoxLayout(orientation="horizontal", size_hint_y=None, height=dp(80), spacing=dp(20))
        btn_ok = MDIconButton(icon="check-circle", theme_text_color="Custom", text_color=(0, 1, 0, 1),
                               on_release=lambda x: save_edit())
        btn_delete = MDIconButton(icon="close-circle", theme_text_color="Custom", text_color=(1, 0, 0, 1),
                                   on_release=lambda x: delete_row())
        icon_container.add_widget(btn_ok)
        icon_container.add_widget(btn_delete)
        # Объединяем ScrollView с полями и контейнер с иконками в один общий контейнер
        container = BoxLayout(orientation="vertical")
        container.add_widget(scroll)
        container.add_widget(icon_container)
        dialog = MDDialog(
            title="Редактирование строки",
            type="custom",
            content_cls=container,
            size_hint=(0.9, None),
            height=Window.height * 0.8,
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        def save_edit():
            new_row = []
            for child in content.children[::-1]:
                new_row.append(child.text)
            self.log_table.update_entry(row_index, new_row)
            self.update_total_v()
            dialog.dismiss()
        def delete_row():
            self.log_table.delete_entry(row_index)
            self.update_total_v()
            dialog.dismiss()
        dialog.open()

    def _set_method_in_field(self, field, method):
        field.text = method
        if "Метод_menu" in self.edit_fields:
            self.edit_fields["Метод_menu"].dismiss()

    def open_column_menu(self):
        pass

    def open_dialog(self):
        self.dialog.open()

    def open_length_menu(self):
        # Заглушка для вызова метода из kv-файла (on_focus команды)
        print("open_length_menu() вызван в MainScreen")