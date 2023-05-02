import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

from pinout import LIGHT_SENSOR_SPI_CHANNEL

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

def read():
    return mcp.read_adc(LIGHT_SENSOR_SPI_CHANNEL)

def readInPercentage():
    value = mcp.read_adc(LIGHT_SENSOR_SPI_CHANNEL)
    return round(100/1023 * value)