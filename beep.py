from machine import Pin, Timer
import utime

buzzer_onboard = Pin(7, Pin.OUT)

while True:
    #buzzer_onboard.toggle()
    buzzer_onboard.on()
    utime.sleep(2)
    buzzer_onboard.off()
    utime.sleep(1)
# buzzer_onboard.toggle() ==> buzzer_onboard.on() and  buzzer_onboard.off()