from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty
from kivy.graphics import Color, Mesh
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton

class ParallelogramButton(ButtonBehavior, BoxLayout):
    text = StringProperty("")
    icon = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.padding = '10dp'
        self.spacing = '5dp'  # Уменьшили расстояние между иконкой и текстом
        self.bind(pos=self.update_shape, size=self.update_shape)

        self.icon_widget = MDIconButton(
            icon=self.icon,
            size_hint=(None, None),
            size=(30, 30),
            pos_hint={"center_y": 0.5}
        )
        self.text_widget = MDLabel(
            text=self.text,
            halign="center",
            valign="middle",
            size_hint=(None, None),
            size=(100, 30),
            pos_hint={"center_y": 0.5}
        )
        self.add_widget(self.icon_widget)
        self.add_widget(self.text_widget)

    def update_shape(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)  # Цвет кнопки
            Mesh(
                vertices=[
                    self.x + 10, self.y, 0, 0,
                    self.right, self.y, 1, 0,
                    self.right - 10, self.top, 1, 1,
                    self.x, self.top, 0, 1,
                ],
                indices=[0, 1, 2, 2, 3, 0],
                mode="triangle_fan"
            )

        # Обновляем иконку и текст
        self.icon_widget.icon = self.icon
        self.text_widget.text = self.text

        # Размещаем иконку и текст внутри кнопки
        self.icon_widget.center_x = self.center_x - 40
        self.text_widget.center_x = self.center_x + 20

        # Масштабируем текст и иконку при изменении размеров экрана
        self.icon_widget.size = (self.height * 0.6, self.height * 0.6)
        self.text_widget.font_size = self.height * 0.4