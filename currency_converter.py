from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

import requests

# Where USD is the base currency you want to use
url = 'https://prime.exchangerate-api.com/v5/16061c8419794ea9c103a980/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data['conversion_rates']["RUB"])

Builder.load_file("design.kv")

class ConverterScreen(Screen):
    def convert(self):
        print(self.ids.currency.text)
        print(self.ids.amount.text)
        try:
            self.ids.result.text = str(self.ids.amount.text) + "$ = " + str(data['conversion_rates'][self.ids.currency.text] * int(self.ids.amount.text))+ str(self.ids.currency.text)
        except:
            self.ids.result.text = "Sorry - we do not support this currency"



        print(self.ids.result)

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
