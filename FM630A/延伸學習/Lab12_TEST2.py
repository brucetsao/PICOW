import board
import time
import pwmio

# 設定 GP13 為 PWMOut 物件, 並命名為 buzzer
# 設定 frequency 頻率為 Do 262Hz
buzzer = pwmio.PWMOut(board.GP13,
                      frequency=262,
                      duty_cycle=0)
buzzer.duty_cycle = 2**8   # 設定工作週期(音量)為 2**15
time.sleep(1)               # 暫停 1 秒鐘
buzzer.duty_cycle = 0       # 設定工作週期(音量)為 0
