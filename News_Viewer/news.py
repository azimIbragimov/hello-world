from selenium import webdriver
from selenium.common.exceptions import *
from webdriver_manager.chrome import ChromeDriverManager
import time

class Infogetter():

    """
    This module uses selenuim to webscrape the follwing websites websites:
    CNN.com
    nytimes.com
    instagram.com
    mashable.com
    amazon.com

    In addition, you can search for speicifc results in:
    cnn.com
    amazon.com

    And it performs login operation on:
    instagram


    """

    def __init__(self):
        # Sets up the Chrome browser
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")

        options.add_argument('--headless')
        options.add_argument('--allow-running-insecure-content')
        options.add_argument('start-maximized')
        options.add_argument('disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--ignore-certificate-errors')

        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')

        options.add_argument("--proxy-server='direct://")
        options.add_argument("--proxy-bypass-list=*")
        options.add_argument("--start-maximized")
        options.add_argument("acceptInsecureCerts")






        webdriver_path = 'C://Users//azimc//chromedriver.exe' # Enter the file directory of the Chromedriver
        self.browser = webdriver.Chrome(webdriver_path, options=options)



    def cnn(self):
        """
        Searches for the latest news on the cnn website
        """
        website = 'https://www.cnn.com/us'
        self.browser.get(website)
        search_form = self.browser.find_elements_by_tag_name('h3')
        result = []
        print("The app found the following results \n --------------------")
        for item in search_form:
            try:
                result.append((item.text, item.find_element_by_css_selector("a").get_attribute("href")))
            except:
                pass

        print(result)
        return result

    def cnn_search(self, message):
        """
        Searches for news about specific topic

        Arguments:
        self - instance of the class
        message - search request
        """
        website = 'https://www.cnn.com/us'
        self.browser.get(website)
        search_form = self.browser.find_element_by_class_name('search-icon')
        search_form.click()
        search_bar = self.browser.find_element_by_id('header-search-bar')
        search_bar.send_keys(message)
        search_bar.submit()

        time.sleep(1)
        search_words = self.browser.find_elements_by_tag_name('h3')
        print("The app found the following results \n --------------------")
        for item in search_words:
            print(item.text)

    def nytimes(self):
        """
        Searches for the latest news on the nytimes website
        """
        website = 'https://www.nytimes.com'
        self.browser.get(website)
        search_form = self.browser.find_elements_by_class_name('css-6p6lnl')
        print("The app found the following results \n --------------------")
        result = []


        for item in search_form:
            print(item.text)
            result.append((item.text, item.find_element_by_css_selector("a").get_attribute("href")))

        print(result)
        return result[3:]

    def insta(self, username, password):
        """
        Logs in into user's account and gives the latest posts from their feed

        Arguments:
        self - instance of the class
        username - Instagram username
        passowrd - Instagram Password

        """
        website = 'https://www.instagram.com'
        self.browser.get(website)
        time.sleep(2)
        username = self.browser.find_element_by_name('username')
        username.send_keys(username)
        password = self.browser.find_element_by_name("password")
        password.send_keys(password)
        password.submit()
        time.sleep(2)
        notnow = self.browser.find_element_by_class_name("cmbtv")
        notnow.click()
        time.sleep(2)
        later = self.browser.find_element_by_class_name("mt3GC")
        later.click()
        time.sleep(2)
        information = self.browser.find_elements_by_tag_name('article')
        print(information)
        for item in information:
            try:
                print(item.text)
            except:
                pass


    def mashable(self):
        """
        Provides the latest news from the mashable website
        """

        website = 'https://mashable.com/'
        self.browser.get(website)
        search_form = self.browser.find_elements_by_tag_name('h2')
        for item in search_form:
            print(item.text)

    def amazon(self, item):
        """
        searches for a specific item and gives the search results

        Arguments:
        self - instance of the class
        item - name of item that you want to find
        """

        website = 'https://www.amazon.com/'
        self.browser.get(website)
        search_form = self.browser.find_element_by_id('twotabsearchtextbox')
        search_form.send_keys(item)
        search_form.submit()
        time.sleep(2)
        search = self.browser.find_elements_by_tag_name("h2")
        price = self.browser.find_elements_by_class_name("a-price-whole")

        for unit, cost in zip(search, price):
            try:
                print(unit.text)
            except:
                pass

            try:
                print(cost.text + "$")
            except:
                pass

    def foxnews(self):
        """
        Provides the latest news from the Fox News
        """
        website = 'https://www.foxnews.com/'
        self.browser.get(website)
        time.sleep(1)
        search_form = self.browser.find_elements_by_tag_name('h2')
        print(search_form)
        print("The app found the following results \n --------------------")
        result = []


        for item in search_form:
            print(item.text)
            result.append((item.text, item.find_element_by_css_selector("a").get_attribute("href")))

        print(result)
        return result


    def vox(self):
        """
        Provides the latest news from the Forbes
        """
        website = 'https://www.vox.com/'
        self.browser.get(website)
        time.sleep(1)
        search_form = self.browser.find_elements_by_tag_name('h2')
        print("The app found the following results \n --------------------")
        result = []


        for item in search_form:
            try:
                result.append((item.text, item.find_element_by_css_selector("a").get_attribute("href")))
            except:
                pass

        print(result)
        return result






if __name__ == "__main__":
    prog = Infogetter()
    prog.cnn()
