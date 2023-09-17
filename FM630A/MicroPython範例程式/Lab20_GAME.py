from machine import Pin,ADC
import time
import random

x_axis = ADC(0)
y_axis = ADC(1)

# 建立 Pin 物件, 並啟用上拉電阻, 並命名為 sw
button = Pin(22,Pin.IN,Pin.PULL_UP)

score = 0
newIndicator = False
indicators =['UP', 'RIGHT', 'DOWN', 'LEFT', 'Click!']

print("Hit [CENTER BUTTON] to START!")
t_start = time.time()

# 按下按鈕開關 或是 10秒 後開始遊戲
while time.time() - t_start < 10:
    if not button.value():
        break
    time.sleep(0.1)
    
# 遊戲開始時間
game_start = time.time()

while(time.time() - game_start < 10):
    # 沒新指令 且 雙軸至中才會更換
    if(newIndicator == False and
       x_axis.read_u16() > 10000 and
       x_axis.read_u16() < 60000 and
       y_axis.read_u16() > 10000 and
       y_axis.read_u16() < 60000 and
       button.value()):
        newIndicator = True
        q = random.choice(indicators)
        print("\n"+q)
    # 有新指令 且 遊戲 10 秒內
    while(newIndicator and time.time() - game_start < 10):
        if(((q == 'UP') and (y_axis.read_u16() < 10000)) or 
           ((q == 'DOWN') and (y_axis.read_u16() > 60000)) or 
           ((q == 'LEFT') and (x_axis.read_u16() < 10000)) or 
           ((q == 'RIGHT') and (x_axis.read_u16() > 60000)) or 
           ((q == 'Click!') and not button.value())):
            newIndicator = False
            score += 1
            print('score : ', score)
            
print('Your Score : ', score, '!')