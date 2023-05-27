import BlynkLib
import RPi.GPIO as GPIO
from BlynkTimer import BlynkTimer

import sys
sys.path.append('/home/jako/Projects/AutomatedPlantPot')
from pinout import PLANT_A_PUMP_PIN, PLANT_B_PUMP_PIN, PLANT_C_PUMP_PIN, PLANT_D_PUMP_PIN
from pinout import PLANT_A_HUMSENSOR_SPI_CHANNEL, PLANT_B_HUMSENSOR_SPI_CHANNEL, PLANT_C_HUMSENSOR_SPI_CHANNEL, PLANT_D_HUMSENSOR_SPI_CHANNEL
from pinout import WATER_LEVEL_SENSOR_SPI_CHANNEL, LIGHT_SENSOR_SPI_CHANNEL
import plantSetupInfo

GPIO.setmode(GPIO.BCM)
GPIO.setup(PLANT_A_PUMP_PIN, GPIO.OUT)
GPIO.setup(PLANT_B_PUMP_PIN, GPIO.OUT)
GPIO.setup(PLANT_C_PUMP_PIN, GPIO.OUT)
GPIO.setup(PLANT_D_PUMP_PIN, GPIO.OUT)

# Autorization
BLYNK_AUTH_TOKEN = 'Py0byXhpv0OqVpYhayvmhZD4vi2HTSkK'
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

# PUMP A
@blynk.on("V0")
def v0_write_handler(value):
    if int(value[0]) != 0:
        GPIO.output(PLANT_A_PUMP_PIN, GPIO.HIGH)
        print('PUMP A ON')
    else:
        GPIO.output(PLANT_A_PUMP_PIN, GPIO.LOW)
        print('PUMP A OFF')

# PUMP B
@blynk.on("V1")
def v1_write_handler(value):
    if int(value[0]) != 0:
        GPIO.output(PLANT_B_PUMP_PIN, GPIO.HIGH)
        print('PUMP B ON')
    else:
        GPIO.output(PLANT_B_PUMP_PIN, GPIO.LOW)
        print('PUMP B OFF')
        
# PUMP C
@blynk.on("V2")
def v2_write_handler(value):
    if int(value[0]) != 0:
        GPIO.output(PLANT_C_PUMP_PIN, GPIO.HIGH)
        print('PUMP C ON')
    else:
        GPIO.output(PLANT_C_PUMP_PIN, GPIO.LOW)
        print('PUMP C OFF')

# PUMP D
@blynk.on("V3")
def v3_write_handler(value):
    if int(value[0]) != 0:
        GPIO.output(PLANT_D_PUMP_PIN, GPIO.HIGH)
        print('PUMP D ON')
    else:
        GPIO.output(PLANT_D_PUMP_PIN, GPIO.LOW)
        print('PUMP D OFF')
        
# Sync data
@blynk.on("connected")
def blynk_connected():
    print("Raspberry Pi Connected to New Blynk") 

while True:
    blynk.run()
   
