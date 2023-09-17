import time         
import board         # 控制板子 pico
import digitalio     # 控制板子 IO 腳位
import usb_hid       # 使用 USB HID 協定

# 匯入鍵盤模組
from adafruit_hid.keyboard import Keyboard
# 匯入鍵盤配置模組
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
# 匯入鍵盤對應碼模組
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

btn_copy = digitalio.DigitalInOut(board.GP18)
btn_copy.direction = digitalio.Direction.INPUT
btn_copy.pull = digitalio.Pull.UP

btn_paste = digitalio.DigitalInOut(board.GP19)
btn_paste.direction = digitalio.Direction.INPUT
btn_paste.pull = digitalio.Pull.UP

while True:
    if btn_copy.value == False:
        keyboard.press(Keycode.CONTROL)
        keyboard.press(Keycode.C)
        keyboard.release(Keycode.CONTROL)
        keyboard.release(Keycode.C)
        time.sleep(0.1)
    if btn_paste.value == False:
        keyboard.press(Keycode.CONTROL)
        keyboard.press(Keycode.V)
        keyboard.release(Keycode.CONTROL)
        keyboard.release(Keycode.V)
        time.sleep(0.1)
    time.sleep(0.1)
