import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

def read(spiChannel):
    return mcp.read_adc(spiChannel)

def readInPercentage(spiChannel):
    value = mcp.read_adc(spiChannel)
    return round(100/1023 * value)