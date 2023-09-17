from machine import Pin, I2C	#使用I2C與GPIO腳位之函式庫
from utime import sleep	#=匯入utime 套件，使用sleep 物件

from htu21d import HTU21D		#使用HTU21D 溫濕度感測元件

#i2c0_sda = Pin(8)
#i2c0_scl = Pin(9)
#i2c0 = I2C(0, sda=i2c0_sda, scl=i2c0_scl)
i2c = I2C(id=1,scl=Pin(7),sda=Pin(6),freq=100_000)
#產生連接腳位GPIO16之DHT22 溫濕度感測元件之操控物件sensor
htu21d = HTU21D(0x40, i2c)

while True:
    measurements = htu21d.measurements
    print(f"Temperature: {measurements['t']} °C, humidity: {measurements['h']} %RH")
    sleep(1)