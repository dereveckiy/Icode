from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.metrics import sp

from screen.main_screen import MainScreen
from screen.settings_screen import SettingsScreen
from screen.history_screen import HistoryScreen
from screen.calculation_screen import CalculationScreen
from screen.c_s_table import CSTableScreen   # Новый экран


# Загружаем все kv-файлы
Builder.load_file("kivy_files/main_screen.kv")
Builder.load_file("kivy_files/settings_screen.kv")
Builder.load_file("kivy_files/history_screen.kv")
Builder.load_file("kivy_files/drawer.kv")
Builder.load_file("kivy_files/calculation_screen.kv")
Builder.load_file("kivy_files/c_s_table.kv")    # Новый kv

class KubaturnikApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.font_styles["Body1"] = ["Roboto", sp(10), 0.15, 0]
        
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main_screen"))
        sm.add_widget(SettingsScreen(name="settings_screen"))
        sm.add_widget(HistoryScreen(name="history_screen"))
        sm.add_widget(CalculationScreen(name="calculation_screen"))
        sm.add_widget(CSTableScreen(name="c_s_table"))    # Добавляем экран c_s_table
        sm.current = "main_screen"
        return sm

if __name__ == "__main__":
    KubaturnikApp().run()