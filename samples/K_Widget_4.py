# модуль K_Widget_4.py
from kivy.app import App
from kivy.lang import Builder
KV = '''
Widget:
    canvas:
        #Color:
        #rgba: 1, 0, 0, 1
        Rectangle:
            source: './Images/Fon2.jpg'
            pos: self.pos
            size: self.size
'''
class MainApp(App):
    def build(self):
        return Builder.load_string(KV)
MainApp().run()