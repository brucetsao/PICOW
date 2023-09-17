from machine import Pin,ADC
import time

x_axis = ADC(0)
y_axis = ADC(1)

# 建立 Pin 物件, 並啟用上拉電阻, 並命名為 sw
sw = Pin(22,Pin.IN,Pin.PULL_UP)

while True:
    print(x_axis.read_u16(),y_axis.read_u16(),sw.value())
    time.sleep(0.05) 