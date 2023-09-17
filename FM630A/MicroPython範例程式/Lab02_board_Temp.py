import machine

# 溫度感測器連接到 ADC4
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

# 將 ADC 值轉換成電壓
reading = sensor_temp.read_u16() * conversion_factor

# 通常電壓 0.706V 時代表溫度 27℃, 當電壓下降 0.001721V 代表上升一度
temperature = 27 - (reading - 0.706)/0.001721
print(temperature)