import eel 
import ctypes

eel.init('web')

DIRECTORY = "C:/Users/azimc/IdeaProjects/Atomprojects/AAA/wallpaper_changer_app/web/img/speakers/"

@eel.expose
def set_wallpaper_1(): 

    change_wallpaper(DIRECTORY + "1.jpg")

@eel.expose
def set_wallpaper_2(): 
    change_wallpaper(DIRECTORY + "2.jpg")

@eel.expose
def set_wallpaper_3(): 
    change_wallpaper(DIRECTORY + "3.jpg")

@eel.expose
def set_wallpaper_4(): 
    change_wallpaper(DIRECTORY + "4.jpg")

@eel.expose
def set_wallpaper_5(): 
    change_wallpaper(DIRECTORY + "5.jpg")

@eel.expose
def set_wallpaper_6(): 
    change_wallpaper(DIRECTORY + "6.jpg")

@eel.expose
def set_wallpaper_7(): 
    change_wallpaper(DIRECTORY + "7.jpg")

@eel.expose
def set_wallpaper_8(): 
    change_wallpaper(DIRECTORY + "8.jpg")

@eel.expose
def set_wallpaper_9(): 
    change_wallpaper(DIRECTORY + "9.jpg")

@eel.expose
def set_wallpaper_10(): 
    change_wallpaper(DIRECTORY + "10.jpg")

@eel.expose
def set_wallpaper_11(): 
    change_wallpaper(DIRECTORY + "11.jpg")

@eel.expose
def set_wallpaper_12(): 
    change_wallpaper(DIRECTORY + "12.jpg")


def change_wallpaper(picture): 
    SPI_SETDESKWALLPAPER = 20 
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 1, picture, 2)
    print(f"Photo has been changed. Image: {random_picture}")





eel.start('index.html', size=(700, 700), block=False)

while True:
    eel.sleep(10)