import eel 
import news

eel.init('web')

@eel.expose
def find_cnn():
    articles = news.Infogetter().cnn()
    return articles

@eel.expose
def find_ny():
    articles = news.Infogetter().nytimes()
    return articles

@eel.expose
def find_vox():
    articles = news.Infogetter().vox()
    return articles


@eel.expose
def find_fox():
    articles = news.Infogetter().foxnews()
    return articles




eel.start('index.html', size=(700, 700), block=False)

while True:
    eel.sleep(10)