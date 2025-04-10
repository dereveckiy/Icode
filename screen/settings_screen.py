from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.app import MDApp

class SettingsScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file("c:/Users/38098/Desktop/progect/p1/Icode/kivy_files/settings_screen.kv")
        self.language_dialog = None
        self.privacy_dialog = None

    def change_language(self):
        languages = ["Русский", "English", "Español"]
        buttons = []
        for lang in languages:
            btn = MDFlatButton(text=lang, on_release=lambda x, l=lang: self.set_language(l))
            buttons.append(btn)
        self.language_dialog = MDDialog(
            title="Выберите язык",
            type="custom",
            text="",
            buttons=buttons
        )
        self.language_dialog.open()

    def set_language(self, lang):
        app = MDApp.get_running_app()
        app.language = lang
        print(f"Выбран язык: {lang}")
        if self.language_dialog:
            self.language_dialog.dismiss()
        Clock.schedule_once(lambda dt: app.update_global_language_texts(), 0.5)

    def toggle_theme(self):
        app = MDApp.get_running_app()
        if app.theme_cls.theme_style == "Light":
            app.theme_cls.theme_style = "Dark"
        else:
            app.theme_cls.theme_style = "Light"
        Clock.schedule_once(lambda dt: app.update_global_theme(), 1.0)
        print(f"Текущая тема: {app.theme_cls.theme_style}")

    def _apply_dark_text_icons(self):
        app = MDApp.get_running_app()
        root = app.root
        for widget in root.walk():
            if widget.__class__.__name__ in ['MDTextField', 'MDLabel', 'MDIconButton', 'MDTopAppBar']:
                widget.theme_text_color = "Custom"
                widget.text_color = (1, 1, 1, 1)
        if self.privacy_dialog:
            for widget in self.privacy_dialog.walk():
                if hasattr(widget, "text_color"):
                    widget.theme_text_color = "Custom"
                    widget.text_color = (1, 1, 1, 1)

    def show_privacy_policy(self):
        from kivy.uix.scrollview import ScrollView
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.core.window import Window
        from kivy.metrics import dp

        # Разбиваем текст политики на более мелкие блоки. Каждый блок отделён несколькими переводами строки.
        paragraphs = [
            "Privacy Policy\n\n\n",
            "Effective Date:\nApril 7, 2025\n\n\n",
            "PP DR.IT.\n(“we”, “our”, or “us”)\nbuilt the\nForest Calc app\nas a free app.\n\n\n",
            "This SERVICE\nis provided by us\nand is intended\nfor use as is.\n\n\n",
            "This page is used\nto inform visitors\nregarding our policies\nwith the collection,\nuse, and disclosure\nof Personal Information\nif anyone decides\nto use our Service.\n\n\n",
            "Information Collection\nand Use\n\n\n",
            "We do not collect\npersonally identifiable information\nfrom users unless\nexplicitly stated.\n\n\n",
            "The app may use\nthird-party services\nthat may collect\ninformation used to\nidentify you.\n\n\n",
            "Link to the privacy policy\nof third-party service\nproviders used by the app:\n\n\n",
            "Google Play Services\n\n\n",
            "Firebase\n\n\n",
            "Log Data\n\n\n",
            "In case of an error in the app,\nwe collect data and information\n(through third-party products)\non your phone\ncalled Log Data.\n\n\n",
            "This Log Data may include\ninformation such as your device\nIP address,\ndevice name,\noperating system version,\napp configuration,\nand the time and date\nof your use of the Service.\n\n\n",
            "Cookies\n\n\n",
            "Cookies are not explicitly used\nby our app. However, third-party\nservices may use cookies\nto collect information\nand improve their services.\nYou can choose to accept\nor refuse these cookies\nthrough your device settings.\n\n\n",
            "Security\n\n\n",
            "We value your trust in\nproviding your information,\nthus we strive to use\ncommercially acceptable means\nof protecting it.\nBut remember that no method\nof transmission over the\ninternet or method of\nelectronic storage is\n100% secure.\n\n\n",
            "Children’s Privacy\n\n\n",
            "Our app does not knowingly\ncollect personally identifiable\ninformation from children under 13.\nIf we discover that a child under 13\nhas provided us with personal\ninformation, we will delete it immediately.\n\n\n",
            "Changes to This Privacy Policy\n\n\n",
            "We may update our Privacy Policy\nfrom time to time.\nYou are advised to review this page\nperiodically for any changes.\nWe will notify you\nof any changes by posting\nthe new Privacy Policy\non this page.\n\n\n",
            "Contact Us\n\n\n",
            "If you have any questions\nor suggestions about our Privacy Policy,\ndo not hesitate\nto contact us at\nparket.dreveks@gmail.com."
        ]
        policy_text = "".join(paragraphs)

        # Рассчитываем размеры диалога адаптивно
        dialog_width = min(Window.width * 0.95, 600)
        dialog_height = Window.height * 0.8

        # Создаем ScrollView с включенной горизонтальной и вертикальной прокруткой
        scroll = ScrollView(
            size_hint=(None, None),
            size=(dialog_width, dialog_height),
            do_scroll_x=True,
            do_scroll_y=True
        )
        # Контейнер с отступами, растягивающийся по ширине ScrollView
        content = BoxLayout(
            orientation='vertical',
            size_hint=(1, None),
            padding=(dp(10), dp(10))
        )
        content.bind(minimum_height=lambda inst, val: setattr(inst, 'height', val))

        # Label с автоматическим переносом строк и включенным markup
        label = Label(
            text=policy_text,
            size_hint=(1, None),
            halign="left",
            valign="top",
            font_size="10sp",
            markup=True
        )
        # Функция обновления text_size с учетом отступа (20 dp)
        def update_label_text_size(*args):
            label.text_size = (content.width - dp(20), None)
        label.bind(width=lambda inst, val: update_label_text_size())
        content.bind(width=lambda inst, val: update_label_text_size())
        label.bind(texture_size=lambda inst, size: setattr(label, 'height', size[1] + dp(20)))

        content.add_widget(label)
        scroll.add_widget(content)

        # Функция обновления размеров при изменении окна
        def update_layout(*args):
            new_width = min(Window.width * 0.95, 600)
            scroll.size = (new_width, Window.height * 0.8)
            content.width = new_width
            update_label_text_size()
        Window.unbind(on_resize=update_layout)
        Window.bind(on_resize=update_layout)
        Clock.schedule_once(update_layout, 0)

        self.privacy_dialog = MDDialog(
            title="Политика конфиденциальности",
            type="custom",
            content_cls=scroll,
            buttons=[MDFlatButton(text="Закрыть", on_release=lambda x: self.privacy_dialog.dismiss())]
        )
        self.privacy_dialog.open()

    def update_language(self, trans):
        if "top_app_bar" in self.ids:
            self.ids.top_app_bar.title = trans["settings_title"]
        print("SettingsScreen texts updated.")