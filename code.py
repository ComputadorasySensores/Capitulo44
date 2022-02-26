import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

boton1_pin= board.GP16
boton2_pin= board.GP17
boton3_pin= board.GP18
boton4_pin= board.GP19

teclado = Keyboard(usb_hid.devices)

boton1 = digitalio.DigitalInOut(boton1_pin)
boton1.direction = digitalio.Direction.INPUT
boton1.pull = digitalio.Pull.DOWN

boton2 = digitalio.DigitalInOut(boton2_pin)
boton2.direction = digitalio.Direction.INPUT
boton2.pull = digitalio.Pull.DOWN

boton3 = digitalio.DigitalInOut(boton3_pin)
boton3.direction = digitalio.Direction.INPUT
boton3.pull = digitalio.Pull.DOWN

boton4 = digitalio.DigitalInOut(boton4_pin)
boton4.direction = digitalio.Direction.INPUT
boton4.pull = digitalio.Pull.DOWN

while True:
    if boton1.value:
        print("Botón 1 W Arriba Pad A")
        teclado.press(Keycode.W)
        time.sleep(0.1)
        teclado.release(Keycode.W)
    if boton2.value:
        print("Botón 2 S Abajo Pad A")
        teclado.press(Keycode.S)
        time.sleep(0.1)
        teclado.release(Keycode.S)
    if boton3.value:
        print("Botón 3 Flecha Arriba Arriba Pad B")
        teclado.press(Keycode.UP_ARROW)
        time.sleep(0.1)
        teclado.release(Keycode.UP_ARROW)
    if boton4.value:
        print("Botón 4 Flecha Abajo Abajo Pad B")
        teclado.press(Keycode.DOWN_ARROW)
        time.sleep(0.1)
        teclado.release(Keycode.DOWN_ARROW)
    time.sleep(0.1)
