#!/usr/bin/python3

import sys

parametro = "ninguno"

def uso():
    print("selector.py recibe los siguientes parametros:")
    print("  enciende - Enciende todos los leds")
    print("  apaga - Apaga todos los leds")
    print("  paresynones - Enciende pares y después nones")
    print(" ")
    print("Ejemplo: selector.py enciende")

def evaluar(comando):
    acciones = {
            "enciende": 1,
            "apaga": 0,
            "paresynones": 2
            }
    orden_arduino = acciones.get(comando)
    if orden_arduino is None:
        print ("Comando inválido")
        sys.exit(1)
    return orden_arduino

if len(sys.argv) < 2:
    uso()
    sys.exit(1)
else:
    parametro = sys.argv[1]



print ("El parametro fue: ", parametro)
print ("Accion para arduino: ", evaluar(parametro))
