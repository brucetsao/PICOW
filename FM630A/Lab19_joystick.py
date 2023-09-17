import time
import analogio
import board
from digitalio import DigitalInOut, Direction,Pull

x_axis = analogio.AnalogIn(board.A0)
y_axis = analogio.AnalogIn(board.A1)

sw = DigitalInOut(board.GP22)
sw.direction = Direction.INPUT
sw.pull = Pull.UP

while True:
    print(x_axis.value, y_axis.value, sw.value)
    time.sleep(0.05)