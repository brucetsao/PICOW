
from machine import Pin, PWM
from time import sleep

buzzerPIN=7
BuzzerObj = PWM(Pin(buzzerPIN))

do5=523
dod5=554
re5=587
red5=622
mi5=659
fa5=698
fad5=739
sol5=784
sold5=830
la5=880
lad5=932
si5=987
songlist=[[mi5,0.1,0.1],[red5,0.1,0.1],[mi5,0.1,0.1],
      [red5,0.1,0.1],[mi5,0.1,0.1],[si5,0.1,0.1],
      [re5,0.1,0.1],[do5,0.1,0.1],[la5,0.5,0.1],
      [do5,0.1,0.1],[mi5,0.1,0.1],[la5,0.1,0.1],
      [si5,0.5,0.1],[mi5,0.1,0.1],[sold5,0.1,0.1],
      [si5,0.1,0.1],[do5,0.5,0.1],[mi5,0.1,0.1],
      [red5,0.1,0.1],[mi5,0.1,0.1],[red5,0.1,0.1],
      [mi5,0.1,0.1],[si5,0.1,0.1],[re5,0.1,0.1],
      [do5,0.1,0.1],[la5,0.5,0.1],[do5,0.1,0.1],
      [mi5,0.1,0.1],[la5,0.1,0.1],[si5,0.5,0.1],
      [mi5,0.1,0.1],[do5,0.1,0.1],[si5,0.1,0.1],
      [la5,0.5,0.1],[si5,0.1,0.1],[do5,0.1,0.1],
      [re5,0.1,0.1],[mi5,0.5,0.1],[sol5,0.1,0.1],
      [fa5,0.1,0.1],[mi5,0.1,0.1],[re5,0.5,0.1],
      [fa5,0.1,0.1],[mi5,0.1,0.1],[re5,0.1,0.1],
      [do5,0.5,0.1],[mi5,0.1,0.1],[re5,0.1,0.1],
      [do5,0.1,0.1],[si5,0.5,0.1],[mi5,0.1,0.1],
      [red5,0.1,0.1],[mi5,0.1,0.1],[red5,0.1,0.1],
      [mi5,0.1,0.1],[si5,0.1,0.1],[re5,0.1,0.1],
      [do5,0.1,0.1],[la5,0.5,0.1],[do5,0.1,0.1],
      [mi5,0.1,0.1],[la5,0.1,0.1],[si5,0.5,0.1],
      [mi5,0.1,0.1],[do5,0.1,0.1],[si5,0.1,0.1],
      [la5,0.5,0.1]]


def buzzer(buzzerPinObject,frequency,sound_duration,silence_duration):

    # Set duty cycle to a positive value to emit sound from buzzer
    buzzerPinObject.duty_u16(int(65536*0.1))
    # Set frequency
    buzzerPinObject.freq(frequency)
    # wait for sound duration
    sleep(sound_duration)
    # Set duty cycle to zero to stop sound
    buzzerPinObject.duty_u16(int(65536*0))
    # Wait for sound interrumption, if needed 
    sleep(silence_duration)

def playsong(beep,song):
    for x in song:
        buzzer(beep,x[0],x[1],x[2])
    beep.deinit()    
    #Deactivates the buzzer    
#set translation table from note to frequency

playsong(BuzzerObj,songlist)