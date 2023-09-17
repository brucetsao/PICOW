import board
import time
from digitalio import DigitalInOut, Direction

# 建立 GP14 腳位的 DigitalInOut 物件, 並命名為 button
button = DigitalInOut(board.GP14)
# 設定 button 為輸入腳位
button.direction = Direction.INPUT

while True:              # 一直重複執行
    # 使用 value 屬性讀取 GP14 腳位的電位值
    print(button.value)  # 使用 print() 輸出按壓開關電位值
    time.sleep(0.1)      # 暫停 0.1 秒
