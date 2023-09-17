from machine import ADC
import time

# 設定 A2 為類比輸入腳位, 並命名為 pot
pot = ADC(2)

while True:
    print(pot.read_u16())  # 讀取可變電阻數值
    time.sleep(0.05)       # 暫停 0.05 秒