from machine import Pin
from time import sleep
import dht
 
sensor = dht.DHT22(Pin(16)) 
#sensor1 = dht.DHT11(Pin(16)) 
 
while True:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print("Temperature: {}°C   Humidity: {:.0f}% ".format(temp, hum))
    sleep(2)