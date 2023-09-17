from machine import Pin, Timer
import utime
#led = Pin(25, Pin.OUT)


led_onboard = Pin('LED', Pin.OUT)

while True:
    #led_onboard.toggle()
    led_onboard.on()
    utime.sleep(2)
    led_onboard.off()
    utime.sleep(1)
# led_onboard.toggle() ==> led_onboard.on() and  led_onboard.off()