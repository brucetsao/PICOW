import time
import analogio
import board
from digitalio import DigitalInOut, Direction,Pull
import pwmio

x_axis = analogio.AnalogIn(board.A0)
y_axis = analogio.AnalogIn(board.A1)

sw = DigitalInOut(board.GP22)
sw.direction = Direction.INPUT
sw.pull = Pull.UP

led = pwmio.PWMOut(board.GP15,
                   frequency=5000,
                   duty_cycle=0)

buzzer = pwmio.PWMOut(board.GP13,
                      frequency=523,
                      duty_cycle=0)

while True:
    if sw.value == True:
        led.duty_cycle = x_axis.value
        buzzer.duty_cycle = int(y_axis.value/2)
    else:
        led.duty_cycle = 0
        buzzer.duty_cycle = 0
        
    time.sleep(0.05)
