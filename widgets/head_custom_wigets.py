from kivymd.uix.toolbar import MDTopAppBar
from kivy.metrics import dp
from kivy.clock import Clock
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton

class SmallTopAppBar(MDTopAppBar):
    def __init__(self, **kwargs):
        kwargs.setdefault("size_hint_y", None)
        kwargs.setdefault("height", dp(20))  # уменьшаем высоту до 20 dp
        super().__init__(**kwargs)
        self.height = dp(20)
        Clock.schedule_once(self.adjust_widgets, 0)

    def adjust_widgets(self, dt):
        self._recursive_set_font(self, "14sp")
        self._recursive_set_icon(self, dp(16))  # задаем новый размер иконок, например 16 dp

    def _recursive_set_font(self, widget, font_size):
        if isinstance(widget, MDLabel):
            widget.font_size = font_size
        if hasattr(widget, "children"):
            for child in widget.children:
                self._recursive_set_font(child, font_size)

    def _recursive_set_icon(self, widget, size):
        if isinstance(widget, MDIconButton):
            widget.icon_size = size  # устанавливаем размер иконки
        if hasattr(widget, "children"):
            for child in widget.children:
                self._recursive_set_icon(child, size)