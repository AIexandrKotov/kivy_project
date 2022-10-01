import kivy.app
from kivy.uix.label import Label

class MainApp(kivy.app.App):
    def build(self):
        self.title = "Здарова мужики"
        label = Label(text="test text")
        return label


if __name__ == "__main__":
    app = MainApp()
    app.run()
