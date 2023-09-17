import time
import analogio
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

x_axis = analogio.AnalogIn(board.A0)
y_axis = analogio.AnalogIn(board.A1)

button = digitalio.DigitalInOut(board.GP22)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

btn_left = digitalio.DigitalInOut(board.GP18)
btn_left.direction = digitalio.Direction.INPUT
btn_left.pull = digitalio.Pull.UP

btn_right = digitalio.DigitalInOut(board.GP19)
btn_right.direction = digitalio.Direction.INPUT
btn_right.pull = digitalio.Pull.UP

pot_min = 0
pot_max = 65535
step = (pot_max - pot_min) / 20

def steps(axis):
    return round((axis.value - pot_min) / step)

while True:
    x = x_axis
    y = y_axis
    
    if button.value == False:
        mouse.click(Mouse.MIDDLE_BUTTON)
        print("Click!")
        time.sleep(0.3)
        
    if btn_left.value == False:
        mouse.click(Mouse.LEFT_BUTTON)
        time.sleep(0.3)
        
    if btn_right.value == False:
        mouse.click(Mouse.RIGHT_BUTTON)
        time.sleep(0.3)
    # x 軸位移距離 1
    if steps(x) > 11:
        mouse.move(x=1)
    if steps(x) < 9:
        mouse.move(x=-1)
    # x 軸位移距離 8
    if steps(x) > 19:
        mouse.move(x=8)
    if steps(x) < 1:
        mouse.move(x=-8)
    # y 軸位移距離 1
    if steps(y) > 11:
        mouse.move(y=1)     # y 軸位移距離 8
    if steps(y) < 9:
        mouse.move(y=-1)    
    # y 軸位移距離 8
    if steps(y) > 19:
        mouse.move(y=8)    
    if steps(y) < 1:
        mouse.move(y=-8)