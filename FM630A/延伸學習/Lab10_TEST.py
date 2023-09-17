import board
import time
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction

# 建立 A0 腳位的 AnalogIn 物件, 並命名為 adc
adc = AnalogIn(board.GP26_A0)
# 建立 GP15 腳位的 DigitalInOut 物件, 並命名為 led1
led1 = DigitalInOut(board.GP15)
# 設定 led 為輸出腳位
led1.direction = Direction.OUTPUT
# 建立 GP12 腳位的 DigitalInOut 物件, 並命名為 led2
led2 = DigitalInOut(board.GP12)
# 設定 led 為輸出腳位
led2.direction = Direction.OUTPUT
# 建立 GP11 腳位的 DigitalInOut 物件, 並命名為 led3
led3 = DigitalInOut(board.GP11)
# 設定 led 為輸出腳位
led3.direction = Direction.OUTPUT

while True:
    if adc.value < 800:    # 光線很不足時
        led1.value = True  # 打開 LED 燈
        led2.value = True  # 打開 LED 燈
        led3.value = True  # 打開 LED 燈
    elif adc.value < 1800:  # 光線有點不足時
        led1.value = True  # 打開 LED 燈
        led2.value = True  # 打開 LED 燈
        led3.value = False  # 關閉 LED 燈
    elif adc.value < 2800:  # 光線有點亮時
        led1.value = True   # 打開 LED 燈
        led2.value = False  # 關閉 LED 燈
        led3.value = False  # 關閉 LED 燈
    else:                   # 光線很亮時
        led1.value = False  # 關閉 LED 燈
        led2.value = False  # 關閉 LED 燈
        led3.value = False  # 關閉 LED 燈
