"""
This code creates a app that can display local time of the user, timer, count-down clock, and an alarm clock.

"""

from tkinter import *
from datetime import datetime
import geocoder


time_window=Tk()
time_window.configure(bg='#F8B195')
time_window.geometry('800x800')
time_window.minsize(800, 800)
blank = Label(time_window, text = " ")
blank.configure(font=("Courier", 30), bg='#F8B195')

time_window.columnconfigure(0, weight=3)

class Time_Screen():

    def __init__(self):
        self.main_frame = Frame(time_window)
        self.main_frame.configure(bg='#F8B195')
        self.time_text = Label(self.main_frame,
        text = f"Current time in your city is \n {datetime.now().strftime('%H:%M:%S')}")
        self.time_text.config(font=("Courier", 30))

    def tick(self):
        time_string = f"Current time in your city is \n {datetime.now().strftime('%H:%M:%S')}"
        self.time_text.config(text=time_string, bg='#F67280')
        self.time_text.after(200, self.tick)

    def set_time_screen(self):

        self.main_frame.grid(row=1, column=0, columnspan=4, rowspan=10)
        self.main_frame.columnconfigure(0, weight=3)
        self.time_text.grid(row=0, column = 0, pady = 50)
        self.tick()

class Location():

    def __init__(self):
        g = geocoder.ipinfo('me')
        self.location = g.state
        area = Label(screen1.main_frame, text = self.location)
        area.config(font=("Courier", 12), bg='#FF847C')

        area.grid(row=2, column=0, pady=20)

class Temperature():
    def __init__(self):
        import pyowm
        city = str(location.location)
        owm = pyowm.OWM('bdd55d1709471376e90cf4f8b9152c9b')
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        print(w)
        print(f"It is {w.get_temperature('fahrenheit')['temp']} degrees fahrenheit/ {w.get_temperature('celsius')['temp']} degrees celcius in {city}")
        self.temp_text = Label(screen1.main_frame,
        text = f"Weather Data: \n\n Current temperature in fahrenheit: {w.get_temperature('fahrenheit')['temp']} \n Current temperature in celcius: {w.get_temperature('celsius')['temp']}\n\n Hottest temperature today in fahrenheit: {w.get_temperature('fahrenheit')['temp_max']}\n Hottest temperature in celcuis {w.get_temperature('celsius')['temp_max']} \n\n Humidity: {w.get_humidity()}% \n Wind: {w.get_wind()['speed']} mph \n\n\n It is {w.get_status().lower()} outside")
        self.temp_text.config(font=("Courier", 15), bg='#FFD3B5')

        self.temp_text.grid(column=0, row=3)


screen1 = Time_Screen()
screen1.set_time_screen()
location = Location()
temp = Temperature()

screen1.tick()

time_window.mainloop()
