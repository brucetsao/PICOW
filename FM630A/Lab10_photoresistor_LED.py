import board
import time
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction

# 建立 A0 腳位的 AnalogIn 物件, 並命名為 adc
adc = AnalogIn(board.GP26_A0)
# 建立 GP15 腳位的 DigitalInOut 物件, 並命名為 led
led = DigitalInOut(board.GP15)
# 設定 led 為輸出腳位
led.direction = Direction.OUTPUT

while True:
    if adc.value < 3000:  # 光線不足時
        led.value = True  # 打開 LED 燈
    else:                 # 否則
        led.value = False # 關閉 LED 燈