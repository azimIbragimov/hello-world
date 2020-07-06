from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from yahoo_fin import stock_info as si
from yahoo_fin.stock_info import *

"""
This app displays current price of stocks
"""

# Creation of GUI
Builder.load_file("design.kv")

class Stock(Screen):
    """
    Searches for the information from the stock market
    """
    def find(self):
        try:
            # name of the comapny
            self.ids.informationstock.text = self.ids.company.text + "\n"

            # finds current price
            self.ids.informationstock.text += "Current price of this stock is: \n" + str(si.get_live_price(self.ids.company.text))

            # finds major share holders
            self.ids.informationstock.text += "\n\n" + 'Major holders: ' + "\n"
            for item in get_holders(self.ids.company.text)['Direct Holders (Forms 3 and 4)']['Holder']:
                 print(item)
                 self.ids.informationstock.text += str(item) + "\n"
        except:

            # displays the information if there is no company that the user provided
            self.ids.informationstock.text = "No information was found" + ('\n' * 8)

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
