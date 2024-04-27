import gpiod
import time

CHIP_NAME = 'gpiochip0'
PIN_NUMBER = 196

chip = gpiod.Chip(CHIP_NAME)

line = chip.get_line(PIN_NUMBER)
line.request(consumer='read_switch', type=gpiod.LINE_REQ_DIR_IN)

print("Iniciando monitoreo del switch. Presiona CTRL+C para terminar.")

try:
   while True:
      state = line.get_value()
      if state == 1:
         print("Switch abierto (OFF)")
      else:
         print("Switch cerrado (ON)")
      time.sleep(0.5)

except KeyboardInterrupt:
   print("Finalizando monitoreo del switch.")

line.release()
