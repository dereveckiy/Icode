from kivymd.uix.list import OneLineListItem
from kivy.properties import BooleanProperty, ListProperty

class CustomOneLineItem(OneLineListItem):
    highlight = BooleanProperty(False)
    bg_color = ListProperty([0, 0, 0, 0])
    
    def on_highlight(self, instance, value):
        # При выделении фон становится салатовым, иначе прозрачным
        self.bg_color = (0.5, 1, 0.5, 1) if value else (0, 0, 0, 0)