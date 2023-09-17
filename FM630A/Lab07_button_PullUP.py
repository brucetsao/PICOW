import board
import time
# 增加數位輸出入的 Pull 類別
from digitalio import DigitalInOut, Direction, Pull

# 建立 GP14 腳位的 DigitalInOut 物件, 並命名為 button
button = DigitalInOut(board.GP14)
# 設定 button 為輸入腳位
button.direction = Direction.INPUT
# 設定 button 為上拉電阻
button.pull = Pull.UP

while True:              # 一直重複執行
    # 使用 value 屬性讀取 GP14 腳位的電位值
    print(button.value)  # 使用 print() 輸出電位值
    time.sleep(0.1)      # 暫停 0.1 秒