import board
import time
import analogio
import pwmio

buzzer = pwmio.PWMOut(board.GP13,
                      frequency=350,
                      duty_cycle=0)

pot = analogio.AnalogIn(board.A2)

while True:
    # 將可變電阻的 ADC 值轉換成 BPM
    bpm = int(pot.value*210/65460) + 40
    
    # 開啟聲音
    buzzer.duty_cycle = 2**15
    time.sleep(0.1)
    # 關閉聲音
    buzzer.duty_cycle = 0
    time.sleep(60/bpm)