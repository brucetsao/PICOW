# 匯入控制板子相關 board 模組
import board
# 匯入時間相關 time 模組
import time
# 匯入數位輸出入的 DigitalInOut、Direction 模組
from digitalio import DigitalInOut, Direction

# 建立 GP15 腳位的 DigitalInOut 物件, 並命名為 led1
led1 = DigitalInOut(board.GP15)
# 設定 led 為輸出腳位
led1.direction = Direction.OUTPUT

# 建立 GP12 腳位的 DigitalInOut 物件, 並命名為 led2
led2 = DigitalInOut(board.GP12)
# 設定 led 為輸出腳位
led2.direction = Direction.OUTPUT

while True:              # 一直重複執行
    led1.value = True    # 設定腳位有電, 點亮 LED1
    led2.value = False   # 設定腳位沒電, 熄滅 LED2
    time.sleep(0.5)      # 暫停 0.5 秒
    led1.value = False   # 設定腳位沒電, 熄滅 LED1
    led2.value = True    # 設定腳位有電, 點亮 LED2
    time.sleep(0.5)      # 暫停 0.5 秒
