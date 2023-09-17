# 匯入控制板子相關 board 模組
import board
# 匯入時間相關 time 模組
import time
# 匯入數位輸出入的 DigitalInOut、Direction 模組
from digitalio import DigitalInOut, Direction

# 建立 GP15 腳位的 DigitalInOut 物件, 並命名為 led
led = DigitalInOut(board.GP15)
# 設定 led 為輸出腳位
led.direction = Direction.OUTPUT

while True:             # 一直重複執行
    led.value = True    # 設定腳位有電, 點亮 LED
    time.sleep(0.1)     # 暫停 0.1 秒
    led.value = False   # 設定腳位沒電, 熄滅 LED
    time.sleep(0.1)     # 暫停 0.1 秒
    led.value = True    # 設定腳位有電, 點亮 LED
    time.sleep(0.1)     # 暫停 0.1 秒
    led.value = False   # 設定腳位沒電, 熄滅 LED
    time.sleep(3)     # 暫停 0.1 秒