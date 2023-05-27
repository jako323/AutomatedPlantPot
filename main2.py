import RPi.GPIO as GPIO
import time

import pinout
from pinout import PLANT_A_PUMP_PIN, PLANT_B_PUMP_PIN, PLANT_C_PUMP_PIN, PLANT_D_PUMP_PIN
from pinout import PLANT_A_HUMSENSOR_SPI_CHANNEL, PLANT_B_HUMSENSOR_SPI_CHANNEL, PLANT_C_HUMSENSOR_SPI_CHANNEL, PLANT_D_HUMSENSOR_SPI_CHANNEL
from pinout import WATER_LEVEL_SENSOR_SPI_CHANNEL, LIGHT_SENSOR_SPI_CHANNEL

from PlantClass import Plant
import waterLevelSensor
import lightSensor

from Blynk import BlynkLib
import RPi.GPIO as GPIO
from Blynk import BlynkTimer

# Autorization
BLYNK_AUTH_TOKEN = 'Py0byXhpv0OqVpYhayvmhZD4vi2HTSkK'
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)


GPIO.setmode(GPIO.BCM)
GPIO.setup(PLANT_A_PUMP_PIN, GPIO.OUT)
GPIO.setup(PLANT_B_PUMP_PIN, GPIO.OUT)
GPIO.setup(PLANT_C_PUMP_PIN, GPIO.OUT)
GPIO.setup(PLANT_D_PUMP_PIN, GPIO.OUT)


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
            
    # Wyświetlanie odczytanych wartości
    print("Wartość z pinu 0:", pin4_value)
    print("Wartość z pinu 1:", pin5_value)
    print("Wartość z pinu 2:", pin6_value)
    print("Wartość z pinu 3:", pin7_value)

# Sync data
@blynk.on("connected")
def blynk_connected():
    print("Raspberry Pi Connected to New Blynk") 


 
# === INITIALIZING PLANTS ===
plantA = Plant('A', pinout.PLANT_A_PUMP_PIN, pinout.PLANT_A_HUMSENSOR_SPI_CHANNEL)
plantB = Plant('B', pinout.PLANT_B_PUMP_PIN, pinout.PLANT_B_HUMSENSOR_SPI_CHANNEL)
plantC = Plant('C', pinout.PLANT_C_PUMP_PIN, pinout.PLANT_C_HUMSENSOR_SPI_CHANNEL)
plantD = Plant('D', pinout.PLANT_D_PUMP_PIN, pinout.PLANT_D_HUMSENSOR_SPI_CHANNEL)

    # Funkcja obsługująca odczyt wartości z pinów
def read_pins():
    # Odczyt wartości z pinu 0
    pinout.PLANT_A_HUMSENSOR_SPI_CHANNEL = blynk.get_pin_value(4)
    
    # Odczyt wartości z pinu 1
    pinout.PLANT_B_HUMSENSOR_SPI_CHANNEL = blynk.get_pin_value(5)
    
    # Odczyt wartości z pinu 2
    pinout.PLANT_C_HUMSENSOR_SPI_CHANNEL = blynk.get_pin_value(6)
    
    # Odczyt wartości z pinu 3
    pinout.PLANT_D_HUMSENSOR_SPI_CHANNEL = blynk.get_pin_value(7)
  

# === GPIO SETUP ===
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(plantA.pumpPin, GPIO.OUT)
GPIO.setup(plantB.pumpPin, GPIO.OUT)
GPIO.setup(plantC.pumpPin, GPIO.OUT)
GPIO.setup(plantD.pumpPin, GPIO.OUT)


# === MAIN LOOP ===
while True:
    print("=======================================================================================================================================")
    # === GETTING DATA FROM THE INTERNET ===
    plantA.updateParameters()
    plantB.updateParameters()
    plantC.updateParameters()
    plantD.updateParameters()


    # === WATERING ===
    currentEpochTime = (int)(time.time())
    print("Current Time:", time.localtime(currentEpochTime))

    if (waterLevelSensor.isWaterInTank()):
        if (plantA.checkForWateringNeed(currentEpochTime)):
            plantA.watering()
        if (plantB.checkForWateringNeed(currentEpochTime)):
            plantB.watering()
        if (plantC.checkForWateringNeed(currentEpochTime)):
            plantC.watering()
        if (plantD.checkForWateringNeed(currentEpochTime)):
            plantD.watering()
    else:
        print("Water level in tank dropped below given treshold. All watering actions are suspended.")
        print("Please fill up the water compartment.")


    # === SENDING DATA TO THE INTERNET ===
    print("Current tank's water level: ", waterLevelSensor.readInPercentage(), "%", sep="")
    print("Current pot's light level:  ", lightSensor.readInPercentage(), "%", sep="")
    
  
    
    blynk.run()
    time.sleep(0.5)



#GPIO.cleanup()