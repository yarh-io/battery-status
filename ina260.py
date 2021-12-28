import time
import board
import adafruit_ina260

i2c = board.I2C()
ina260 = adafruit_ina260.INA260(i2c, address=0x40)
while True:
    print("U = %.2f V, I = %.2f mA, P = %.2f mW" % (ina260.voltage, ina260.current, ina260.power))
    time.sleep(1)
