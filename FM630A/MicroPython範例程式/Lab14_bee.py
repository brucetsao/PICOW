from machine import PWM,Pin
import time

# 建立 Pin 物件, 並啟用上拉電阻, 並命名為 button
button = Pin(14,Pin.IN,Pin.PULL_UP)

# 建立 PWM 物件, 並命名為 buzzer
buzzer = PWM(Pin(13))

# 小蜜蜂
# |So Mi Mi -|Fa Re Re -| Do Re Mi Fa So So So -|
notes = [392 ,330 ,330 ,0 ,
         349 ,294 ,294 ,0 ,
         262 ,294 ,330 ,349 ,392 ,392 ,392]

while True:
    # 當按下按鈕時, 發出音樂
    if button.value() == 0:
        for note in notes:
            if note == 0:                     # 設為 0 時不發音
                buzzer.duty_u16(0)            # 設定音量為 0
            else:                             # 否則
                buzzer.freq(note)             # 設定聲音頻率
                buzzer.duty_u16(2**15)        # 設定音量為 2**15
            time.sleep(0.2)                   # 聲音持續 0.2 秒
        buzzer.duty_u16(0)                    # 停止發聲
        time.sleep(0.1)                       # 持續停止發聲 0.1 秒
