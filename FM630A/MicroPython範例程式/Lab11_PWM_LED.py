from machine import PWM,Pin
import time

# 建立 PWM 物件, 並命名為 led
led = PWM(Pin(15))

while True:
    # 數值越來越高, LED 漸漸變亮
    for i in range(0, 65536, 512):
        led.duty_u16(i)      # 設定 PWM 工作週期控制 LED 亮度
        time.sleep(0.01)     # 暫停 0.01 秒
    for i in range(65535, -1, -512):
        led.duty_u16(i)      # 設定 PWM 工作週期控制 LED 亮度
        time.sleep(0.01)     # 暫停 0.01 秒