# модуль K_CheckBox_1.py
from kivy.app import App
from kivy.uix.checkbox import CheckBox
class MainApp(App):
    def build(self):
        checkbox = CheckBox()
        return checkbox
MainApp().run()
