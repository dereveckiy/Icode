from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder

class Drawer(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file("kivy_files/drawer.kv")