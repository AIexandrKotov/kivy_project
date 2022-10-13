# Модуль StencilView_1.py
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.stencilview import StencilView
from kivy.uix.scatter import Scatter
class MainApp(App):
    def build(self):
        stv = StencilView() # контейнер – трафарет
        sc = Scatter() # контейнер – конвертор
        sc.add_widget(Image(source='./Images/Fon2.jpg'))
        stv.add_widget(sc) # положить конвертор в трафарет
        return stv
MainApp().run()
