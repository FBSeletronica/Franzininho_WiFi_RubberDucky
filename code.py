
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_win_br import KeyboardLayout
import adafruit_ducky

import board
from digitalio import DigitalInOut, Direction, Pull

time.sleep(1)
# Configura o pino do botão
btn = DigitalInOut(board.IO0)       # 
btn.direction = Direction.INPUT     # 
btn.pull = Pull.UP                  # 

# Configura o pino do led
led_blue = DigitalInOut(board.IO21)       #
led_blue.direction = Direction.OUTPUT    # 

led_yellow = DigitalInOut(board.IO33)       # 
led_yellow.direction = Direction.OUTPUT    # 


keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayout(keyboard)  # 
duck = adafruit_ducky.Ducky("duckyscript.txt", keyboard, keyboard_layout)

time.sleep(5)
led_yellow.value = 1

result = True
running = False
while result is not False:
    if btn.value ==0 :
        running = True
        led_blue.value = 1
        time.sleep(0.2)
    if running:
        result = duck.loop()
