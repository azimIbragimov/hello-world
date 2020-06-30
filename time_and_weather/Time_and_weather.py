"""
This code creates a app that can display location, local time and weather information of the user

"""

from tkinter import *
from datetime import datetime
import geocoder
import pyowm


class Time_Screen():
    
    """Creates a text displaying local time of the user"""
    
    def __init__(self):
        self.main_frame = Frame(time_window)
        self.main_frame.configure(bg='#F8B195')
        
        #gets local time and displays it
        self.time_text = Label(self.main_frame,
        text = f"Current time in your city is \n {datetime.now().strftime('%H:%M:%S')}")    
                               
        self.time_text.config(font=("Courier", 30))
                               
      

    def tick(self):
                               
        """Updates the local time text every second"""
                               
        time_string = f"Current time in your city is \n {datetime.now().strftime('%H:%M:%S')}"
        self.time_text.config(text=time_string, bg='#F67280')
        self.time_text.after(200, self.tick)

    def set_time_screen(self):
                               
        """Creates the rest of the screen. This code was divide into a separate function to make it easier in
        the future to edit the code"""
                               
        self.main_frame.grid(row=1, column=0, columnspan=4, rowspan=10)
        self.main_frame.columnconfigure(0, weight=3)
        self.time_text.grid(row=0, column = 0, pady = 50)
        self.tick()

                               
class Location():
                               
    """Determines user's location based on his/her IP address
    and then shows it on the main screen"""
                               
    def __init__(self):
        g = geocoder.ipinfo('me')
        
        # this variable contains user's location information.
        self.location = g.state
                               
        area = Label(screen1.main_frame, text = self.location)
        area.config(font=("Courier", 12), bg='#FF847C')
        area.grid(row=2, column=0, pady=20)

                               
class Temperature():
    """Determines user's weather information and displays it on the main screen"""
    def __init__(self):
        
        # Weather API
        owm = pyowm.OWM('bdd55d1709471376e90cf4f8b9152c9b')
        city = str(location.location)
        observation = owm.weather_at_place(city)
        w = observation.get_weather()

        # Displays the data infomration. 
        self.temp_text = Label(screen1.main_frame,
        text = f"Weather Data: \n\n Current temperature in fahrenheit: {w.get_temperature('fahrenheit')['temp']} \n" +
               f"Current temperature in celcius: {w.get_temperature('celsius')['temp']}\n\n " +
               f"Hottest temperature today in fahrenheit: {w.get_temperature('fahrenheit')['temp_max']}\n " +
               f"Hottest temperature in celcuis {w.get_temperature('celsius')['temp_max']} \n\n" +
               f"Humidity: {w.get_humidity()}% \n Wind: {w.get_wind()['speed']} mph \n\n\n " +
               f"It is {w.get_status().lower()} outside")
        
        self.temp_text.config(font=("Courier", 15), bg='#FFD3B5')
        self.temp_text.grid(column=0, row=3)

# setting up the GUI                               
time_window=Tk()
time_window.configure(bg='#F8B195')
time_window.geometry('800x800')
time_window.minsize(800, 800)
blank = Label(time_window, text = " ")
blank.configure(font=("Courier", 30), bg='#F8B195')
time_window.columnconfigure(0, weight=3)
                               
# Using the classes
screen1 = Time_Screen()
screen1.set_time_screen()
location = Location()
temp = Temperature()

screen1.tick()

time_window.mainloop()
