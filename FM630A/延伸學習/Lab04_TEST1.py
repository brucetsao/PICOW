# 匯入 Pico 控制板相關的 board 模組
import board
# 匯入時間相關的 time 模組
import time
# 匯入數位輸出入的 DigitalInOut、Direction 模組
from digitalio import DigitalInOut, Direction

# 建立 GPIO15 腳位的 DigitalInOut 物件, 並命名為 led
led = DigitalInOut(board.GP15)
# 設定 led 為輸出腳位
led.direction = Direction.OUTPUT

led.value = True    # 設定腳位有電, 點亮 LED
time.sleep(10)      # 暫停 10 秒
led.value = False   # 設定腳位沒電, 熄滅 LED
