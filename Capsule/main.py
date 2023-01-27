from machine import SPI, Pin, I2C
import time

# sensors
from rfm69 import RFM69
from bme280 import BME280, BMP280_I2CADDR



# Radio init/ settings

FREQ           = 433.1
ENCRYPTION_KEY = b"\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08"
NODE_ID        = 120 # ID of this node
BASESTATION_ID = 100 # ID of the node (base station) to be contacted

spi = SPI(0, baudrate=50000, polarity=0, phase=0, firstbit=SPI.MSB)
nss = Pin( 5, Pin.OUT, value=True )
rst = Pin( 3, Pin.OUT, value=False )

rfm = RFM69( spi=spi, nss=nss, reset=rst )
rfm.frequency_mhz = FREQ

rfm.encryption_key = ( ENCRYPTION_KEY )
rfm.node    = NODE_ID # This instance is the node 120


rfm.ack_retries = 3 # 3 attempt to receive ACK
rfm.ack_wait    = 0.5 # 500ms, time to wait for ACK 
rfm.destination = BASESTATION_ID # Send to specific node 100




# BME280 init


i2c = I2C(0)
bmp = BME280( i2c=i2c, address=BMP280_I2CADDR )



while True:
    try:
        rfm.send_with_ack( bmp.raw_values , "utf-8")
        time.sleep(0.1)
    except:
        pass


