# модуль K_ToggleButton_1.py
from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
class MainApp(App):
    def build(self):
        t_but = ToggleButton(text='Кнопка',
        font_size=50)
        return t_but
MainApp().run()
