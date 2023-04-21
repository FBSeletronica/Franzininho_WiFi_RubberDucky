# Importação de bibliotecas necessárias
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_win_br import KeyboardLayout
import adafruit_ducky

import board
from digitalio import DigitalInOut, Direction, Pull

# Aguarda 1 segundo para as configurações iniciais
time.sleep(1)

# Configura o pino do botão
btn = DigitalInOut(board.IO0)       # Define o pino do botão
btn.direction = Direction.INPUT     # Define a direção do pino como entrada
btn.pull = Pull.UP                  # Define um resistor pull-up para o pino

# Configura os pinos dos LEDs
led_blue = DigitalInOut(board.IO21)       # Define o pino do LED azul
led_blue.direction = Direction.OUTPUT    # Define a direção do pino como saída

led_yellow = DigitalInOut(board.IO33)       # Define o pino do LED amarelo
led_yellow.direction = Direction.OUTPUT    # Define a direção do pino como saída

# Configuração do teclado USB
keyboard = Keyboard(usb_hid.devices)   # Inicializa o teclado USB
keyboard_layout = KeyboardLayout(keyboard)  # Define o layout do teclado
duck = adafruit_ducky.Ducky("duckyscript.txt", keyboard, keyboard_layout) # Define o objeto Ducky com o script a ser executado

# Aguarda 5 segundos para indicar que o sistema está pronto
time.sleep(5)
led_yellow.value = 1   # Acende o LED amarelo

result = True
running = False

# Loop principal
while result is not False:
    if btn.value ==0 :
        running = True
        led_blue.value = 1  # Acende o LED azul
        time.sleep(0.2)
    if running:
        result = duck.loop()  # Executa o script
# Quando o script termina, acende o LED amarelo
led_yellow.value = 1
