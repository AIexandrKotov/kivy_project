# модуль K_Switch1.py
from kivy.app import App
from kivy.uix.switch import Switch
class MainApp(App):
    def build(self):
        sw = Switch(active=True)
        return sw
MainApp().run()
