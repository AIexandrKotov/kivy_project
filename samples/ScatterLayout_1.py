# модуль ScatterLayout_1.py
from kivy.app import App
from kivy.lang import Builder
KV = '''
<Picture@ScatterLayout>:
    source: None
    size: image.size
    size_hint: None, None
    Image:
        id: image
        source: root.source
    RelativeLayout:
        canvas:
            Rectangle:
                source: './Images/Fon2.jpg'
                size: self.size
                pos: self.pos
        Picture:
            source: './Images/Dog.jpg'
        Picture:
            source: './Images/forest.jpg'
        Picture:
            source: './Images/Elena.jpg'
'''
class MyApp(App):
    def build(self):
        return Builder.load_string(KV)
MyApp().run()
# ВНИМАНИЕ! Код не работает (он неправильный). Искать ошибку в чужом коде лишь на этапе изучения фреймворка я не буду.