import board
import time
import pwmio
from digitalio import DigitalInOut, Direction, Pull

# 設定 GP14 為數位輸入腳位, 並命名為 button
button = DigitalInOut(board.GP14)
button.direction = Direction.INPUT
button.pull = Pull.UP

# 設定 GP13 為 PWM 輸出腳位, 並命名為 buzzer
buzzer = pwmio.PWMOut(board.GP13,
                      frequency=262,
                      duty_cycle=0,
                      variable_frequency=True)
# 小蜜蜂
# |So Mi Mi -|Fa Re Re -| Do Re Mi Fa So So So -|
notes = [392 ,330 ,330 ,0 ,
         349 ,294 ,294 ,0 ,
         262 ,294 ,330 ,349 ,392 ,392 ,392]

while True:
    # 當按下按鈕時, 發出音樂
    if button.value == False:                 # 一一取出音符
        for note in notes:
            if note == 0:                     # 設為 0 時不發音
                buzzer.duty_cycle = 0         # 設定音量為 0       
            else:                             # 否則
                buzzer.frequency = note       # 設定聲音頻率
                buzzer.duty_cycle = 2 ** 15   # 設定音量為 2**15               
            time.sleep(0.05)                  # 聲音持續 0.05 秒
            buzzer.duty_cycle = 0             # 停止發聲
            time.sleep(0.1)                   # 持續停止發聲 0.1 秒
