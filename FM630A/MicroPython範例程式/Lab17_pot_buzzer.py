from machine import PWM,Pin,ADC
import time

# 建立 PWM 物件, 並命名為 buzzer
buzzer = PWM(Pin(13))
buzzer.duty_u16(2**15)

# 設定 A2 為類比輸入腳位, 並命名為 pot
pot = ADC(2)

while True:
    # 將可變電阻的值(0~65535)轉換成 262~1976
    frequ = int(pot.read_u16()*1714 / 65535) + 262
    buzzer.freq(frequ)
    time.sleep(0.05) 
