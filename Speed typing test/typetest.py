"""
This application measures user's typping speed and accuracy
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import datetime, json,random

# reads the deign.kv file
Builder.load_file("designing.kv")

# reads the file with english words
file =  open('C:/Users/azimc/IdeaProjects/Atomprojects/Typing speed test/data1.json')
data = json.load(file)


class TypingScreen(Screen):
    def start(self):

        """
        Detects the time when the code was executed and displays a random string
        on the GUI
        """
        try:
            self.ids.your_text.text = ""
            self.starting = datetime.datetime.now()
            string = ''
            for _ in range(10):
                string += str(random.choice(list(data))) + " "
            self.ids.text_test.text = string
        except:
            pass

    def finish(self):
        """
        Calculates the time between the 1st and the 2nd calculation and gives
        mesaurements of speed and accuracy
        """
        try:
            result = datetime.datetime.now() -self.starting
            print(type(result.seconds))
            self.ids.speed.text = str(len(self.ids.your_text.text)*(60/result.seconds))
            print(len(self.ids.your_text.text))

            errors = 0

            for letter1, letter2 in zip(self.ids.your_text.text, self.ids.text_test.text):
                if letter1 == letter2:
                    pass
                else:
                    errors += 1


            self.ids.errors.text = str(errors)

            self.ids.text_test.text = ""
        except:
            pass


class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
