from machine import Pin
import time

# 建立 Pin 物件, 並啟用上拉電阻, 並命名為 button
button = Pin(14,Pin.IN,Pin.PULL_UP)

while True:            # 一值重複執行
    # 讀取 GP14 腳位的電位值
    print(button.value())  
    time.sleep(0.1)    # 暫停 0.1 秒