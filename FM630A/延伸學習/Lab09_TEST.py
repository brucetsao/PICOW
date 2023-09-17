import board
import time
# 匯入 analogio 模組的 AnalogIn 類別
from analogio import AnalogIn
# 設定 A0 為類比輸入腳位, 並命名為 adc
adc = AnalogIn(board.A0)

while True:
    print(adc.value*3.3/65535)  # 讀取光敏電阻數值轉換後的電壓
    time.sleep(0.05)            # 暫停 0.05 秒
