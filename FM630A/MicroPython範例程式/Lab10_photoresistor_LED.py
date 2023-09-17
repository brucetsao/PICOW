from machine import ADC,Pin
import time

# 建立 Pin 物件, 並命名為 led
led = Pin(15,Pin.OUT)

# 設定 A0 為類比輸入腳位, 並命名為 adc
adc = ADC(0)

while True:
    if adc.read_u16() < 3000:  # 光線不足時
        led.value(1)           # 打開 LED 燈
    else:                      # 否則
        led.value(0)           # 關閉 LED 燈