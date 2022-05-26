import digitalio
import board
import time
import adafruit_bmp280
import radio

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = True
print("CanSat Hello!")
test_value = 3.14159
print(test_value)
print("Test value {:d}". format(int(test_value)))
while True:
    led.value = False
    time.sleep(0.5)
    led.value = True
    time.sleep(0.5)

i2c = busio.I2C(scl = board.GP15, sda = board.GP14)
bmp280_sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

def read_temperature():
    return bmp280_sensor.temperature
    cansat_temperature = bmp280.read_temperature()
    print(cansat_temperature)

def read_pressure():
    return bmp280_pressure.temperature  
    cansat_pressure = bmp280.read_pressure()
    print(cansat_pressure)