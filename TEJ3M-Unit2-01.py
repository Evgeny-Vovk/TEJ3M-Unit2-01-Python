# Copyright(c) 2023 Evgeny Vovk All rights reserved.
# Created by : Evgeny Vovk
# Created on : Fabruary 2023
# TEJ3M-Unit2-01.py File.

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
