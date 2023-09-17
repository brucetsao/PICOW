from machine import PWM,Pin,ADC
import time

# 建立 PWM 物件, 並命名為 led
led = PWM(Pin(15))

# 設定 A2 為類比輸入腳位, 並命名為 pot
pot = ADC(2)

while True:
    # 將可變電阻的 ADC 值設為 LED 的 Duty
    led.duty_u16(pot.read_u16())
    time.sleep(0.05) 