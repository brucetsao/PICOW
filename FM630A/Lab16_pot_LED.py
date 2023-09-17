import board
import time
import analogio
import pwmio

pot = analogio.AnalogIn(board.A2)
led = pwmio.PWMOut(board.GP15,
                   frequency=5000,
                   duty_cycle=0)

while True:
    # 將可變電阻的 ADC 值設為 LED 的工作週期
    led.duty_cycle = pot.value
    time.sleep(0.05)