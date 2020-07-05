"""
This code creates a a Smart Assistant that uses a GUI and Text to speech conversion
"""
# import modules
import wolframalpha
import PySimpleGUI as sg
import wikipedia
import pyttsx3

# initiate wolframalpha's search engine
engine = pyttsx3.init()
client = wolframalpha.Client('84EP9Q-EYGULH6U4Q')
sg.theme('DarkTeal9')

# configuration of the GUI
layout = [  [sg.Text('Smart Assistant')],
            [sg.Text('Enter a command'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Smart Assistant', layout)

#While launching, the app will greed the user
engine.say("Hello, it is very nice to see you again. The window will apear in a couple of seconds")
engine.runAndWait()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    try:
        # gets the first value of the search result
        res = client.query(values[0])
        wolfram_res = next(res.results).text
    except:
        # output this if the engine does not find anything
        wolfram_res = "Sorry we are unable to process your request"

    # say the following words and show it in a pop up window
    engine.say(wolfram_res)
    sg.PopupNonBlocking(wolfram_res)
    engine.runAndWait()
