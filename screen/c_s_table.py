import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivy.factory import Factory
from utils.storage import save_table, load_table

Builder.load_file("c:/Users/38098/Desktop/progect/p1/Icode/kivy_files/c_s_table.kv")

class CSTableScreen(Screen):
    def set_table(self, table):
        self.ids.table_box.clear_widgets()
        self.ids.table_box.add_widget(table)

    def open_save_load_menu(self):
        self.saveload_dialog = MDDialog(
            title="Выберите действие",
            text="Сохранить таблицу или загрузить историю?",
            buttons=[
                MDFlatButton(text="Сохранить", on_release=self.open_save_dialog),
                MDFlatButton(text="Загрузить", on_release=self.open_load_dialog)
            ]
        )
        self.saveload_dialog.open()

    def open_save_dialog(self, instance):
        self.saveload_dialog.dismiss()
        content = Factory.MDTextField(hint_text="Введите имя файла для сохранения", font_size="14sp")
        self.save_dialog = MDDialog(
            title="Сохранение таблицы",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(text="ОК", on_release=self._save_table),
                MDFlatButton(text="Отмена", on_release=lambda x: self.save_dialog.dismiss())
            ]
        )
        self.save_dialog.open()

    def _save_table(self, instance):
        file_name = self.save_dialog.content_cls.text.strip()
        if not file_name:
            file_name = "table_data.json"
        else:
            if not file_name.endswith(".json"):
                file_name += ".json"
        try:
            if self.ids.table_box.children:
                log_table = self.ids.table_box.children[0]
                entries = log_table.get_entries()
                save_table(entries, filename=file_name)
                dialog = MDDialog(title="Сохранение", text=f"Сохранено в {file_name}")
            else:
                dialog = MDDialog(title="Сохранение", text="Нет таблицы для сохранения.")
        except Exception as e:
            dialog = MDDialog(title="Сохранение", text=f"Ошибка: {e}")
        self.save_dialog.dismiss()
        dialog.open()

    def open_load_dialog(self, instance):
        self.saveload_dialog.dismiss()
        saved_files = [f for f in os.listdir('.') if f.endswith(".json")]
        if not saved_files:
            dialog = MDDialog(title="Загрузка", text="Нет сохранённых таблиц.")
            dialog.open()
            return
        from kivymd.uix.list import OneLineListItem, MDList
        from kivy.uix.scrollview import ScrollView
        md_list = MDList(size_hint_y=None)
        md_list.bind(minimum_height=md_list.setter('height'))
        for file_name in saved_files:
            item = OneLineListItem(
                text=file_name,
                on_release=lambda x, fn=file_name: self._select_load_item(fn)
            )
            md_list.add_widget(item)
        scroll = ScrollView(size_hint=(1, None), height=200)
        scroll.add_widget(md_list)
        self.load_dialog = MDDialog(
            title="Выберите файл для загрузки",
            type="custom",
            content_cls=scroll,
            buttons=[
                MDFlatButton(text="Отмена", on_release=lambda x: self.load_dialog.dismiss())
            ]
        )
        self.load_dialog.open()

    def _select_load_item(self, file_name):
        try:
            entries = load_table(filename=file_name)
            entries = [tuple(row) for row in entries]
            if self.ids.table_box.children:
                log_table = self.ids.table_box.children[0]
                log_table._rows = entries
                log_table.update_table()
                if hasattr(log_table, "update_summary"):
                    log_table.update_summary()
                dialog = MDDialog(title="Загрузка", text=f"Загружено из {file_name}")
            else:
                dialog = MDDialog(title="Загрузка", text="Нет таблицы для загрузки.")
        except Exception as e:
            dialog = MDDialog(title="Загрузка", text=f"Ошибка: {e}")
        self.load_dialog.dismiss()
        dialog.open()

    def open_export_dialog(self, instance):
        if hasattr(self, "saveload_dialog"):
            self.saveload_dialog.dismiss()
        content = Factory.MDTextField(hint_text="Введите имя файла для экспорта", font_size="14sp")
        self.export_dialog = MDDialog(
            title="Экспорт таблицы",
            type="custom",
            content_cls=content,
            buttons=[
                MDIconButton(icon="file-pdf-box", on_release=lambda x: self._export_table("pdf")),
                MDIconButton(icon="file-word-box", on_release=lambda x: self._export_table("docx")),
                MDIconButton(icon="file-excel-box", on_release=lambda x: self._export_table("xlsx")),
                MDIconButton(icon="close-circle", theme_text_color="Custom", text_color=(1, 0, 0, 1),
                              on_release=lambda x: self.export_dialog.dismiss())
            ]
        )
        self.export_dialog.open()

    def _export_table(self, file_type):
        file_name = self.export_dialog.content_cls.text.strip()
        if not file_name:
            file_name = f"exported_table.{file_type}"
        else:
            if not file_name.endswith(f".{file_type}"):
                file_name += f".{file_type}"
        try:
            if self.ids.table_box.children:
                log_table = self.ids.table_box.children[0]
                entries = log_table.get_entries()
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(f"Экспорт таблицы в {file_type.upper()} формате:\n")
                    for row in entries:
                        f.write(",".join(row) + "\n")
                dialog = MDDialog(title="Экспорт", text=f"Экспортировано в {file_name}")
            else:
                dialog = MDDialog(title="Экспорт", text="Нет таблицы для экспорта.")
        except Exception as e:
            dialog = MDDialog(title="Экспорт", text=f"Ошибка: {e}")
        self.export_dialog.dismiss()
        dialog.open()