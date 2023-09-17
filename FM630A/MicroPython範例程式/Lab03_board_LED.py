from machine import Pin
import time

# 建立 Pin 物件, 並命名為 led
led = Pin(25,Pin.OUT)

led.value(1)   # 設定腳位有電, 點亮 LED
time.sleep(3)  # 暫停 3 秒
led.value(0)   # 設定腳位沒電, 熄滅 LED