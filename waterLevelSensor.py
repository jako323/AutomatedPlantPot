import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

from pinout import WATER_LEVEL_SENSOR_SPI_CHANNEL

WATER_LEVEL_TRESHOLD = 15

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

def read():
    return mcp.read_adc(WATER_LEVEL_SENSOR_SPI_CHANNEL)

def readInPercentage():
    value = mcp.read_adc(WATER_LEVEL_SENSOR_SPI_CHANNEL)
    return round(100/1023 * value)

def isWaterInTank():
    if (readInPercentage() >= WATER_LEVEL_TRESHOLD):
        return True
    else:
        return False
