import requests
from bs4 import BeautifulSoup
import sqlite3

"""
This application searches for the information on the USF's website and saves them in a database
"""

# Connecting to the datebase
db = sqlite3.connect("C://Users//azimc//IdeaProjects//Atomprojects//contentagregator//contegrator.db")
cursor = db.cursor()
#Creates a tabel if one does not already exist
cursor.execute('CREATE TABLE IF NOT EXISTS board (parent name, title name, link name)')

def view_the_datebase():
    # Views all distinct entries in the database
    string = f'SELECT DISTINCT title, link FROM board'
    cursor.execute(string)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def add_USF():
    # searches for data on the usf's website
    URL = 'https://www.usf.edu/news/listing.aspx'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    results = soup.find_all('div', class_ = 'newsItem')
    for search in results:
        title = search.find('h2', class_ = 'newsItem_headline').text
        link = "https://www.usf.edu" + search.find('a', href = True)['href']
        query = f"INSERT INTO board (parent, title, link) VALUES ('usf.edu','{title}', '{link}')"
        cursor.execute(query)

    db.commit()


# add new entries in the databse
add_USF()
# views the database
view_the_datebase()
#closes the database
db.close()
