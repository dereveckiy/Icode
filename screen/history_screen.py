import os
import json
import datetime
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton

# Импорт функций экспорта из export.py, включая функцию share_file
from utils.export import export_to_pdf, export_to_word, export_to_excel, share_file

Builder.load_file("kivy_files/history_screen.kv")

class HistoryScreen(Screen):

    def on_enter(self):
        self.load_saved_tables()

    def load_saved_tables(self):
        """
        Загружает список сохранённых таблиц.
        Отображаются файлы с расширениями .json, .pdf, .docx, .xlsx.
        Каждая запись создается как BoxLayout: слева – имя файла, справа – кнопки экспорта, удаления и поделиться.
        """
        if 'saved_tables_list' not in self.ids:
            return
        self.ids.saved_tables_list.clear_widgets()
        files = [f for f in os.listdir('.') if f.endswith((".json", ".pdf", ".docx", ".xlsx"))]
        if not files:
            self.ids.saved_tables_list.add_widget(
                MDLabel(text="Нет сохраненных таблиц", halign="center")
            )
        else:
            for filename in files:
                item_layout = BoxLayout(orientation="horizontal",
                                          size_hint_y=None,
                                          height=dp(48),
                                          padding=[dp(10), 0, dp(10), 0])
                file_label = MDLabel(text=filename,
                                     halign="left",
                                     size_hint_x=1,
                                     valign="middle")
                file_label.bind(on_touch_down=lambda inst, touch, fn=filename: self._open_file(inst, touch, fn))
                btn_layout = BoxLayout(orientation='horizontal', spacing=dp(10),
                                       size_hint_x=None, width=dp(150))
                export_btn = MDIconButton(
                    icon="file-export",
                    size_hint=(None, None),
                    size=(dp(40), dp(40)),
                    on_release=lambda x, fn=filename: self.show_export_dialog(fn)
                )
                delete_btn = MDIconButton(
                    icon="delete",
                    size_hint=(None, None),
                    size=(dp(40), dp(40)),
                    on_release=lambda x, fn=filename: self.delete_table(fn)
                )
                share_btn = MDIconButton(
                    icon="share-variant",
                    size_hint=(None, None),
                    size=(dp(40), dp(40)),
                    on_release=lambda x, fn=filename: share_file(fn)
                )
                btn_layout.add_widget(export_btn)
                btn_layout.add_widget(delete_btn)
                btn_layout.add_widget(share_btn)
                item_layout.add_widget(file_label)
                item_layout.add_widget(btn_layout)
                self.ids.saved_tables_list.add_widget(item_layout)

    def _open_file(self, instance, touch, fn):
        if instance.collide_point(*touch.pos):
            self.load_table(fn)

    def load_table(self, filename):
        """
        Загружает JSON-файл с таблицей и отображает его содержимое в диалоговом окне.
        Если файл не JSON – выводит сообщение об отсутствии предпросмотра.
        """
        if not filename.endswith(".json"):
            MDDialog(
                title="Просмотр недоступен",
                text="Просмотр содержимого экспортированного файла недоступен.",
                size_hint=(0.8, None),
                height=dp(200)
            ).open()
            return
        try:
            with open(filename, "r", encoding="utf-8") as f:
                table_data = json.load(f)
            header_text = ""
            data_entries = []
            if isinstance(table_data, dict) and "metadata" in table_data and "data" in table_data:
                metadata = table_data["metadata"]
                header_text = f"Method: {metadata.get('method','')}"
                if "summary_qty" in metadata:
                    header_text += (
                        f"\nВсего шт: {metadata.get('summary_qty','')}, "
                        f"Общий V(m3): {metadata.get('summary_volume','')}, "
                        f"Общая цена: {metadata.get('summary_total_price','')}"
                    )
                data_entries = table_data["data"]
            elif isinstance(table_data, list):
                data_entries = table_data

            scroll = ScrollView(
                size_hint=(1, None),
                height=dp(300),
                do_scroll_x=True,
                do_scroll_y=True
            )
            content = BoxLayout(orientation="vertical", size_hint_y=None)
            content.bind(minimum_height=content.setter("height"))

            if header_text:
                header_label = MDLabel(
                    text=header_text,
                    halign="left",
                    size_hint_x=None
                )
                header_label.texture_update()
                header_label.width = header_label.texture_size[0] + dp(20)
                header_label.size_hint_y = None
                header_label.height = header_label.texture_size[1] + dp(10)
                content.add_widget(header_label)

            for entry in data_entries:
                if isinstance(entry, dict):
                    text_line = (
                        f"D: {entry.get('diameter','')}, "
                        f"L: {entry.get('length','')}, "
                        f"Qty: {entry.get('quantity','')}, "
                        f"Wood: {entry.get('wood_type','')}, "
                        f"Sort: {entry.get('sort','')}, "
                        f"V: {entry.get('total_volume','')}, "
                        f"Price: {entry.get('price','')}, "
                        f"Total: {entry.get('total_price','')}"
                    )
                elif isinstance(entry, (list, tuple)):
                    temp = list(entry)
                    if temp and str(temp[0]).isdigit():
                        temp = temp[1:]
                    text_line = (
                        f"D: {temp[0] if len(temp) > 0 else ''}, "
                        f"L: {temp[1] if len(temp) > 1 else ''}, "
                        f"Qty: {temp[2] if len(temp) > 2 else ''}, "
                        f"Wood: {temp[3] if len(temp) > 3 else ''}, "
                        f"Sort: {temp[4] if len(temp) > 4 else ''}, "
                        f"V: {temp[5] if len(temp) > 5 else ''}, " 
                        f"Price: {temp[6] if len(temp) > 6 else ''}, "
                        f"Total: {temp[7] if len(temp) > 7 else ''}"
                    )
                else:
                    text_line = ""
                label = MDLabel(
                    text=text_line,
                    halign="left",
                    size_hint_x=None
                )
                label.texture_update()
                label.width = label.texture_size[0] + dp(20)
                label.size_hint_y = None
                label.height = label.texture_size[1] + dp(10)
                content.add_widget(label)

            scroll.add_widget(content)
            MDDialog(
                title=f"Таблица: {filename}",
                type="custom",
                content_cls=scroll,
                size_hint=(0.8, None),
                height=dp(350)
            ).open()
        except Exception as e:
            MDDialog(
                title="Ошибка загрузки",
                text=str(e),
                size_hint=(0.8, None),
                height=dp(200)
            ).open()

    def delete_table(self, filename):
        """
        Удаляет файл таблицы и обновляет список.
        """
        try:
            os.remove(filename)
            MDDialog(
                title="Удалено",
                text=f"Файл {filename} удален",
                size_hint=(0.8, None),
                height=dp(150)
            ).open()
            self.load_saved_tables()
        except Exception as e:
            MDDialog(
                title="Ошибка удаления",
                text=str(e),
                size_hint=(0.8, None),
                height=dp(150)
            ).open()

    def show_export_dialog(self, filename):
        """
        Открывает диалоговое окно для выбора формата экспорта.
        Отображаются кнопки с иконками: PDF, Word, Excel и Отмена.
        """
        export_dialog = MDDialog(
            title="Экспортировать в:",
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDIconButton(icon="file-pdf-box", on_release=lambda x: self._select_export(filename, "pdf", export_dialog)),
                MDIconButton(icon="file-word-box", on_release=lambda x: self._select_export(filename, "word", export_dialog)),
                MDIconButton(icon="file-excel-box", on_release=lambda x: self._select_export(filename, "excel", export_dialog)),
                MDIconButton(icon="close", on_release=lambda x: export_dialog.dismiss())
            ]
        )
        export_dialog.open()

    def _select_export(self, filename, format, dialog):
        dialog.dismiss()
        self.prompt_export_filename(filename, format)

    def prompt_export_filename(self, original_filename, format):
        """
        Открывает диалог ввода имени файла для экспорта.
        """
        self.export_name_field = MDTextField(
            hint_text="Введите имя файла без расширения",
            size_hint_x=0.8,
            pos_hint={"center_x": 0.5}
        )
        export_name_dialog = MDDialog(
            title="Введите имя файла для экспорта",
            type="custom",
            content_cls=self.export_name_field,
            size_hint=(0.8, None),
            height=dp(250),
            buttons=[
                MDIconButton(icon="check", on_release=lambda x: self._do_export(export_name_dialog, original_filename, format)),
                MDIconButton(icon="close", on_release=lambda x: export_name_dialog.dismiss())
            ]
        )
        export_name_dialog.open()

    def _do_export(self, dialog, original_filename, format):
        dialog.dismiss()
        self.export_table_with_name(original_filename, format, self.export_name_field.text)

    def export_table_with_name(self, original_filename, format, user_filename):
        """
        Выполняет экспорт таблицы в выбранном формате с именем,
        указанным пользователем.
        """
        try:
            with open(original_filename, "r", encoding="utf-8") as f:
                table_data = json.load(f)
            if isinstance(table_data, dict):
                data = table_data.get("data", [])
            else:
                data = table_data
            base = user_filename.strip() if user_filename.strip() else os.path.splitext(original_filename)[0]
            if format.lower() == "pdf":
                export_filename = base + ".pdf"
                export_to_pdf(data, export_filename)
            elif format.lower() == "word":
                export_filename = base + ".docx"
                export_to_word(data, export_filename)
            elif format.lower() == "excel":
                export_filename = base + ".xlsx"
                export_to_excel(data, export_filename)
            else:
                raise Exception("Неверно указан формат экспорта")
            MDDialog(
                title="Экспорт выполнен",
                text=f"Файл экспортирован как {export_filename}",
                size_hint=(0.8, None),
                height=dp(200)
            ).open()
        except Exception as e:
            print("Ошибка экспорта:", e)
            MDDialog(
                title="Ошибка экспорта",
                text=str(e),
                size_hint=(0.8, None),
                height=dp(200)
            ).open()

    def save_current_table(self, metadata, table_entries):
        """
        Сохраняет текущую таблицу в файл с итоговыми значениями.
        Имя файла формируется по шаблону: table_data_{table_name}_{timestamp}.json.
        Если пользователь задал имя (metadata["table_name"]), оно используется,
        иначе используется имя на основе метода.
        Итоговые значения суммируются по колонкам (ожидается новый формат строки):
          - Количество: индекс 4
          - V(m3): индекс 7
          - Общая цена: индекс 9
        """
        total_qty = 0.0
        total_vol = 0.0
        total_price = 0.0
        clean_entries = []
        for row in table_entries:
            try:
                if isinstance(row, (list, tuple)):
                    temp = list(row)
                    if temp and str(temp[0]).isdigit():
                        temp = temp[1:]
                    clean_entries.append(temp)
                else:
                    clean_entries.append(row)
                total_qty += float(row[4])
                total_vol += float(row[7])
                total_price += float(row[9])
            except (ValueError, IndexError) as e:
                print("Ошибка при подсчете для строки:", row, e)
                continue

        print("Перед сохранением, metadata =", metadata)
        table_name_input = metadata.get("table_name", "").strip()
        method_val = metadata.get("method", "").strip() or "no_method"
        new_metadata = {"method": method_val}
        new_metadata["summary_qty"] = total_qty
        new_metadata["summary_volume"] = f"{total_vol:.6f}"
        new_metadata["summary_total_price"] = f"{total_price:.2f}"
        if table_name_input:
            new_metadata["table_name"] = table_name_input

        data_to_save = {"metadata": new_metadata, "data": clean_entries}
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        if table_name_input:
            table_safe = table_name_input.replace(" ", "_")
            filename = f"table_data_{table_safe}_{timestamp}.json"
        else:
            method_safe = method_val.replace(" ", "_")
            filename = f"table_data_{method_safe}_{timestamp}.json"
        print("Формируем имя файла:", filename)
        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data_to_save, f, ensure_ascii=False, indent=4)
            print(f"Таблица сохранена в файл: {filename}")
            self.load_saved_tables()
            MDDialog(
                title="Успех",
                text=f"Таблица сохранена как {filename}",
                size_hint=(0.8, None),
                height=dp(200)
            ).open()
        except Exception as e:
            print("Ошибка сохранения:", e)
            MDDialog(
                title="Ошибка сохранения",
                text=str(e),
                size_hint=(0.8, None),
                height=dp(200)
            ).open()

    def delete_table(self, filename):
        """
        Удаляет файл таблицы и обновляет список.
        """
        try:
            os.remove(filename)
            MDDialog(
                title="Удалено",
                text=f"Файл {filename} удален",
                size_hint=(0.8, None),
                height=dp(150)
            ).open()
            self.load_saved_tables()
        except Exception as e:
            MDDialog(
                title="Ошибка удаления",
                text=str(e),
                size_hint=(0.8, None),
                height=dp(150)
            ).open()