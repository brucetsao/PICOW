from machine import PWM,Pin
import time

# 建立 PWM 物件, 並命名為 buzzer
buzzer = PWM(Pin(13))
# 設定 frequency 頻率為 Do 262Hz
buzzer.freq(262)

buzzer.duty_u16(2**15)
time.sleep(1)
buzzer.duty_u16(0)