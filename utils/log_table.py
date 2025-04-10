import re
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.factory import Factory

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.menu import MDDropdownMenu

from utils.calculations import calculate_volume

Builder.load_file("c:/Users/38098/Desktop/progect/p1/Icode/kivy_files/log_table.kv")

class LogTable(BoxLayout):
    cell_font_size = StringProperty("10sp")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._rows = []
        self.toggle_settings = {"Порода": False}
        self.create_table()
        Window.bind(on_resize=self.on_window_resize)
    
    def on_window_resize(self, instance, width, height):
        Clock.schedule_once(lambda dt: self.create_table(), 0)
    
    def update_row_numbers(self):
        for i, row in enumerate(self._rows):
            if isinstance(row, tuple) and len(row) >= 1:
                rest = row[1:]
                self._rows[i] = (str(i+1),) + rest
            else:
                self._rows[i] = (str(i+1),) + tuple(row)
    
    def create_table(self):
        self.update_row_numbers()
        if "table_container" not in self.ids:
            return
        container = self.ids.table_container
        container.clear_widgets()
        for index, row in enumerate(self._rows):
            row_layout = BoxLayout(orientation="horizontal", spacing=dp(2),
                                   size_hint_y=None, height=dp(30))
            for cell in row:
                label = Factory.MyLabel(
                    text=str(cell),
                    halign="center",
                    font_size=self.cell_font_size,
                    font_style="Body1",
                    size_hint_x=1,
                    theme_text_color="Custom",
                    text_color=(0, 0, 0, 1)
                )
                row_layout.add_widget(label)
            def on_touch(instance, touch, idx=index):
                if instance.collide_point(*touch.pos):
                    self.edit_row(idx)
                return False
            row_layout.bind(on_touch_down=on_touch)
            container.add_widget(row_layout)
        self.update_summary()
    
    def update_summary(self):
        total_qty = len(self._rows)
        total_vol = 0.0
        total_price = 0.0
        print("[DEBUG] Обновление сводки. Текущие записи:")
        for idx, row in enumerate(self._rows):
            print(f"[DEBUG] Row {idx}: {row}")
            try:
                vol_str = row[7].strip()
                vol = float(vol_str)
            except Exception as e:
                print(f"[DEBUG] Ошибка преобразования объёма в строке {idx}: '{row[7]}' ({e})")
                vol = 0.0
            try:
                price_str = row[9].strip()
                price = float(price_str)
            except Exception as e:
                print(f"[DEBUG] Ошибка преобразования цены в строке {idx}: '{row[9]}' ({e})")
                price = 0.0
            total_vol += vol
            total_price += price
        if "summary_vol" in self.ids:
            self.ids.summary_vol.text = f"Общий V(m3): {total_vol:.6f}"
        if "summary_qty" in self.ids:
            self.ids.summary_qty.text = f"Всего шт: {total_qty}"
        if "summary_price" in self.ids:
            self.ids.summary_price.text = f"Общая цена: {total_price:.2f}"
    
    def update_table(self):
        self.create_table()
    
    def add_log_entry(self, diameter, length, method, quantity, species, grade, price, total_volume):
        try:
            vol = float(total_volume)
        except Exception:
            vol = 0.0
        vol_str = f"{vol:.6f}"
        try:
            unit_price = float(price)
        except Exception:
            unit_price = 0.0
        total_price = unit_price * vol
        row = (
            str(len(self._rows) + 1),
            str(diameter),
            str(length),
            method,
            str(1),
            species,
            grade,
            vol_str,
            str(price),
            f"{total_price:.2f}"
        )
        self._rows.append(row)
        print("[DEBUG] Добавлена запись:", row)
        self.update_table()
    
    def get_entries(self):
        return self._rows
    
    def clear_entries(self):
        self._rows = []
        print("[DEBUG] Записи очищены")
        self.update_table()
    
    def edit_row(self, row_index):
        if row_index < 0 or row_index >= len(self._rows):
            return
        old_values = list(self._rows[row_index])
        from kivy.uix.scrollview import ScrollView
        scroll = ScrollView(size_hint=(1, None), size=(self.width, dp(300)))
        from kivymd.uix.boxlayout import MDBoxLayout
        content = MDBoxLayout(orientation="vertical", spacing="12dp", size_hint_y=None)
        content.bind(minimum_height=content.setter("height"))
        scroll.add_widget(content)
        
        self.edit_fields = {}
        for col, idx in {"D(cm)": 1, "L(m)": 2, "Метод": 3, "Кол-во": 4,
                         "Порода": 5, "Сорт": 6, "Цена": 8}.items():
            if col == "Метод":
                field = MDTextField(
                    hint_text=col,
                    text=str(old_values[idx]) if idx < len(old_values) else "",
                    size_hint_x=1,
                    size_hint_y=None,
                    height=dp(40)
                )
                method_list = ["ISO 4480-83", "Doyle Log Rule", "Scribner Log Rule",
                               "International 1/4 Log Rule", "JAS Scale", "Hoppus Log Rule", "ГОСТ 2708-75"]
                from kivymd.uix.menu import MDDropdownMenu
                menu_items = [{"text": m, "viewclass": "OneLineListItem", "on_release": lambda x, m=m, f=field: self._set_method_in_field(f, m)}
                              for m in method_list]
                method_menu = MDDropdownMenu(caller=field, items=menu_items, width_mult=4)
                field.bind(focus=lambda instance, value: method_menu.open() if value else None)
                self.edit_fields[col] = field
                self.edit_fields["Метод_menu"] = method_menu
                content.add_widget(field)
            else:
                current_value = old_values[idx] if idx < len(old_values) else ""
                field = MDTextField(
                    hint_text=col,
                    text=str(current_value),
                    size_hint_x=1,
                    size_hint_y=None,
                    height=dp(40)
                )
                self.edit_fields[col] = field
                content.add_widget(field)
        
        volume_field = MDTextField(
            hint_text="V(m3)",
            text=old_values[7] if len(old_values) > 7 else "",
            size_hint_x=1,
            size_hint_y=None,
            height=dp(40),
            readonly=True
        )
        self.edit_fields["V(m3)"] = volume_field
        content.add_widget(volume_field)
        
        def recalc_row(*args):
            try:
                d = float(self.edit_fields["D(cm)"].text)
                l = float(self.edit_fields["L(m)"].text)
                q = float(self.edit_fields["Кол-во"].text or 1)
                m = self.edit_fields["Метод"].text
                volume, unit, total = calculate_volume(d, l, q, method=m)
                volume_field.text = f"{volume:.6f}{unit}"
            except Exception:
                volume_field.text = "Ошибка ввода"
        self.edit_fields["D(cm)"].bind(text=lambda inst, val: recalc_row())
        self.edit_fields["L(m)"].bind(text=lambda inst, val: recalc_row())
        self.edit_fields["Кол-во"].bind(text=lambda inst, val: recalc_row())
        self.edit_fields["Метод"].bind(text=lambda inst, val: recalc_row())
        
        def on_save(_):
            edited_diameter = self.edit_fields["D(cm)"].text
            edited_length = self.edit_fields["L(m)"].text
            edited_method = self.edit_fields["Метод"].text
            edited_quantity = self.edit_fields["Кол-во"].text
            edited_species = self.edit_fields["Порода"].text
            edited_grade = self.edit_fields["Сорт"].text
            edited_price = self.edit_fields["Цена"].text
            try:
                q_val = float(edited_quantity) if edited_quantity.strip() != "" else 1
                d_val = float(edited_diameter)
                l_val = float(edited_length)
                volume, unit, tot_vol = calculate_volume(d_val, l_val, q_val, method=edited_method)
            except Exception:
                tot_vol = 0
            vol_str = f"{tot_vol:.6f}"
            try:
                unit_price = float(edited_price) if edited_price.strip() != "" else 0
            except Exception:
                unit_price = 0
            new_total_price = unit_price * tot_vol
            new_row = [
                old_values[0],
                edited_diameter,
                edited_length,
                edited_method,
                edited_quantity,
                edited_species,
                edited_grade,
                vol_str,
                edited_price if edited_price.strip() != "" else "0",
                f"{new_total_price:.2f}"
            ]
            self.update_entry(row_index, new_row)
            self.dialog.dismiss()
        
        def on_delete(_):
            self._rows.pop(row_index)
            self.update_table()
            self.dialog.dismiss()
        
        self.dialog = MDDialog(
            title="Редактировать строку",
            type="custom",
            content_cls=scroll,
            buttons=[
                MDFlatButton(text="ОК", on_release=on_save),
                MDFlatButton(text="Удалить", on_release=on_delete),
                MDFlatButton(text="Отмена", on_release=lambda _: self.dialog.dismiss())
            ]
        )
        self.dialog.open()
    
    def update_entry(self, row_index, new_row):
        if 0 <= row_index < len(self._rows):
            self._rows[row_index] = tuple(new_row)
            self.update_table()
    
    def _set_method_in_field(self, field, method):
        field.text = method
        if "Метод_menu" in self.edit_fields:
            self.edit_fields["Метод_menu"].dismiss()
    
    def open_column_menu(self):
        pass
    
    def open_dialog(self):
        self.dialog.open()