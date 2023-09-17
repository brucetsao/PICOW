# 匯入控制板中的 microcontroller 模組
import microcontroller
# 讀取模組內 cpu 物件的 temperature 屬性
print('Pico 控制板攝氏溫度:',microcontroller.cpu.temperature)
print('Pico 控制板華氏溫度:',microcontroller.cpu.temperature*(9/5)+32)