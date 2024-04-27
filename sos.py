#!/usr/bin/python

import gpiod
import time

def morse_code_signal(line, symbol):
    if symbol == ".":
        line.set_value(1)
        time.sleep(0.2)  # Duración del punto
        line.set_value(0)
        time.sleep(0.2)  # Espacio entre partes de la misma letra
    elif symbol == "-":
        line.set_value(1)
        time.sleep(0.6)  # Duración de la raya
        line.set_value(0)
        time.sleep(0.2)  # Espacio entre partes de la misma letra

def morse_code_sos(line):
    # Representación de SOS en Morse: ... --- ...
    for symbol in "... --- ...":
        morse_code_signal(line, symbol)
        if symbol == " ":
            time.sleep(0.6)  # Espacio entre letras

chip = gpiod.Chip('gpiochip0')
line_number = 196
led = chip.get_line(line_number)
led.request(consumer='gpio_led_morse', type=gpiod.LINE_REQ_DIR_OUT)

try:
    while True:
        morse_code_sos(led)
        time.sleep(5)  # Espera 5 segundos antes de repetir
finally:
    led.release()
