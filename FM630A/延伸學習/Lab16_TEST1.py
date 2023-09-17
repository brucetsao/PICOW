import board
import time
import analogio
import pwmio

pot = analogio.AnalogIn(board.A2)
led = pwmio.PWMOut(board.GP15,
                   frequency=5000,
                   duty_cycle=0)

while True:
    # 將可變電阻的 ADC 值設為 65535 減掉 LED 的 Duty
    led.duty_cycle = 65535-pot.value
    time.sleep(0.05)
