from pynput.keyboard import Controller, Key, Listener
from pynput import mouse
import pyscreenshot
import pytesseract
import time

'''
Script for screenshotting text and typing it back by pressing selected key
'''
TYPE_DELAY = 0.01
SELECTED_KEY = Key.caps_lock


def on_click(x, y, button, pressed):
    if pressed:
        on_click.px = x
        on_click.py = y
    else:
        on_click.rx = x
        on_click.ry = y
    if not pressed:
        return False

def on_press(key):
    if key == SELECTED_KEY:
        for i in text:
            keyboard.press(i)
            keyboard.release(i)
            time.sleep(TYPE_DELAY)

if __name__ == "__main__":
    time.sleep(3) # Give time to screenshot

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    image = pyscreenshot.grab(bbox=(on_click.px, on_click.py, on_click.rx, on_click.ry))
    text = str(pytesseract.image_to_string(image,lang = 'eng'))

    keyboard = Controller()
    with Listener(on_press=on_press) as listener:
        listener.join()



    