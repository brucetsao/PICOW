import board
import time
import analogio
# 設定 A2 為類比輸入腳位, 並命名為 pot
pot = analogio.AnalogIn(board.A2)

while True:
    print(pot.value)  # 讀取可變電阻數值
    time.sleep(0.05)  # 暫停 0.05 秒