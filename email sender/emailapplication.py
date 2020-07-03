"""
Creates an app that can send emails.
To use this app, you should tunr off security settings on your gmail account
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import smtplib, ssl

"""Calles the Kivy file"""
Builder.load_file("design.kv")


class SignInScreen(Screen):

    """ Gathers the filled out information and sends email"""

    def convert(self):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = self.ids.your_address.text
        receiver_email = self.ids.receiver_address.text
        password = self.ids.password.text
        message = self.ids.message.text

        # check if the password is correct and send mail
        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
                self.ids.button1.text = "Sending the message"

        # run if the password is incorrect
        except:
            self.ids.your_address.text = "Incorrect username or password"
            self.ids.password.text = "Incorrect username or password"

        # run if the password is correct
        else:
            self.ids.message.text = "The message has been sent succesfully"
            self.ids.your_address.text = ''
            self.ids.receiver_address.text = ''
            self.ids.password.text = ''
            self.ids.button1.text = 'Submit'



class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
