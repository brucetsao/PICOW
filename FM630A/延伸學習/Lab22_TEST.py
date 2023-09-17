import time
import analogio
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

mouse = Mouse(usb_hid.devices)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

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

btn_copy = digitalio.DigitalInOut(board.GP20)
btn_copy.direction = digitalio.Direction.INPUT
btn_copy.pull = digitalio.Pull.UP

btn_paste = digitalio.DigitalInOut(board.GP21)
btn_paste.direction = digitalio.Direction.INPUT
btn_paste.pull = digitalio.Pull.UP

pot_min = 0
pot_max = 65535
step = (pot_max - pot_min) / 20

def steps(axis):
    return round((axis.value - pot_min) / step)

while True:
    if btn_copy.value == False:
        keyboard.press(Keycode.CONTROL)
        keyboard.press(Keycode.C)
        keyboard.release(Keycode.CONTROL)
        keyboard.release(Keycode.C)
        time.sleep(0.2)
    if btn_paste.value == False:
        keyboard.press(Keycode.CONTROL)
        keyboard.press(Keycode.V)
        keyboard.release(Keycode.CONTROL)
        keyboard.release(Keycode.V)
        time.sleep(0.2)
    
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
