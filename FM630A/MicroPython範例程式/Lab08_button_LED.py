from machine import Pin
import time

# 建立 Pin 物件, 並命名為 led
led = Pin(15,Pin.OUT)

# 建立 Pin 物件, 並啟用上拉電阻, 並命名為 button
button = Pin(14,Pin.IN,Pin.PULL_UP)

while True:            # 一值重複執行
    if button.value() == 0: # 如果按下按壓開關
        led.value(1)      # 點亮 LED
    else:                 # 否則
        led.value(0)      # 熄滅 LED

