# модуль Scatter_2.py
from kivy.app import App
from kivy.lang import Builder
KV = '''
RelativeLayout:
    Scatter:
        Image:
            source: './Images/forest.jpg'
'''
class MainApp(App):
    def build(self):
        return Builder.load_string(KV)
MainApp().run()
