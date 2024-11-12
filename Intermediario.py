import gpiod
from gpiod.line import Direction, Value

import threading
import time

class Intermediario:
    def __init__(self):
        print("Activando la electronica")

        # Definicion de puertos para termostato
        self.LM555 = 14

        self.FocosC1 = 17
        self.FocosC2 = 27

        # Variables

        self.X_00 =  False

        self.Y_00 =  False
        self.Y_01 =  False

        self.funcion_pines = False
        self.configurar_senal()

    def configurar_senal (self):
        print('Mandando la senal')

        self.chip = gpiod.request_lines(
            "/dev/gpiochip4",
            config = {
                #Senal entrada
                self.LM555: gpiod.LineSettings(direction=Direction.INPUT),

                #Senal salida
                self.FocosC1: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE),
                self.FocosC2: gpiod.LineSettings(direction=Direction.OUTPUT, output_value=Value.INACTIVE)
            },
        )
        self.tarea = threading.Thread(target=self.iniciar)
        self.tarea.start()

    def iniciar (self):
        self.funcion_pines = True
        while self.funcion_pines:
            self.X_00 = True if self.chip.get_value(self.LM555) == Value.ACTIVE else False

            self.chip.set_value(self.FocosC1,Value.ACTIVE if self.Y_00 == True else Value.INACTIVE)
            self.chip.set_value(self.FocosC2,Value.ACTIVE if self.Y_01 == True else Value.INACTIVE)

            time.sleep(0.001)

    def detener(self):
        self.funcion_pines = False
        if self.tarea:
            self.tarea.join()

def main():
    intermediario = Intermediario()
    intermediario.Y_00 = True

if __name__ == "__main__":
    main()

