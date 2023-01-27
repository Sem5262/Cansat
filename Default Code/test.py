from machine import I2C
import time
i2c  = I2C(0)
while True:
    time.sleep(2)
    print(i2c.scan())