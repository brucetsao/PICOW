from machine import Pin
import time

# 建立 Pin 物件, 並命名為 led
led = Pin(15,Pin.OUT)

while True:         # 一值重複執行
    led.value(1)    # 設定腳位有電, 點亮 LED
    time.sleep(0.5) # 暫停 0.5 秒
    led.value(0)    # 設定腳位沒電, 熄滅 LED
    time.sleep(0.5) # 暫停 0.5 秒