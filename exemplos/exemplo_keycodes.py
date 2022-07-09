import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_win_br import KeyboardLayout
from adafruit_hid.keycode_win_br import Keycode

import board
from digitalio import DigitalInOut, Direction, Pull

time.sleep(2)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayout(keyboard) 


keyboard.send(Keycode.ALT, Keycode.TAB)
#keyboard.press(Keycode.ALT,Keycode.TAB)
time.sleep(2)
keyboard.release_all()
