from machine import ADC
import time

# 設定 A0 為類比輸入腳位, 並命名為 adc
adc = ADC(0)

while True:
    print(adc.read_u16())  # 讀取光敏電阻數值
    time.sleep(0.05)       # 暫停 0.05 秒