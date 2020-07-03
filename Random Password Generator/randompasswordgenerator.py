from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import random

Builder.load_file("design.kv")

class GeneratorScreen(Screen):
    def generate(self):

        available_letters=['0','1','2','3','4','5','6','7','8','9','q', 'w', 'e',
        'r', 't', 'y', 'u',
        'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'a', 's',
        'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
        "+", "-", "=", 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S',
        'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']

        result = ''
        try:
            for _ in range(int(self.ids.length.text)):
                result += random.choice(available_letters)

            self.ids.password.text = str(result)
        except:
            pass


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
