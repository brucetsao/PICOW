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

while True:
    # 當按鈕按下時, 發出 "叮咚" 聲音
    if button.value == False:
        # "叮" 頻率約 988, 聲音持續較短
        buzzer.frequency = 988
        buzzer.duty_cycle = 2**15
        time.sleep(0.3)
        buzzer.duty_cycle = 0
        # "咚" 頻率約 784, 聲音持續較長
        buzzer.frequency = 784
        buzzer.duty_cycle = 2**15
        time.sleep(0.3)
        buzzer.duty_cycle = 0
                # "叮" 頻率約 988, 聲音持續較短
        buzzer.frequency = 988
        buzzer.duty_cycle = 2**15
        time.sleep(0.3)
        buzzer.duty_cycle = 0
