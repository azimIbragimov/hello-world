import eel 
from googletrans import Translator
eel.init('web')
translator = Translator()

@eel.expose
def translate(text, dest, src):
    translation = translator.translate(text, dest=dest, src=src).text
    return translation



eel.start('index.html', size=(700, 700), block=False)

while True:
    eel.sleep(10)