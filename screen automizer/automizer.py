from pynput.mouse import Button, Controller
import pynput
import time

mouse = Controller()
keyboard = pynput.keyboard.Controller()

def move(x, y): 
    print('The current pointer position is {0}'.format(
    mouse.position))


    location_x = x
    location_y = y

    mouse.position = (int(location_x), int(location_y))
    print('Now we have moved it to {0}'.format(
    mouse.position))

def click():
    mouse.click(Button.left, 1)


def type(text):
    keyboard.type(text)

def find_app(app_name):
    move(50, 990)
    click()
    time.sleep(1)
    type(app_name)
    time.sleep(1)
    move(235, 450)
    click()
    time.sleep(1)

class Chrome():
    
    def type(self, text):
        time.sleep(1)
        type(text)
        keyboard.press(pynput.keyboard.Key.enter)
        keyboard.release(pynput.keyboard.Key.enter)

    def new_tab(self):
        time.sleep(1)
        keyboard.press(pynput.keyboard.Key.ctrl)
        keyboard.press('t')
        keyboard.release(pynput.keyboard.Key.ctrl)
        keyboard.release('t')


find_app("Youtube Music Desktop App")
find_app("AtomProjects")
find_app("wallpaper.py")
find_app("Visual Studio 2019")
find_app("Google Chrome")

Browser = Chrome()
Browser.type("www.nytimes.com")
Browser.new_tab()
Browser.type("www.gmail.com")


