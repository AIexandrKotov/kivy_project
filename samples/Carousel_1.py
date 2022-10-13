# модуль Carousel_1.py
from kivy.lang import Builder
from kivy.app import App
KV = '''
Carousel:
    direction: 'right'
    BoxLayout:
        Image:
            source: './Images/Fon2.jpg'
    BoxLayout:
        Image:
            source: './Images/Elena.jpg'
    BoxLayout:
        Image:
            source: './Images/Dog.jpg'
    BoxLayout:
        Image:
            source: './Images/Elena.jpg'
'''
class MainApp(App):
    def build(self):
        return Builder.load_string(KV)
MainApp().run()
#Это всё демонстрационные файлы, какие конкретно изображения используются - неважно.