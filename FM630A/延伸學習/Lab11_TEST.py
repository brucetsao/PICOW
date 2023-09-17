import board
import time
import pwmio

# 設定 GP15 為 PWMOut 物件, 並命名為 led
led = pwmio.PWMOut(board.GP15,
                   frequency=5000,
                   duty_cycle=0)

while True:
    # 數值越來越高, LED 漸漸變亮
    for i in range(0, 65536, 1024):
        led.duty_cycle = i   # 設定 PWM 工作週期控制 LED 亮度
        time.sleep(0.01)     # 暫停 0.01 秒
    # 數值越來越低, LED 漸漸變暗
    for i in range(65535, -1, -1024):
        led.duty_cycle = i   # 設定 PWM 工作週期控制 LED 亮度
        time.sleep(0.01)     # 暫停 0.01 秒