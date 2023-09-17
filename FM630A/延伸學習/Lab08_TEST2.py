import board
import time
from digitalio import DigitalInOut, Direction, Pull

# 建立 GP15 腳位的 DigitalInOut 物件, 並命名為 led
led = DigitalInOut(board.GP15)
# 設定 led 為輸出腳位
led.direction = Direction.OUTPUT
# 建立 GP14 腳位的 DigitalInOut 物件, 並命名為 button
button = DigitalInOut(board.GP14)
# 設定 button 為輸入腳位
button.direction = Direction.INPUT
# 設定 button 為上拉電阻
button.pull = Pull.UP

while True:                  # 一值重複執行
    if(button.value == 0):
        led.value = not led.value
        time.sleep(0.3)

