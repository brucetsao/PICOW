from machine import PWM,Pin
import time

# 建立 Pin 物件, 並啟用上拉電阻, 並命名為 button
button = Pin(14,Pin.IN,Pin.PULL_UP)

# 建立 PWM 物件, 並命名為 buzzer
buzzer = PWM(Pin(13))

while True:
    # 當按鈕按下時, 發出 "叮咚" 聲音
    if button.value() == 0:
        # "叮" 頻率約 988, 聲音持續較短
        buzzer.freq(988)
        buzzer.duty_u16(2**15)
        time.sleep(0.6)
        buzzer.duty_u16(0)
        # "咚" 頻率約 784, 聲音持續較長
        buzzer.freq(784)
        buzzer.duty_u16(2**15)
        time.sleep(1.2)
        buzzer.duty_u16(0)