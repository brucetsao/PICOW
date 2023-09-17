from machine import PWM,Pin,ADC
import time

# 建立 PWM 物件, 並命名為 buzzer
buzzer = PWM(Pin(13))
buzzer.duty_u16(2**15)

# 設定 A2 為類比輸入腳位, 並命名為 pot
pot = ADC(2)

while True:
    # 將可變電阻的 ADC 值轉換成 BPM
    beat = int(pot.read_u16()*210/65460) + 40
    
    # 開啟聲音
    buzzer.duty_u16(2**15)
    time.sleep(0.1)
    # 關閉聲音
    buzzer.duty_u16(0)
    time.sleep(60/beat) 