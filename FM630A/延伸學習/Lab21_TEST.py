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

btn_plus = digitalio.DigitalInOut(board.GP18)
btn_plus.direction = digitalio.Direction.INPUT
btn_plus.pull = digitalio.Pull.UP

btn_minus = digitalio.DigitalInOut(board.GP19)
btn_minus.direction = digitalio.Direction.INPUT
btn_minus.pull = digitalio.Pull.UP

while True:
    if btn_plus.value == False:
        keyboard.press(Keycode.WINDOWS)
        keyboard.press(Keycode.KEYPAD_PLUS)
        keyboard.release(Keycode.WINDOWS)
        keyboard.release(Keycode.KEYPAD_PLUS)
        time.sleep(0.1)
    if btn_minus.value == False:
        keyboard.press(Keycode.WINDOWS)
        keyboard.press(Keycode.KEYPAD_MINUS)
        keyboard.release(Keycode.WINDOWS)
        keyboard.release(Keycode.KEYPAD_MINUS)
        time.sleep(0.1)
    time.sleep(0.1)

