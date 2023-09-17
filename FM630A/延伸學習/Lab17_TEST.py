import board
import time
import analogio
import pwmio

buzzer = pwmio.PWMOut(board.GP13,
                      frequency=523,
                      duty_cycle=2**15,
                      variable_frequency=True)

pot = analogio.AnalogIn(board.A2)

while True:
    # 將可變電阻的值(0~65535)轉換成 262~1976
    freq = int((65535-pot.value)*1714 / 65535) + 262
    buzzer.frequency = freq
    time.sleep(0.05)
